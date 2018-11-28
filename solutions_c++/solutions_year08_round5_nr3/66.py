#include <stdio.h>
#include <string.h>
int nT,T;
int M,N;
char p[10][11];
int f1[1024],f2[1024];
int*obtain;
int*lobtain,*t;
int sz;
int main()
{
	freopen("C:\\test.in","r",stdin);
	FILE*f=fopen("C:\\test.out","w");
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		scanf("%d%d",&M,&N);
		int i,j,k,l,m,bst=0;
		for (i=0;i<M;i++)
			scanf("%s",p[i]);
		obtain=f1;
		lobtain=f2;
		sz=4<<N;
		memset(obtain,-1,sz);
		obtain[0]=0;
		for (i=0;i<M;i++)
		{
			t=obtain;
			obtain=lobtain;
			lobtain=t;
			memset(obtain,0,sz);
			for (j=1<<N;j--;)
			{
				int c=0;
				for (k=0;k<N;k++)
					if (j&(1<<k))
					{
						c++;
						if (p[i][k]=='x'||((k!=0)&&(j&(1<<(k-1))))||(j&(1<<(k+1))))
						{
							obtain[j]=-1;
							goto cont;
						}
					}
				int forb=j>>1|j<<1;
				for (k=1<<N;k--;) if (!(forb&k))
					if (lobtain[k]!=-1&&lobtain[k]+c>obtain[j])
						if ((obtain[j]=lobtain[k]+c)>bst)
							bst=obtain[j];
cont:
				continue;
			}
		}
		fprintf(f,"Case #%d: %d\n",nT-T,bst);
	}
	fclose(f);
}