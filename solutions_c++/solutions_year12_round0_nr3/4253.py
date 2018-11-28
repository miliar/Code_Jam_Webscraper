#include<stdio.h>
#include<string.h>

char a[1111];
char b[1111];

int main(void)
{
	int l1, l2, l3, l4, l0, T, A, B;

	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"%d %d\n",l0,T);
		scanf("%d %d",&A,&B);

		int ret = 0;

		for(l1=A;l1<=B;l1++)
		{
			for(l2=l1+1;l2<=B;l2++)
			{
				sprintf(a,"%d",l1);
				for(l3=0;l3<10;l3++)
				{
					char temp = a[0];
					for(l4=0;a[l4];l4++)
					{
						a[l4] = a[l4+1];
					}
					a[l4-1] = temp;

					sprintf(b,"%d",l2);
					if(strcmp(a,b) == 0)
					{
						ret++;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",l0,ret);
	}
}