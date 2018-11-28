#define _CRT_SECURE_NO_DEPRECATE
//
//
//
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <set>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

const double zero=1e-6;
const double limit=1e8;
#define SZ(x) (int(x.size()))
typedef long long int64;
typedef unsigned long long uint64;
template<class T> T sqr(T x) {return x*x;}
template<class T> T gcd(T a,T b){ if(a<0) return gcd(-a,b);if(b<0) return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(T a,T b){ return a*(b/gcd(a,b));}
int64 toInt64(string s){ istringstream sin(s); int64 t; sin>>t;return t;}
int toInt(string s){ istringstream sin(s); int t; sin>>t; return t;}
template<class T> string toString(T x){ ostringstream sout; sout<<x; return sout.str();}


#define IFF_GUYING
#ifdef IFF_GUYING
	ifstream inf("in.txt");
#define cin inf
#endif


char m[50][50];
int main(int argc, char* argv[])
{

	int T;
	cin>>T;
	for(int t=1; t<= T;t++)
	{
		int n,k;
		cin>>n>>k;
		memset(m,0,sizeof(m));
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				cin>>m[j][n-i-1];

		for(int i=0;i<n;i++)
		{
			int next = n-1;
			for(int j=n-1;j>=0;j--)
			{
				while(next>=0)
				{
					if(m[next][i]!='.')
						break;
					next--;
				}
				if(next>=0)
				{
					char c = m[next][i];
					m[next][i] = '.';
					m[j][i] = c;
					next--;
				}
				else
					break;
			}
		}
		int can[128]={0};
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(m[i][j] == '.')
					continue;
				if(can[m[i][j]])
					continue;
				// об
				int dw = 0;
				for(int l=i;l<l+k;l++)
				{
					if(l<n && m[l][j] == m[i][j])
						dw++;
					else
						break;
				}
				if(dw==k)
				{
						can[m[i][j]] = 1;
				}
				// ср
				dw = 0;
				for(int l=j;l<j+k;l++)
				{
					if(l<n && m[i][l] == m[i][j] )
						dw ++;
					else
						break;
				}
				if(dw==k)
				{
						can[m[i][j]] = 1;
				}
				// сроб
				dw = 0;
				for(int l=0;l<k;l++)
				{
					if(i+l<n && j+l<n && m[i+l][j+l] == m[i][j])
						dw++;
					else
						break;
				}
				if(dw==k)
				{
						can[m[i][j]] = 1;
				}
				// срио
				dw = 0;
				for(int l=0;l<k;l++)
				{
					if(i-l>=0 && j+l<n && m[i-l][j+l] == m[i][j])
						dw++;
					else
						break;
				}
				if(dw==k)
				{
						can[m[i][j]] =1;
				}
			}
		}

		cout<<"Case #"<<t<<": ";
		int r='R';
		int b='B';
		if(can[r] && can[b])
			cout<<"Both"<<endl;
		else if(can[r])
			cout<<"Red"<<endl;
		else if(can[b])
			cout<<"Blue"<<endl;
		else
			cout<<"Neither"<<endl;
	}
}
