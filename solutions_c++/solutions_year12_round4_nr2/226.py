// B
#include<iostream>
using namespace std;
const int MAX=1000+10;

int N,W,L;
struct NODE
{
	int id;
	int rad;
	int x,y;
}nod[MAX];

bool cmp(NODE a,NODE b)
{
	return a.rad>b.rad;
}

bool cmp2(NODE a,NODE b)
{
	return a.id<b.id;
}
int main()
{
	int T;scanf("%d",&T);
	
	while(T--)
	{
		scanf("%d%d%d",&N,&W,&L);
		for(int i=1;i<=N;i++) 
		{
			scanf("%d",&nod[i].rad);
			nod[i].id=i;
		}
		sort(&nod[1],&nod[N+1],cmp);
		
		nod[1].x=0;
		nod[1].y=0;
		int now=nod[1].rad;
		for(int i=2;i<=N;i++)
		{
			if(nod[i-1].y+nod[i-1].rad+nod[i].rad<=L)
			{
				nod[i].x=nod[i-1].x;
				nod[i].y=nod[i-1].y+nod[i-1].rad+nod[i].rad;
			}
			else
			{
				nod[i].x=nod[i-1].x+now+nod[i].rad;
				nod[i].y=0;
				now=nod[i].rad;
			}
		}
		
		sort(&nod[1],&nod[N+1],cmp2);
		
		static int CN=0;
		printf("Case #%d:",++CN);
		for(int i=1;i<=N;i++) printf(" %.1f %.1f",0.0+nod[i].x,0.0+nod[i].y);
		printf("\n");
	}
	
	
	return 0;
}
