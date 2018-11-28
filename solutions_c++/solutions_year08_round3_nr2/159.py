#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <fstream>
#include <utility>
#include <sstream>
#include <cstring>

#define AS(arr)  (sizeof(arr)/sizeof(arr[0]))
#define ALL(c) (c).begin(),(c).end() 
#define SIZE(a) int((a).size())
#define EACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define REP(I, T) for(int I=0;(I)<(T);++I)

using namespace std;

/*
2,3,5,7�Ŋ���鐔�͉���
14,-14 �c����
13�cOK
0�c����

�Ԃ�+��-������
3^(n-1)��̐����o���邪�A
�i�ꏊ��+,-,�����̂ǂꂩ
����������
0�Ŏn�܂��Ă��ǂ�

*/


struct Stat
{
	string lvalue;
	char prevSign;
	long long total;
	int pos;

	Stat(string &l, char p, long long t, int po) : lvalue(l), prevSign(p), total(t), pos(po)
	{

	}

	void calc()
	{
		long long v = _atoi64(lvalue.c_str());
		if(prevSign == '+')
		{
			total += v;
		}
		else if(prevSign == '-')
		{
			total -= v;
		}
	}

	bool checkResult()
	{
		if(total % 2 == 0 || total %3 == 0 || total % 5 == 0 || total % 7 == 0)
		{
			return true;
		}
		else
		{
			return false;
		}

	}
	
};

string in;
int size;
long long all = 0;

std::vector<Stat*> allStats;




void count(Stat &s)
{
	if(s.pos == size)
	{
		s.calc();
		if(s.checkResult())
		{
			all++;
		}

	}

	else
	{
		
		{
		Stat *sp = new Stat(s);
		allStats.push_back(sp);
		sp->calc();
		sp->prevSign = '+';
		sp->lvalue = in[s.pos];
		sp->pos++;
		count(*sp);
		}

		//minus
		//�v�Z
		{
		Stat *sm = new Stat(s);
		allStats.push_back(sm);
		sm->calc();
		sm->prevSign = '-';
		sm->lvalue = in[s.pos];
		sm->pos++;
		count(*sm);
		}

		//none
		{
		Stat *sn = new Stat(s);
		allStats.push_back(sn);
		sn->lvalue += in[s.pos];
		sn->pos++;
		count(*sn);
		}

	}
	


}

int main()
{
	int testcases;
	cin >> testcases;

	REP(testcase, testcases)
	{
		int ret = 0;
		all = 0;
		cin >> in;
		size = in.length();

		
		string lvalue;
		char prevSign = '+';
		lvalue.reserve(64);
		lvalue.push_back(in[0]);

		Stat stat(lvalue, '+', 0, 1);
		count(stat);

		REP(i, allStats.size())
		{
			delete allStats[i];
		}
		allStats.clear();
		
		cout << "Case #" << testcase+1 << ": " << all << endl;
		fflush(NULL);
		
	}
	

	return 0;
}


