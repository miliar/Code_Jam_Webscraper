// joy
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
const int MAX=1000+10;

int N;
struct NODE
{
	int a,b;
	int id;
}nod[MAX];

bool cmp(NODE x,NODE y)
{
	int tt=x.b*y.a,zz=x.a*y.b;
	if(tt==zz) return x.id<y.id;
	return tt>zz;
}
int main()
{
	int T;scanf("%d",&T);
	
	while(T--)
	{
		scanf("%d",&N);
		for(int i=1;i<=N;i++)
		{
			scanf("%d",&nod[i].a);
		}
		for(int i=1;i<=N;i++)
		{
			scanf("%d",&nod[i].b);
			nod[i].id=i-1;
		}
		
		sort(&nod[1],&nod[N+1],cmp);
		
		static int CN=0;
		printf("Case #%d:",++CN);
		for(int i=1;i<=N;i++) printf(" %d",nod[i].id);
		printf("\n");
	}
	
	return 0;
}
