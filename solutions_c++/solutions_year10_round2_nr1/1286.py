#include<stdio.h>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<set>
#include<stack>
#include<iostream>
#include<math.h>
#include<map>
#include<memory.h>
#include<algorithm>
using namespace std;
map<string,int> amap;
int tree[10001][10001];
int node,m,n,mapid;
void insert(int id,int *zz)
{
	if(*zz == -1)
	{
		//danger[id]=1;
		//puts("finish insert it");
		return;
	}
	if(tree[id][*zz]==-1)
	{
		//printf("insert tree[%d][%d] at %d\n",id,*zz,node);
		tree[id][*zz]=node++;
	}
	insert(tree[id][*zz],zz+1);
}
void nana()
{
	        char tmp[10001];
	        scanf("%s",tmp);
	    	int len=strlen(tmp);
	    	int j=1;
	    	char iris[10001];
			int irisid=0;
			int zz[101]; 
			int zzid=0;
			int py;
			while(j<=len)
	    	{
	    		if(tmp[j]=='/' || j==len)
				{
					iris[irisid++]='\0';
					if(amap[iris]==0)
					{
					    amap[iris]=mapid++;
					    py=mapid-1;
				   }
				    else py=amap[iris];
				    zz[zzid++]=py;//°Ñzz®”×÷Ò»‚€×Ö·û´®íÍæ 
					j++;
				    irisid=0;
				    memset(iris,0,sizeof(iris));
				}
	    		else 
	    		{
	    			iris[irisid]=tmp[j];
	 			    irisid++;
				    j++;
				}
			}
			zz[zzid++]=-1;
			insert(0,zz);
			return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.txt","w",stdout);
	int i,j,cas,t;
	cas=1;
	scanf("%d",&t);
	while(t--)
	{
		memset(tree,-1,sizeof(tree));
		node=1;
		amap.clear();	    
	    scanf("%d %d",&n,&m);
	    mapid=1;
	    for(i=0;i<n;i++)
	    {
	    	nana();
		}
		int cnt1=node;
		for(i=0;i<m;i++)
	    {
	    	nana();
		}
		int cnt2=node;
		//printf("cnt1==%d  cnt2==%d\n",cnt1,cnt2);
		printf("Case #%d: %d\n",cas++,cnt2-cnt1);    	
	}
	return 0;
}
/*
9
5 5
/rogc
/ujb
/2y0l
/cyk4
/zed5
/yx38/altq/rkl/elp
/vm9
/vm9/rx22
/yx38/altq/rkl/rx22
/yx38/altq/rkl/2y0l
*/
