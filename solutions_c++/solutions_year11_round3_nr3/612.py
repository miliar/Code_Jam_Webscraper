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
int n,l,h;

int a[100000];

void swap(int & a, int & b){
     int c = a;
        a = b;
        b = c;
}

int gcd(int a,int b){
     if(0 == a ){
         return b;
      }
     if( 0 == b){
         return a;
      }
     if(a > b){
          swap(a,b);
      }
     int c;
     for(c = a % b ; c > 0 ; c = a % b){
            a = b;
            b = c;
      }
     return b;
}


void main()
{
	fin.open("C-small-attempt0.in",ios::in);
	fout.open("a.out",ios::out);
	int cases,con,i,j,k,sum;



	fin>>cases;
	rep(con,cases)
	{
		cout<<"Now in test case "<<con+1<<endl;
		fin >>n>>l>>h;
		clr(a,0);
		rep(i,n)
			fin>>a[i];
		for(i=l;i<=h;i++)
		{
			int flag=1;
			rep(j,n)
			{
				int g = gcd(i,a[j]);
				if(!(g==i||g==a[j]))
				{
					flag = 0;break;
				}
			}
			if(flag == 1)
				goto succ;
		}

		fout<<"Case #"<<con+1<<": NO"<<endl;
		goto endd;
succ:
		fout<<"Case #"<<con+1<<": "<<i<<endl;
		goto endd;
endd:;


	}
	char theFix;
	cin>>theFix;
	return;
}
