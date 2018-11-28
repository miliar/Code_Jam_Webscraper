#include "stdio.h"
#include "stdlib.h"

int cmp(const void *a,const void *b)
{
	return *(int *)a-*(int*)b;
}

int a[200000][2];

int main()
{
	freopen("A-small-attempt0.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ca,v,i,n,A,B,C,D,M,j,k,i1,j1,k1,e,f,g;
	__int64 t,s,p,sum;
	scanf("%d",&ca);
	for(v=1;v<=ca;v++)
	{
		int b[3][3]={0};
		bool ex[3][3][3][3][3][3]={0};
		sum=0;
		scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&a[0][0],&a[0][1],&M);
		t=a[0][0]%M;
		s=a[0][1]%M;
		t=t%3;
		s=s%3;
		b[t][s]++;
		for(i=1;i<n;i++)
		{
			t=a[i-1][0]*(__int64)A;
			t=t+B;
			t=t%M;
			a[i][0]=(int)t;
			s=a[i-1][1]*(__int64)C;
			s=s+D;
			s=s%M;
			a[i][1]=(int)s;
			b[t%3][s%3]++;
		}
		p=0;
		for(i=0;i<3;i++)
		{
			for(i1=0;i1<3;i1++)
			{
				e=b[i][i1];
				b[i][i1]--;
				for(j=0;j<3;j++)
				{
					for(j1=0;j1<3;j1++)
					{
						f=b[j][j1];
						b[j][j1]--;
						for(k=0;k<3;k++)
						{
							for(k1=0;k1<3;k1++)
							{
								g=b[k][k1];
								if((i+j+k)%3==0&&(i1+j1+k1)%3==0)
								{
									p=p+e*(__int64)f*g;
								}
							}
						}
						b[j][j1]++;
					}
				}
				b[i][i1]++;
			}
		}
		sum=sum+p/6;
		printf("Case #%d: %I64d\n",v,sum);
	}
	return 0;
}