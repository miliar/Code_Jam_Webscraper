#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{
	int T,N;
	int ti,ni;
	int op[111],bp[111],opc,bpc;
	char r[111];
	int p[111];
	int bpn,opn,opi,bpi,time,i;
	//freopen("d:\\A-large.in","r",stdin);
	//freopen("d:\\aoutbig.txt","w",stdout);
	scanf("%d",&T);
	for (ti=0;ti<T;ti++)
	{
		scanf("%d",&N);
		opc=bpc=0;
		op[opc++]=1;
		bp[bpc++]=1;
		for (ni=0;ni<N;ni++)
		{
			scanf(" %c %d",&r[ni],&p[ni]);
			if (r[ni]=='O')
				op[opc++]=p[ni];
			else
				bp[bpc++]=p[ni];
		}
		for (i=0;i<opc-1;i++)
			op[i]=abs(op[i+1]-op[i])+1;
		for (i=0;i<bpc-1;i++)
			bp[i]=abs(bp[i+1]-bp[i])+1;
		opi=bpi=0;
		time=0;
		/*for (i=0;i<opc-1;i++)
			printf("%d ",op[i]);
		printf("\n");
		for (i=0;i<bpc-1;i++)
			printf("%d ",bp[i]);
		printf("\n");*/
		for (i=0;i<ni;i++)
		{
			if (r[i]=='O')
			{
				time+=op[opi];
				if (bp[bpi]<=op[opi]) bp[bpi]=1; else bp[bpi]-=op[opi];
				opi++;
			}else
			{
				time+=bp[bpi];
				if (op[opi]<=bp[bpi]) op[opi]=1; else op[opi]-=bp[bpi];
				bpi++;
			}
		}
		printf("Case #%d: %d\n",ti+1,time);
	}
	//fclose(stdin);
	//fclose(stdout);
	return 0;
}

