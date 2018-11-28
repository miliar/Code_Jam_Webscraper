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

int n;
int aa[100][100];
int n1[100];
int n0[100];
double wp[100];
double owp[100];
double oowp[100];
double r[100];

void main()
{
	fin.open("A-large.in",ios::in);
	fout.open("a.out",ios::out);
	int cases,con,i,j,k,sum;
	char c;


	fin>>cases;
	rep(con,cases)
	{
		cout<<"Now in test case "<<con+1<<endl;
		fin>>n;
		clr(aa, 0);clr(n1, 0);clr(n0, 0);
		clr(owp, 0);
		clr(oowp, 0);
		clr(aa, 0);
		clr(r, 0);

		rep(i,n)
			rep(j,n)
		{
			fin>>c;
			if(c == '1')
				aa[i][j]=1;
			else if(c == '0')
				aa[i][j]=0;
			else
				aa[i][j]=2;
		}
		
		rep(i,n)
		{
			int num1 =0, num0=0;
			rep(j,n)
			{
				if(aa[i][j] == 1)
					num1++;
				else if(aa[i][j] == 0)
					num0++;
			}
			n1[i]=num1;
			n0[i]=num0;
			wp[i] = (double)(num1)/(double)(num1+num0);
			//cout<<wp[i]<<endl;
		}
		//KH;

		rep(j,n)
		{
			int num =0;
			double sum =0;
			rep(i,n)
			{
				if(aa[i][j] == 1)
				{
					sum+=(double)(n1[i]-1)/(double)(n1[i]+n0[i]-1);
					num++;
				}
				if(aa[i][j] == 0)
				{
					sum+=(double)(n1[i])/(double)(n1[i]+n0[i]-1);
					num++;
				}

			}
			owp[j] = ((double)1/(double)(num))*sum;
			//cout<<j KG owp[j]<<endl;
		}
		//KH;

		rep(j,n)
		{
			int num =0;
			double sum =0;
			rep(i,n)
			{
				if(aa[i][j] == 1)
				{
					//cout<<i KG owp[i]<<endl;
					sum+=owp[i];
					num++;
				}
				if(aa[i][j] == 0)
				{
					sum+=owp[i];
					num++;
				}

			}
			//cout<<num;
			//cout<<sum<<endl;
			oowp[j] = ((double)1/(double)(num))*sum;
			//cout<<oowp[j]<<endl;
		}

		rep(i,n)
		{
			r[i]= 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			//cout<<r[i]<<endl;
		}

		fout<<"Case #"<<con+1<<": "<<endl;
		rep(i,n)
		{
			fout<<r[i]<<endl;
		}

	}
	char theFix;
	cin>>theFix;
	return;
}
