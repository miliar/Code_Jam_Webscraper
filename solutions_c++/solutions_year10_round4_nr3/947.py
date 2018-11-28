#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define L(s) (int)(s).size()
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define fr(i,st,fn) for(int (i)=(st);(i)<=(fn);++(i))
#define VI vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define pii pair<int,int>
#define mp make_pair
//#define x first
//#define y second
int a[111][111];
int b[111][111];
int main()
{
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ts;
	cin>>ts;
	rp(t,ts)
	{
		memset(a,0,sizeof(a));
		cout<<"Case #"<<t+1<<": ";
		int n;
		cin>>n;
		rp(i,n)
		{
			int i1,j1,i2,j2;
			cin>>i1>>j1>>i2>>j2;
			for(int i=i1;i<=i2;++i)
				for(int j=j1;j<=j2;++j)
					a[i][j]=1;
		}
		bool ok=1;
		int cnt=0;
		do
		{
			memset(b,0,sizeof(b));
			++cnt;
			ok=0;
			for(int i=1;i<=100;++i)
				for(int j=1;j<=100;++j)
				if (a[i][j]==1)
				{
					if (a[i-1][j]==1||a[i][j-1]==1)
					{
						ok=1;
						b[i][j]=1;
					}
					else
						b[i][j]=0;
				}
				else
					if (a[i][j]==0&&a[i-1][j]==1&&a[i][j-1]==1)
					{
						ok=1;
						b[i][j]=1;
					}
			memcpy(a,b,sizeof(a));
					
		}while(ok);
		cout<<cnt<<endl;
	}
}
