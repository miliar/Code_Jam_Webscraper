#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
const int N = 15;
const double eps = 1e-8;
char g[N][N];
double v[N][N];
int min(int a,int b)
{
	return a<b?a:b;
}
int main()
{
	//freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int T,res,ca=1,k,h,l,i,j,m,n,d;
    double mx,my,tx,ty;
    scanf("%d",&T);
    while(T--)
    {
    	scanf("%d%d%d",&m,&n,&d);
    	for(i=0;i<m;i++)
    	{
    		scanf("%s",g[i]);
    	}
    	for(i=0;i<m;i++)
    		for(j=0;j<n;j++)v[i][j]=g[i][j]-'0'+d;
    	res=-1;
    	for(k=min(m,n);res==-1&&k>=3;k--)
    	{
    		for(i=0;res==-1&&i+k<=m;i++)
    			for(j=0;res==-1&&j+k<=n;j++)
    			{
    				mx=(double)(k-1)/2.0+i;
    				my=(double)(k-1)/2.0+j;
    				tx=ty=0;
    				for(h=0;h<k;h++)
    				{
    					for(l=0;l<k;l++)
    					{
    						if((h==0&&l==0)||(h==0&&l==k-1)||(h==k-1&&l==0)||(h==k-1&&l==k-1))continue;
    						tx+=v[i+h][j+l]*(mx-i-h);
    						ty+=v[i+h][j+l]*(my-j-l);
    					}
    				}
    				if(tx<eps&&tx>-eps&&ty<eps&&ty>-eps){res=k;break;}
    			}
    	}
    	printf("Case #%d: ",ca++);
    	if(res==-1)puts("IMPOSSIBLE");
    	else printf("%d\n",res);
    }	
    return 0;
}
