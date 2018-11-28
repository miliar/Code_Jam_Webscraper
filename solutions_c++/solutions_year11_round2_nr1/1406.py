#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <utility>

using namespace std;

#define SIZE(X) ((int)X.size())
#define LENGTH(X) ((int)X.length())
#define MP(A,B) make_pair(A,B)
//typedef long long int64;
//typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) ((S&two(X))>0)
#define containL(S,X) ((S&twoL(X))>0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> void checkmin(T &a,T b){if (b<a) a=b;}
template<class T> void checkmax(T &a,T b){if (b>a) a=b;}
template<class T> T sqr(T x) {return x*x;}
int countbit(int n) {return (n==0)?0:(1+countbit(n&(n-1)));}
int lowbit(int n) {return (n^(n-1))&n;}
typedef pair<int,int> ipair;
template <class T> void out(T A[],int n){for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> void out(vector<T> A,int n=-1){if(n==-1) n=A.size(); for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> gcd(T a,T b){ if (a<0) return gac(-a,b); if(b<0) return gac(a,-b); return (b==0)?a:gcd(b,a%b);}
template <class T> lcm(T a,T b){ return a*(b/gcd(a,b));}
//int64 toInt64(string s){ istringstream sin(s); int64 t; sin>>t; return t;}
int toInt(string s){ istringstream sin(s); int t; sin>>t; return t;}
//string toString(int64 v){ ostringstream sout; sout<<v; return sout.str();}
string toString(int v){ ostringstream sout; sout<<v; return sout.str();}


void RPI()
{
	int n, i, j, k;
	char map[110][110];
	double wp[110], wp2[110][110], owp[110], oowp[110];

	memset(map, 0, sizeof(map));
	memset(wp, 0, sizeof(wp));
	memset(wp2, 0, sizeof(wp2));

	scanf("%d", &n);

	for(i=0; i<n; i++) scanf("%s", map[i]);

	for(i=0; i<n; i++)
	{
		int w=0, num=0;
		for(j=0; j<n; j++)
		{
			if(map[i][j]=='1' || map[i][j]=='0')
			{
				num++; if(map[i][j]=='1') w++;
			}
		}
		wp[i] = w*1.0/num;
	}

	for(i=0; i<n; i++)
	{
		vector<double> vec;
		for(j=0; j<n; j++)
		{
			if(map[i][j]=='1' || map[i][j]=='0')
			{				
				//calulate wp[j]'
				int w=0, num=0;
				for(k=0; k<n; k++)
				{
					if(k!=i)
					{
						if(map[j][k]=='1' || map[j][k]=='0')
						{
							num++; if(map[j][k]=='1') w++;
						}
					}
				}
				vec.push_back(w*1.0/num);
			}
		}
		double d = 0;
		for(j=0; j<vec.size(); j++)
			d += vec[j];
		owp[i] = d / vec.size();
	}

	for(i=0; i<n; i++)
	{
		int count=0;
		double d=0;
		for(j=0; j<n; j++)
		{
			if(map[i][j]=='1' || map[i][j]=='0')
			{
				d+=owp[j]; count++;
			}
		}
		oowp[i] = d*1.0/count;
	}

	for(i=0; i<n; i++)
	{
		printf("%.8lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}

}


int main()
{
	freopen("1.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t, x;
	
	scanf("%d", &t);

	for(x=1; x<=t; x++)
	{
		printf("Case #%d:\n", x);
		RPI();
	}
	return 0;
}
