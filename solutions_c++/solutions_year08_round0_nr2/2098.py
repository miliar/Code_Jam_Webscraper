// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <algorithm>
#include <numeric>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <iterator>
#include <cmath>
using namespace std;

struct date
{
	int h, m;
	date(){}
	date(int i_h, int i_m) { h = i_h, m = i_m; }
	bool operator == (date b) { return h == b.h && m == b.m; }
	friend ostream& operator << (ostream& out, date a)
	{ return out<<a.h<<":"<<a.m<<" "; }
};

struct voyage
{
	date dep, arr;
	voyage(){  }
	voyage(date a, date b) { dep = a, arr = b; }
};

	bool operator < (date a, date b)
	{
		if(a.h==b.h)
			return a.m < b.m;
		return a.h < b.h;
	}
	bool operator < (voyage a, voyage b)
	{
		if(a.dep == b.dep)
			return a.arr < b.arr;
		return a.dep < b.dep;
	}

	class Dless
	{
	public:
		bool operator () (date a, date b)
		{
			if(a.h==b.h)
				return a.m > b.m;
			return a.h > b.h;
		}
	};
	class Vless
	{
	public:
		bool operator () (voyage a, voyage b)
		{
			if(a.dep == b.dep)
				return b.arr < a.arr;
			return b.dep < a.dep;
		}
	};

int T;
int obsluz(priority_queue<voyage, vector<voyage>, Vless>& SA, priority_queue<date, vector<date>, Dless> & A, priority_queue<date, vector<date>, Dless> & B)
{
	int res = 1;

	voyage t = SA.top();
	//cout<<"obsluguje "<<t.dep<<t.arr<<endl;
	//if(A.size()!=0) cout<<"czeka na mnie "<<A.top()<<endl;
	SA.pop();
	if(A.size()!=0)
		if(!( t.dep < A.top() ))
			res = 0, A.pop();
	t.arr.m+=T;
	t.arr.h+=t.arr.m/60;
	t.arr.m%=60;
	B.push(t.arr);

	return res;
}

// BEGIN CUT HERE
int main()
{
	int N, NA, NB, i, j, A , B, t1,t2,t3,t4;
	scanf("%d", &N);
	for(i = 1; i <= N; i++)
	{
		A = B = 0;
		priority_queue<voyage, vector<voyage>, Vless> SA, SB;
		priority_queue<date, vector<date>, Dless> QA, QB;
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);

		for(j = 0; j < NA; j++)
			scanf("%d:%d %d:%d", &t1, &t2, &t3, &t4), SA.push(voyage(date(t1,t2), date(t3,t4)));
		for(j = 0; j < NB; j++)
			scanf("%d:%d %d:%d", &t1, &t2, &t3, &t4), SB.push(voyage(date(t1,t2), date(t3,t4)));

		while(SA.size() != 0 || SB.size() != 0)
		{
			if(SA.size()==0 || SB.size()==0)
			{
				if(SA.size()==0)
					B += obsluz(SB, QB, QA);
				else
					A += obsluz(SA, QA, QB);
			}
			else
			{
				if(SA.top() < SB.top())
					A += obsluz(SA, QA, QB);
				else if(SB.top() < SA.top())
					B += obsluz(SB, QB, QA);
				else
				{
					if(QA.size() == 0 && QB.size() != 0)
							obsluz(SB, QB, QA);
					else
						obsluz(SA, QA, QB);
				}
			}
		}

		printf("Case #%d: %d %d\n", i, A, B);
	}
	return 0;
} 
// END CUT HERE
