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
	fin.open("C-large.in",ios::in);
	fout.open("C-large.out",ios::out);
	int cases,con,i,j,k,sum;
	int n;
	int min;
	int result;

	fin>>cases;
	rep(con,cases)
	{
		cout<<"Now in test case "<<con+1<<endl;
		sum = 0;
		min = 10000000;
		result = 0;

		fin >>n;
		rep(i,n)
		{
			fin >> j;
			result = result ^ j;
			sum += j;
			if(j < min)
				min = j;
		}

		if(result != 0)
			fout<<"Case #"<<con+1<<": NO"<<endl;
		else
			fout<<"Case #"<<con+1<<": "<<sum-min<<endl;

	}
	char theFix;
	cin>>theFix;
	return;
}
