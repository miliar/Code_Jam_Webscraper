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
int N, S, p;
int t[101];

int solve()
{
	int res = 0;
	int sc = 0;
	int sb = 0;

	for(int i = 0;i < N;++i)
	{
		switch(t[i] % 3)
		{
		case 0:
			if(t[i] == 0 || t[i] == 30)
			{
				if(t[i] / 3 >= p)
					++res;
			}
			else
			{
				if(t[i] / 3 >= p)
				{
					res++;
					sb++;
				}
				else
				{
					if(t[i] / 3 + 1 >= p && sc < S)
					{
						res++;
						sc++;
					}
					else
					{
						sb++;
					}
				}
			}
			break;
		case 1:
			if(t[i] == 1)
			{
				if(t[i] / 3 + 1 >= p)
					++res;
			}
			else
			{
				++sb;
				if(t[i] / 3 + 1 >= p)
				{
					++res;
				}
			}
			break;
		case 2:
			if(t[i] == 29)
			{
				if(t[i] / 3 + 1 >= p)
					++res;
			}
			else
			{
				if(t[i] / 3 + 1 >= p)
				{
					++res;
					++sb;
				}
				else
				{
					if(t[i] / 3 + 2 >= p && sc < S)
					{
						++res;
						++sc;
					}
					else
					{
						++sb;
					}
				}
			}
			break;
		default:
			break;
		}
	}
	if(sc+sb >= S)
		return res;
	else
		return 0;
}

int main()
{
	ofstream fout;
	fout.open("output.txt");
	in >> T;

	for(int i = 0;i < T;++i)
	{
		in >> N >> S >> p;
		for(int j = 0;j < N;++j)
		{
			in >> t[j];
		}

		fout << "Case #" << i+1 << ": " << solve() << endl;
	}
	fout.close();
	return 0;
}