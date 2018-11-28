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

int ff[1001][1001];
int cc[1001];
int aa[1001];
__int64 l,t,n,c,sum;


int find(int i, int l)
{
	int r1,r2;
	if(i == (n-1))
	{
		if(l >0)
			return aa[i];
		else
			return 2*aa[i];
	}
	r1 = find(i+1,l) + 2*aa[i];
	if(l == 0)
		return r1;	
	r2 = find(i+1,l-1) + aa[i];
	if(r1 < r2)
		return r1;
	else
		return r2;
}

void main()
{
	fin.open("B-small-attempt0.in",ios::in);
	fout.open("a.out",ios::out);
	int cases,con,i,j,k;



	fin>>cases;
	rep(con,cases)
	{
		cout<<"Now in test case "<<con+1<<endl;
		clr(ff,0);clr(aa,0);clr(cc,0);
		fin>>l>>t>>n>>c;
		rep(i,c)
			fin>>cc[i];
		j=0;
		rep(i,n)
		{
			aa[i]=cc[j];
			j = (j+1)%c;
		}
		//rep(i,n)
			//cout<<aa[i]<<endl;
		sum = 0;
		rep(i,n)
		{
			sum+=2*aa[i];
			if(sum > t)
			{
				int r1 = find(i+1, l) + sum;
				if(l==0)
				{
					sum = r1;
					break;
				}
				int r2 = find(i+1, l-1) + sum - (sum - t)/2;
				if(r1 < r2)
					sum = r1;
				else
					sum = r2;
				break;
			}
		}

		//cout<<sum<<endl;
		fout<<"Case #"<<con+1<<": "<<sum<<endl;

	}
	char theFix;
	cin>>theFix;
	return;
}
