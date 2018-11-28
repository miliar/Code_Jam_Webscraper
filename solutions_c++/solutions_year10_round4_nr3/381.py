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

int aa[110][110];
int n=101;
bool check()
{
	int i;
	int j;
	REP(i,1,n)
	{
		REP(j,1,n)
		{
			if(aa[i][j]==1)
				return 0;
		}
	}
	return 1;
	
}

void main()
{
	fin.open("b.in",ios::in);
	fout.open("z.in",ios::out);
	int cases,con,i,j,k,sum;

	int a,b,c,d;
	int r;
	
	
	int bb[110][110];

	fin>>cases;
	rep(con,cases)
	{
		//cout<<"Now in test case "<<con+1<<endl;
		fin>>r;
		clr(aa,0);clr(bb,0);
		rep(k,r)
		{
			fin>>a>>b>>c>>d;
			for(i=a;i<=c;i++)
				for(j=b;j<=d;j++)
					aa[j][i]=1;
		}
		//REP(i,1,7)
		//{
		//	REP(j,1,7)
				//cout<<aa[i][j];
			//KH
		//}
		sum=0;
		while(check()!=1)
		{
			sum++;
			REP(i,1,n)
			{
				REP(j,1,n)
				{
					if(aa[i][j]==1)
					{
						if(aa[i-1][j]==0&&aa[i][j-1]==0)
							bb[i][j]=0;
						else
							bb[i][j]=1;
					}
					else
					{
						if(aa[i-1][j]==1&&aa[i][j-1]==1)
							bb[i][j]=1;
						else
							bb[i][j]=0;
					}
				}
			}
			REP(i,1,n)
			{
				REP(j,1,n)
				{
					aa[i][j]=bb[i][j];
				}
			}
		}
		
		fout<<"Case #"<<con+1<<": "<<sum<<endl;

	}
	return;
}
