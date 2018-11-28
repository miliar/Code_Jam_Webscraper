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

int C;

long long D;
struct P
{
	int n;
	long long pos;
};

P p[250];

bool check(long long t)
{
	long long preLeft = -100000000000000LL;
	for(int i=0;i<C;i++)
	{
		long long leftP = p[i].pos - t;
		long long rightP = p[i].pos +t;
		leftP = max(leftP,preLeft);
		long long xRightP = leftP + D * (p[i].n-1);
		if(rightP < xRightP)
			return false;
		preLeft = xRightP + D;
	}
	return true;
}
int main()
{
	fin>>T;
	for(int c=0;c<T;c++)
	{
		fin>>C>>D;
		D = D*2;
		for(int i=0;i<C;i++)
		{
			fin>>p[i].pos>>p[i].n;
			p[i].pos *= 2;

		}
		for(int i=0;i<C;i++)
		{
			for(int j=i+1;j<C;j++)
			{
				if(p[i].pos>p[j].pos)
				{
					long long tmp = p[j].pos;
					p[j].pos = p[i].pos;
					p[i].pos = tmp;
					int tt = p[j].n;
					p[j].n = p[i].n;
					p[i].n = tt;
				}
			}
		}
		long long left = 0;
		long long right = 100000000000000LL;
		long long res;
		while(right>left)
		{
			res = (left+right)/2;
			bool good = check(res);
			if(good)
				right = res;
			else
				left = res+1;
		}	
		
		cout<<"Case #"<<c+1<<": "<<left/2;
		if(left%2)
			cout<<".5"<<endl;
		else
			cout<<".0"<<endl;

		fout<<"Case #"<<c+1<<": "<<left/2;
		if(left%2)
			fout<<".5"<<endl;
		else
			fout<<".0"<<endl;
	
	}
	return 0;
}
