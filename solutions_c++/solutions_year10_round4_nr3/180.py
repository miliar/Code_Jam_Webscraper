#include<stdio.h>

int T;
int a[101][101], b[101][101];
int n;
int nn;

int main(void)
{
	int l0, l1, l2, l3, ret;
	int t1, t2, t3, t4;
	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);
	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"%d\n",l0);
		scanf("%d",&nn);
		for(l1=0;l1<101;l1++) for(l2=0;l2<101;l2++) a[l1][l2] = 0;
		for(l1=0;l1<nn;l1++)
		{
			scanf("%d %d %d %d",&t1,&t2,&t3,&t4);
			for(l2=t2;l2<=t4;l2++)
			{
				for(l3=t1;l3<=t3;l3++)
				{
					a[l2][l3] = 1;
				}
			}
		}
		
		for(ret=0;;ret++)
		{
			//printf("..%d\n",ret);
			for(l1=1;l1<=100;l1++) for(l2=1;l2<=100;l2++) if(a[l1][l2] == 1) goto maki;
			break;
maki:
			for(l1=1;l1<=100;l1++) for(l2=1;l2<=100;l2++)
			{
				if(a[l1][l2])
				{
					if(a[l1][l2-1] || a[l1-1][l2]) b[l1][l2] = 1;
					else b[l1][l2] = 0;
				}
				else
				{
					if(a[l1][l2-1] && a[l1-1][l2]) b[l1][l2] = 1;
					else b[l1][l2] = 0;
				}
			}
			for(l1=1;l1<=100;l1++) for(l2=1;l2<=100;l2++) a[l1][l2] = b[l1][l2];
		}
		printf("Case #%d: %d\n",l0,ret);
	}
}