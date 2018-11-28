#include<cstdlib>
#include<cstdio>
#include<cmath>
int N;
int P[100];
char R[100];
int p[200];
void Solve(int c)
{
	p['O']=1,p['B']=1;
	int time=0;
	for (int i=0;i<N;i++)
	{
		int dur=abs(P[i]-p[R[i]])+1;
		p[R[i]]=P[i];
		char other=(R[i]=='O'?'B':'O');
		for (int j=i+1;j<N;j++)
			if (R[j]==other)
			{
				int dis=P[j]-p[other];
				int dir=(dis>=0?1:-1);
				if (abs(dis)>dur)
					p[other]+=dir*dur;
				else
					p[other]=P[j];
				break;
			}
		time+=dur;
	}
	printf("Case #%d: %d\n",c,time);
}
void Init()
{
	scanf("%d",&N);
	char t[10];
	for (int i=0;i<N;i++)
	{
		scanf("%s",t);
		R[i]=t[0];
		scanf("%d",&P[i]);
	}
}
int main()
{
	freopen("a.txt","r",stdin);
	freopen("b.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		Init();
		Solve(i+1);
	}
	return 0;
}
