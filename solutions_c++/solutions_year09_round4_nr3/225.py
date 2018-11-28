// gcjr2c2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)
#define MAXN 310
const int M = 33;
int n,m;
struct node 
{
	int a[M];
	bool operator<(const node &other)const
	{
		return a[0]>other.a[0];
	}
}d[MAXN];
bool check(int x,int y)
{
	for(int i = 0; i < m; i++) 
		if(d[x].a[i] <= d[y].a[i]) 
			return 0;
	return 1;
}





int mm[MAXN][MAXN];
int match1[MAXN];
int match2[MAXN];




int hungary(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
				return ret;
}




int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t1,i,j,k,res;
	scanf("%d",&t);
	t1=1;
	while(t--)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
				scanf("%d",&d[i].a[j]);
		}
			sort(d,d+n);
			memset(mm,0,sizeof(mm));
			for(i=0;i<n;i++)
			{
				for(j=0;j<n;j++)
				{
					if(check(i,j)) mm[i][j] = 1;
				}
			}
          res=hungary(n,n,mm,match1,match2);
		  printf("Case #%d: %d\n",t1++, n - res);
	}
}


