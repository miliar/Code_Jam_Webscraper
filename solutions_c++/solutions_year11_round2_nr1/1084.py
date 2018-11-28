#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int main()
{
	int t;
	int k = 0;
	s(t);
	while(t--)
	{
		k++;
		int n; s(n);
		int i, j;
		int graph[110][110];
		int w[110], t[110]; 
		long double wp[110];
		rep(i,n)
		{
			w[i] = 0; t[i] = 0;
			string p; cin>>p;
			rep(j,p.sz)
			{
				if(p[j]=='0') {graph[i][j]=0;t[i]++;}
				if(p[j]=='1') {graph[i][j]=1;w[i]++;t[i]++;}
				if(p[j]=='.') graph[i][j]=-1;
			}
			wp[i]=w[i]*1.0/t[i];
		}
		cout << "Case #"<<k<<":" << endl;
		
		long double owp[110];
		rep(i,n)
		{
			owp[i] = 0;
			rep(j,n)
				if(graph[i][j]==0||graph[i][j]==1)
				{ 
					if(graph[i][j])
						owp[i]+=(w[j])*1.0/(t[j]-1);
					else
						owp[i]+=(w[j]-1)*1.0/(t[j]-1);
				}
			owp[i]/=t[i]; 
		}
		
		rep(i,n)
		{
			long double _wp = wp[i];
			long double _oowp = 0, _owp = owp[i];
			rep(j,n)
				if(graph[i][j]==0||graph[i][j]==1)
				{ 
					_oowp += owp[j];
				} 
			
			_oowp/=t[i];
			//cout << _wp << " " <<_oowp << " " << _owp << endl;
			long double rpi = 0.0;
			rpi = (0.25 * _wp) + (0.50 * _owp) + (0.25 * _oowp);
			printf("%.9Lf\n",rpi);
		}
		
	}
}
