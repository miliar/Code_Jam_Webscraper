#include <iostream>
#include <stdio.h>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define ff(i,x,y) for(int i = (x);i < (y);++i)
#define rep(i,n) ff(i,0,n)
#define st(v) sort(v.begin(),v.end())
#define st2(v,f) sort(v.begin(),v.end(),f)
#define rvs(v) reverse(v.begin(),v.end())
#define cnt(v,n) count(v.begin(),v.end(),n)
#define pb push_back
bool myfunction (int i,int j) { return (i<j); }
#define fact(x) for(i=x-1;i>0;i--){x=x*i;}
#define F first
#define S second
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VVI vector<VI>

#define LOCAL 1
#ifdef LOCAL
ifstream in("in.txt");
#else
in = &cin;
#endif

int T;
int A, B;

int powInt(int num, int exp)
{
	int res = 1;
	for(int i = 0;i < exp;++i)
		res *= num;
	return res;
}

int solve()
{
	int res = 0;
	int dig = 0;
	int tnum = A;
	while(tnum)
	{
		dig++;
		tnum /= 10;
	}
	for(int num = A;num <= B;++num)
	{
		for(int d = 1;d < dig;++d)
		{
			int low = num / powInt(10,d);
			int upp = num % powInt(10,d) * powInt(10,dig-d);
			int m = low + upp;
			if(m > num && m <= B)
			{
				++res;
				//cout << res << ": " << num << " " << m << endl;
			}
		}
	}

	return res;
}
int main()
{
	ofstream fout;
	fout.open("output.txt");
	in >> T;

	for(int i = 0;i < T;++i)
	{
		in >> A >> B;
		fout << "Case #" << i+1 << ": " << solve() << endl;
	}
	return 0;
	fout.close();
}