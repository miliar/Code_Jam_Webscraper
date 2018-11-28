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
using namespace std;
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
int f[555][555];
int c[555][555];
int n;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcount;
	scanf("%d",&testcount);
	memset(f,0,sizeof(f));
	memset(c,0,sizeof(c));
	c[0][0]=1;
	c[1][0]=1;
	c[1][1]=1;
	for(int i=2;i<=500;++i)
	{
		c[i][0]=c[i][i]=1;
		for(int j=1;j<i;++j)
			c[i][j]=(c[i-1][j]+c[i-1][j-1])%100003;
	}
	f[2][1]=1;
	f[3][1]=1;
	f[3][2]=1;
	for(int i=4;i<=500;++i)
	{
		f[i][1]=1;
		f[i][2]=1;
		for(int j=3;j<i;++j)
		{
			f[i][j]=(c[j-2][j-2]+c[i-j-1][j-2])%100003;
			for(int k=1;k<j-2;++k)
				f[i][j]=(f[i][j]+(ll)f[j][k+1]*c[i-j-1][j-2-k])%100003LL;
		}
	}
	for(int testnum=1;testnum<=testcount;++testnum)
	{
		scanf("%d",&n);
		int rez=0;
		for(int i=1;i<n;++i)
			rez=(rez+f[n][i])%100003;
		printf("Case #%d: %d\n",testnum,rez);
	}
}