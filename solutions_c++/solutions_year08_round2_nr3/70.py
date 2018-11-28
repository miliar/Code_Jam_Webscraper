#include<stdio.h>
#include<string.h>

const int maxn = 1000006;
int n;
int m;
int a[100];
int b[maxn];

int main() {
	int cs, step;
	scanf("%d",&cs);
	for(step=1;step<=cs;step++)
	{
		int i,j,k,i1,j1,k1;
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)scanf("%d",&a[i]);

		memset(b, 0, sizeof(b));
		j = n-1;
		for(i=1;i<=n;i++)
		{
			i1 = i % (n-i+1);
			if(i1==0) i1 = n-i+1;
			while(i1--)
			{
				while(true)
				{
					j=(j+1)%n;
					if(b[j]==0) break;
				}
			}
			b[j] = i;
		}
		printf("Case %d:", step);
		for(i=0;i<m;i++)printf(" %d", b[a[i]-1]);
		printf("\n");
	}
	return 0;
}
