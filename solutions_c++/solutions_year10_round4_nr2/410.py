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
	fin.open("b.in",ios::in);
	fout.open("z.in",ios::out);
	int cases,con,i,j,k,sum;

	int p;
	int pp[15];
	int m[1500];
	int cost[20][1500];
	int ppp;
	int c[11][600][11];
	int temp1;
	int temp2;


	fin>>cases;
	rep(con,cases)
	{
		//cout<<"Now in test case "<<con+1<<endl;
		fin>>p;
		ppp=1;
		clr(m,0);
		clr(cost,0);
		clr(pp,0);
		clr(c,0);
		rep(i,p+1)
		{
			pp[i]=1;
		}
		for(i=1;i<=p;i++)
		{
			ppp=ppp*2;
			pp[i]=ppp;
		}
		
		rep(i,ppp)
			fin>>m[i];
		for(i=1;i<=p;i++)
			for(j=1;j<=pp[p-i];j++)
				fin>>cost[i][j];
		//for(i=1;i<=p;i++)
		//{
		//	for(j=1;j<=pp[p-i];j++)
		//		cout<<cost[i][j];
		//	KH
		//}
		for(i=1;i<=p;i++)
		{
			for(j=1;j<=pp[p-i];j++)
			{
				for(k=0;k<=p-i;k++)
				{
					c[i][j][k]=1000000000;
				}
			}
		}
		//rep(i,ppp)
			//cout<<m[i];

		for(i=1;i<=1;i++)
		{
			for(j=1;j<=pp[p-i];j++)
			{
				for(k=0;k<=p-i;k++)
				{
					if(m[2*j-2]<p-k-1||m[2*j-1]<p-k-1)
						c[i][j][k]=1000000000;
					else if(m[2*j-2]==p-k-1||m[2*j-1]==p-k-1)
						c[i][j][k]=cost[i][j];
					else
						c[i][j][k]=0;
				}
			}
		}

		for(i=2;i<=p;i++)
		{
			for(j=1;j<=pp[p-i];j++)
			{
				for(k=0;k<=p-i;k++)
				{
					temp1=c[i-1][2*j-1][k]+c[i-1][2*j][k];
					if(temp1>=1000000000)
						temp1=1000000000;
					temp2=cost[i][j]+c[i-1][2*j-1][k+1]+c[i-1][2*j][k+1];
					if(temp2>=1000000000)
						temp2=1000000000;
					c[i][j][k]=min(temp1,temp2);
				}
			}
		}
		
		fout<<"Case #"<<con+1<<": "<<c[p][1][0]<<endl;

	}
	return;
}
