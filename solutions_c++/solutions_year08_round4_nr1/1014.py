#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define Max 	10000
#define Pi      acos(-1)
#define Ee      exp(1)
#define min(a,b)      (a)>(b)?(b):(a)


void Kevinew()
{
#ifndef  ONLINE_JUDGE
	freopen("in.txt","r",stdin);
#endif
}


typedef struct  
{
	int g,c;
	int v;
} Node;

Node nod[11000];

int n;

int mem[11000][2];

int gogo(int x,int v){
	if(mem[x][v]!=-1) return mem[x][v];
	int i;
	if(x<=(n-1)/2){
		int mans=1<<20;

		if(nod[x].c)	{
			if(v==1)	{
				mans=min(mans,gogo(x*2,1)+gogo(x*2+1,1) );
				mans=min(mans,gogo(x*2,0)+gogo(x*2+1,1)+(nod[x].g?1:0));
				mans=min(mans,gogo(x*2,1)+gogo(x*2+1,0)+(nod[x].g?1:0));
			}
			else 	{
				mans=min(mans,gogo(x*2,0)+(nod[x].g?0:1));
				mans=min(mans,gogo(x*2+1,0)+(nod[x].g?0:1));
				mans=min(mans,gogo(x*2,0)+gogo(x*2+1,0));
			}
		}
		else{
			if(v==1)	{
				if(nod[x].g)	{
					mans=min(mans,gogo(x*2,1)+gogo(x*2+1,1));
				}
				else{
					mans=min(mans,gogo(x*2,1)+gogo(x*2+1,0));
					mans=min(mans,gogo(x*2,0)+gogo(x*2+1,1));
					mans=min(mans,gogo(x*2,1)+gogo(x*2+1,1));
				}
			}
			else{
				if(nod[x].g){
					mans=min(mans,gogo(x*2,0)+gogo(x*2+1,1));
					mans=min(mans,gogo(x*2,1)+gogo(x*2+1,0));
					mans=min(mans,gogo(x*2,0)+gogo(x*2+1,0));
				}
				else{
					mans=min(mans,gogo(x*2,0)+gogo(x*2+1,0));
				}
			}
		}
		mem[x][v]=mans;
		return mans;
	}
	else	{
		if(v==nod[x].v)
			return 0;
		else 
			return 1<<20;
	}
}

int main()
{
	int T,Ti=0;
	int i;

	scanf("%d",&T);
	while(T--){
		Ti++;
		memset(mem,-1,sizeof(mem));
		int v;
		scanf("%d",&n);
		scanf("%d",&v);
		for( i=1;i<=(n-1)/2;i++){	
			int t1,t2;
			scanf("%d%d",&t1,&t2);
			nod[i].g=t1;
			nod[i].c=t2;
		}
		for( i=(n-1)/2+1;i<=n;i++)	{
			scanf("%d",&nod[i].v);
		}
		int ans=gogo(1,v);
		printf("Case #%d: ",Ti);

		if(ans<1<<20)
			printf ("%d\n",ans);	
		else
			printf ("IMPOSSIBLE\n");

	}

	return 0;
}


