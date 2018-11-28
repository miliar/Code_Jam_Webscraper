#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include <queue>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("b.in");
ofstream fout("b.out");

int T;
int N,S,p;

int high[32];
int sHigh[32];

void compute()
{
	

	for(int i=0;i<=30;i++)
	{
		if(i%3)
		{
			sHigh[i] = high[i] = (i/3) + 1;
		}
		else
			sHigh[i] = high[i] = i/3;
	}
	
	sHigh[2] = 2;
	sHigh[3] = 2;
	for(int i=3;i<=30;i++)
	{
		sHigh[i] = (i-2)/3 + 2;
	}

}
int main()
{
	
	fin>>T;
	compute();
	
	for(int c=1;c<=T;c++)
	{
		fin>>N>>S>>p;
		int res = 0;
		for(int i=0;i<N;i++)
		{
			int n;
			fin>>n;
			if(high[n]>=p)
				res++;
			else if(sHigh[n]>=p && S>0)
			{
				res++;
				S--;
			}
		}

	
		cout<<"Case #"<<c<<": "<<res<<endl;
		fout<<"Case #"<<c<<": "<<res<<endl;
		
	}
	return 0;
}
