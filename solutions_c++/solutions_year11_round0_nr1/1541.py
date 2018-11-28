#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <limits>

using namespace std;
#define clr(x,a) memset((x), a, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define REPD(i,a,b) for(i=a-1;i>=b;i--)
#define repd(i,n) REPD(i,n,0)
#define KG <<"	"<<
#define KG2 <<"	"
#define KH cout<<endl;
#define INF 2147483647
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}

typedef long double ld;
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;
typedef signed   long long i64;
typedef unsigned long long u64;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

ifstream fin;
ofstream fout;

void main()
{
	fin.open("A-large.in",ios::in);
	fout.open("A-large.out",ios::out);
	int cases,con,i,j,k,sum;
	int n;
	char c;
	int po;
	int pb;
	int nexto;
	int nextb;

	queue<int> o;
	queue<int> b;
	queue<char> all;

	fin>>cases;
	rep(con,cases)
	{
		cout<<"Now in test case "<<con+1<<endl;
		while(!o.empty())
			o.pop();
		while(!b.empty())
			b.pop();
		while(!all.empty())
			all.pop();
		po = 1;
		pb = 1;
		sum = 0;

		fin >> n;
		rep(i, n)
		{
			fin>>c;
			if(c == 'O')
			{
				fin>>j;
				o.push(j);
			}
			if(c == 'B')
			{
				fin>>j;
				b.push(j);
			}
			all.push(c);
		}
		while(!all.empty())
		{
			c = all.front(); all.pop();
			if(!o.empty())
				nexto = o.front();
			if(!b.empty())
				nextb = b.front();
			if(c == 'O')
			{		
				o.pop();		
				sum+= abs(nexto-po) + 1;
				if(nextb > pb)
				{
					pb += abs(nexto-po) + 1;
					if(pb > nextb)
						pb = nextb;
				}
				else if(nextb < pb)
				{
					pb -= abs(nexto-po) + 1;
					if(pb < nextb)
						pb = nextb;
				}
				else ;
				po = nexto;
			}
			else
			{
				b.pop();
				sum+= abs(nextb-pb) + 1;
				if(nexto > po)
				{
					po += abs(nextb-pb) + 1;
					if(po > nexto)
						po = nexto;
				}
				else if(nexto < po)
				{
					po -= abs(nextb-pb) + 1;
					if(po < nexto)
						po = nexto;
				}
				else ;
				pb = nextb;
			}
			
		}

		fout<<"Case #"<<con+1<<": "<<sum<<endl;

	}
	char theFix;
	cin >> theFix;
	return;
}
