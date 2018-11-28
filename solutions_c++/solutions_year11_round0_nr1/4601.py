#include <cstdio>
#include <cstring>

int		S1[200],S2[200],No1[200],No2[200];
int		P1,P2,N1,N2,n1,n2,n,Ans,T;
bool	Flag1,Flag2;
char	ch;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for (int k=1;k<=T;k++)
	{
		memset(S1,0,sizeof(S1));
		memset(S2,0,sizeof(S2));
		memset(No1,0,sizeof(No1));
		memset(No2,0,sizeof(No2));
		N1=N2=0;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%s",&ch);
			if (ch=='O')	scanf("%d",&S1[++N1]),	No1[N1]=i;
			else			scanf("%d",&S2[++N2]),	No2[N2]=i;
		}
		Ans=0;
		P1=P2=1;
		n=1;
		n1=n2=1;
		while (1)
		{
			Ans++;
			Flag1=Flag2=0;
			if (P1==S1[n1] && No1[n1]==n)
			{
				n1++;
				n++;
				Flag1=1;
			}
			if (!Flag1)
			if (P2==S2[n2] && No2[n2]==n)
			{
				n2++;
				n++;
				Flag2=1;
			}
			if (!Flag1 && No1[n1]>0)
			{
				if (S1[n1]>P1)	P1++;
				if (S1[n1]<P1)	P1--;
			}
			if (!Flag2 && No2[n2]>0)
			{
				if (S2[n2]>P2)	P2++;
				if (S2[n2]<P2)	P2--;
			}
			if (S1[n1]==0 && S2[n2]==0)	break;
		}
		printf("Case #%d: %d\n",k,Ans);
	}
}
