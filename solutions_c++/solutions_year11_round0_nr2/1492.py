#include<cstdlib>
#include<cstdio>
#include<cstring>
int C,D,N;
char F[300][300];
bool O[300][300];
char L[300],Lt;
void Print(int c)
{
	printf("Case #%d: [",c);
	for (int i=0;i<Lt-1;i++)
		printf("%c, ",L[i]);
	if (Lt-1>=0)
		printf("%c",L[Lt-1]);
	printf("]\n");
}
void Solve()
{
	memset(F,0,sizeof(F));
	memset(O,0,sizeof(O));
	scanf("%d",&C);
	char t[200];
	for (int i=0;i<C;i++)
	{
		scanf("%s",t);
		F[t[0]][t[1]]=F[t[1]][t[0]]=t[2];
	}
	scanf("%d",&D);
	for (i=0;i<D;i++)
	{
		scanf("%s",t);
		O[t[0]][t[1]]=O[t[1]][t[0]]=true;
	}
	scanf("%d",&N);
	scanf("%s",t);
	memset(L,0,sizeof(L));
	Lt=0;
	for (i=0;i<N;i++)
	{
		if (Lt>0&&F[t[i]][L[Lt-1]]!=0)
			L[Lt-1]=F[t[i]][L[Lt-1]];
		else
		{
			bool clr=false;
			for (int j=0;j<Lt;j++)
				if (O[L[j]][t[i]])
				{
					clr=true;
					break;
				}
			if (clr) Lt=0;
				else L[Lt++]=t[i];
		}
	}
}
void Init()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		Solve();
		Print(i+1);
	}
}
int main()
{
	Init();
	return 0;
}
