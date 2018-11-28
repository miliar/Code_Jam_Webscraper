#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
#include<string.h>
#include<map>
#include<math.h>
#include<string>
#include<queue>
#include<csetjmp>
#include<cstring>
#include<vector>
#define M 1000000007
int mam[5][110],mark[1100];
struct B
{
	int x;
	char y;
}w[110];
int main()
{
	int i,n,m,cs=0,k,T,t1,t2,j,c,t,f;
	char a[5],b[5];
	freopen("A.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		t1=t2=1;
		memset(mam,-1,sizeof(mam));
		memset(mark,0,sizeof(mark));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s%s",a,b);
			sscanf(b,"%d",&t);
			w[i].y=a[0];
			w[i].x=t;
			if(a[0]=='O') mam[0][t]=i;
			else mam[1][t]=i;
		}
		c=0;
		for(k=0,i=1;;i++)
		{
			if(t1==w[k].x&&w[k].y=='O')
				if(!mark[k])
				{
					for(f=0,j=k+1;j<n;j++)
						if(w[j].y=='B')
						{
							if(w[j].x>t2)
								t2++;
							else if(w[j].x<t2)t2--;
							break;
						}
					mark[k]=1;
					c++;
					k++;
					if(c==n) break;
					continue;
				}
			if(t2==w[k].x&&w[k].y=='B')
				if(!mark[k]) 
				{
					for(f=0,j=k+1;j<n;j++)
						if(w[j].y=='O')
						{
							if(w[j].x>t1)
								t1++;
							else if(w[j].x<t1) t1--;
							break;
						}
					mark[k]=1;
					c++;
					k++;
					if(c==n) break;
					continue;
				}
			if(w[k].y=='O')
			{
				if(t1<w[k].x) t1++;
				else if(t1>w[k].x) t1--;
				for(f=0,j=k+1;j<n;j++)
					if(w[j].y=='B')
					{
						if(w[j].x>t2)
							t2++;
						else if(w[j].x<t2) t2--;
						break;
					}
			}
		    if(w[k].y=='B')
			{
				if(t2<w[k].x) t2++;
				else if(t2>w[k].x) t2--;
				
				for(f=0,j=k+1;j<n;j++)
					if(w[j].y=='O')
					{
						if(w[j].x>t1)
							t1++;
						else if(w[j].x<t1) t1--;
						break;
					}
			}
		}
		printf("Case #%d: %d\n",++cs,i);
	}
	return 0;
}