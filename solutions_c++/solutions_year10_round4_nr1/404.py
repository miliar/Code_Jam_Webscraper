#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

typedef long long LL;

#define VI vector<int>
#define VS vector<string>
#define SZ(x) ((int)(x).size())
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define MS(a,b) memset((a),b,sizeof(a))
#define EC(tp,it,a) for(tp::iterator it=(a).begin();it!=(a).end();++it)
#define SE(x) cout<<#x<<" = "<<x<<endl
#define PB push_back

template<class T> void inc(T& a, const T& b)
{
	if (a < b) a = b;
}
template<class T> void dec(T& a, const T& b)
{
	if (a > b) a = b;
}

const int N=52*3;

int n;
int a[N][N];
int rez;

inline int size(int i,int p)
{
	return (p-i+1);
}

bool check(int r1,int c1,int r2,int c2)
{
//	printf("check(%d %d, %d,%d)\n",r1,c1,r2,c2);
	int sz = size(r1,r2);
	
	for(int i=r1;i<=r2;++i)
		for(int j=c1;j<=c2;++j)
			if(i<n+n || i>=n+n+n || j<n+n || j>=n+n+n) a[i][j]=-1;
	
	for(int i=r1;i<=r2;++i)
		for(int j=c1;j<=c2;++j)
		{
//			if(r1==1 && c1==2 && r2==3 && c2==4) printf("%d %d\n",i,j);
			int r=j-c1+r1,c=i-r1+c1;
//			if(r1==1 && c1==2 && r2==3 && c2==4)printf("%d %d\n",r,c);
			if(a[i][j]!=a[r][c])
			{
				if(a[i][j]==-1)a[i][j]=a[r][c];
				else if(a[r][c]==-1)a[r][c]=a[i][j];
				else return false;
			}
			
			r=sz-1-(j-c1)+r1,c=sz-1-(i-r1)+c1;
//			if(r1==1 && c1==2 && r2==3 && c2==4)printf("%d %d\n\n",r,c);
			if(a[i][j]!=a[r][c])
			{
				if(a[i][j]==-1)a[i][j]=a[r][c];
				else if(a[r][c]==-1)a[r][c]=a[i][j];
				else return false;
			}
			
			r=j-c1+r1,c=i-r1+c1;
			if(a[i][j]!=a[r][c])
			{
				if(a[i][j]==-1)a[i][j]=a[r][c];
				else if(a[r][c]==-1)a[r][c]=a[i][j];
				else return false;
			}
		}
	
		
	return true;
}

int run()
{
	
	rez=9999;
	
	if(check(n+n,n+n,n+n+n-1,n+n+n-1))return 0;
	
	for(int i=0;i<=n+n;++i)
	{
		for(int j=0;j<=n+n;++j)
		{
			for(int s=0;;++s)
			{
				int p=i+s;
				int q=j+s;
				
				if(p>=n+n+n+n+n)break;
				if(q>=n+n+n+n+n)break;
				
				if(p<n+n+n-1)continue;
				if(q<n+n+n-1)continue;
				
				if(size(i,p)>rez)continue;
				if(check(i,j,p,q))
				{
					rez=min(rez,size(i,p));
//					printf("rez=%d\n",rez);
				}
			}
		}
	}
	return rez*rez-n*n;
}

int main()
{
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	
	int ts;
	scanf("%d",&ts);
	FR(cas,0,ts)
	{
		scanf("%d",&n);
		int r=0,c=0,tr=1,tc=1;
		int tot=n*n;
//		SE(n);
//		SE(tot);
		FR(i,0,tot)
		{
			scanf("%d",&a[r+n+n][c+n+n]);
			--r;
			++c;
			if(c>=n)
			{
				r=n-1;
				c=tc++;
			}
			else if(r<0)
			{
				r=tr++;
				c=0;
			}
		}
/*
		FR(i,0,n){FR(j,0,n)
			printf("%d ",a[i+n][j+n]);
			putchar(10);
		}
*/
		printf("Case #%d: %d\n",cas+1,run());
	}
	
	return 0;
}
