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


ifstream fin("c.in");
ofstream fout("c.out");

int T;

int A,B;

bool marked[10000002];

int base;
int myrotate(int t)
{
	return t/10 + (t%10)*base;
}
long long compute()
{
	if(B<10) return 0;
	memset(marked, false, sizeof(marked));
	long long r = 0;
	base = 10;
	while(A>=base)
	{
		base *=10;
	}
	base/=10;
	
	for(int i=A;i<=B;i++)
	{
		if(!marked[i])
		{
			int count = 0;
			int t = i;
			while( !marked[t])
			{
				marked[t] = true;

				if(t>=A && t<=B)
					count++;

				t = myrotate(t);

			}
			r += (long long)count*(count-1)/2;
		}
	}
	return r;

}

int main()
{
	
	fin>>T;
	for(int c=1;c<=T;c++)
	{	
		fin>>A>>B;

		long long res = compute();
		


		cout<<"Case #"<<c<<": "<<res<<endl;
		fout<<"Case #"<<c<<": "<<res<<endl;
		
	}
	return 0;
}
