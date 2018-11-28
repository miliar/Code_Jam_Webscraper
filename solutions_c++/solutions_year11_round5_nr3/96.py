#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <set>
#include <sstream>
#include <map>
#include <ctime>
#include <cstdlib>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define oo 1000111222
using namespace std;
typedef long long ll;
const int dx[]={-1,1,0,0,-1,1,-1,1};
      int dy[]={0,0,-1,1,1,-1,-1,1};
      
int m,n,b[111][111],re,d[111][111],deg[111][111];
string a[111];

void go(int x,int y)
{
	int t,xx,yy;
	d[x][y]=1;
	if (a[x][y]=='|') t=0;
	if (a[x][y]=='-') t=2;
	if (a[x][y]=='/') t=4;
	if (int(a[x][y])==92) t=6;
	t+=b[x][y];
	xx=x+dx[t]; yy=y+dy[t];
	if (xx<0) xx+=m;
	if (xx>=m) xx-=m;
	if (yy<0) yy+=n;
	if (yy>=n) yy-=n;
	deg[xx][yy]++;
	if (!d[xx][yy]) go(xx,yy);
}

void work()
{
	int i,j;
	fr(i,0,m-1) fr(j,0,n-1) d[i][j]=deg[i][j]=0;
	fr(i,0,m-1)
		fr(j,0,n-1)
			if (!d[i][j]) go(i,j);
	fr(i,0,m-1)
		fr(j,0,n-1)
			if (deg[i][j]>1) return;
	re++;
}

void att(int x,int y)
{
	if (y==n)
	{
		if (x==m-1) work();
		else att(x+1,0);
		return;
	}
	att(x,y+1);
	b[x][y]=1;
	att(x,y+1);
	b[x][y]=0;
}

int main()
{
	freopen("csmall.in","r",stdin); freopen("csmall.out","w",stdout);
	int test,it,i;
	cin >> test;
	fr(it,1,test)
	{
		cout << "Case #" << it << ": ";
		cin >> m >> n;
		re=0;
		fr(i,0,m-1) cin >> a[i];
		att(0,0);
		cout << re << endl;
	}
   return 0;
}
