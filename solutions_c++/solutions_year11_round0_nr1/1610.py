#include <stdio.h>
#include <cmath>
using namespace std;

int p[110];
int r[110];
int nr;
int po,pb;

int main()
{
	int T,N,P,nCase=0;
	char R[2];
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		nr=0;
		for(int i=0;i<N;i++)
		{
			scanf("%s%d",R,&P);
			r[nr]=R[0]=='O'?0:1;
			p[nr++]=P;
		}
		po=pb=1;
		int timeslice=0,pre=-1;
		int sum=0;
		for(int i=0;i<nr;i++)
		{
			if(r[i]==0)
			{
				if(pre==-1||pre==0)
				{
					timeslice+=abs(p[i]-po)+1;
					po=p[i];
					pre=0;
				}
				else
				{
					int tmp=abs(p[i]-po);
					int delta=0;
					if(timeslice>=tmp)
						delta=1;
					else
						delta=tmp-timeslice+1;
					sum+=timeslice;
					timeslice=delta;
					po=p[i];
					pre=0;
				}
			}
			else
			{
				if(pre==-1||pre==1)
				{
					timeslice+=abs(p[i]-pb)+1;
					pb=p[i];
					pre=1;
				}
				else
				{
					
					int tmp=abs(p[i]-pb);
					int delta=0;
					if(timeslice>=tmp)
						delta=1;
					else
						delta=tmp-timeslice+1;
					sum+=timeslice;
					timeslice=delta;
					pb=p[i];
					pre=1;
				}
			}
		}
		sum+=timeslice;
		printf("Case #%d: ",++nCase);
		printf("%d\n",sum);
	}
	return 0;
}