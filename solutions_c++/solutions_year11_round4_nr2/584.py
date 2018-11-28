#include<cstdio>

#define LL long long

const int mx=550;

int r,c,d;
LL a[mx][mx];
LL sum_m[mx][mx];
LL sum_p_mx[mx][mx];
LL sum_p_my[mx][mx];

void init()
{
	int i,j;
	for(i=0;i<=r;i++)
	{
		for(j=0;j<=c;j++)
		{
			sum_m[i][j]=0;
			sum_p_mx[i][j]=0;
			sum_p_my[i][j]=0;
		}
	}
}

LL calsum(LL a[][mx],int x,int y,int k)
{
	return a[x+k][y+k]-a[x+k][y]-a[x][y+k]+a[x][y];
}

LL calmx(int x,int y ,int k)
{
	return x*(a[x][y]+a[x][y+k-1])+(x+k-1)*(a[x+k-1][y]+a[x+k-1][y+k-1]);
}

LL calmy(int x,int y ,int k)
{
	return y*(a[x][y]+a[x+k-1][y])+(y+k-1)*(a[x][y+k-1]+a[x+k-1][y+k-1]);
}

LL calm(int x,int y,int k)
{
	return a[x][y]+a[x+k-1][y]+a[x][y+k-1]+a[x+k-1][y+k-1];
}

bool can(int k)
{
	int i,j;
	for(i=0;i+k<=r;i++)
	{
		for(j=0;j+k<=c;j++)
		{
			LL p_mp_x=calsum(sum_p_mx,i,j,k)-calmx(i,j,k);
			LL p_mp_y=calsum(sum_p_my,i,j,k)-calmy(i,j,k);
			LL c_mp_x=(calsum(sum_m,i,j,k)-calm(i,j,k))*(i+i+k);
			LL c_mp_y=(calsum(sum_m,i,j,k)-calm(i,j,k))*(j+j+k);
			if(k==5&&i==1&&j==1)
			{
				printf("here: %lld %lld %lld %lld\n\n",p_mp_x*2,c_mp_x,p_mp_y*2,c_mp_y);
			}
			if(p_mp_x*2==c_mp_x&&p_mp_y*2==c_mp_y)
				return true;
		}
	}
	return false;
}

int main()
{
	int i,j,k;
	int t,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&c,&d);
		init();
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				scanf("%1d",&a[i][j]);
				sum_m[i+1][j+1]=d+a[i][j];
				sum_p_mx[i+1][j+1]=(d+a[i][j])*i;
				sum_p_my[i+1][j+1]=(d+a[i][j])*j;
			}
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				sum_m[i+1][j+1]+=sum_m[i+1][j];
				sum_p_mx[i+1][j+1]+=sum_p_mx[i+1][j];
				sum_p_my[i+1][j+1]+=sum_p_my[i+1][j];
			}
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				sum_m[i+1][j+1]+=sum_m[i][j+1];
				sum_p_mx[i+1][j+1]+=sum_p_mx[i][j+1];
				sum_p_my[i+1][j+1]+=sum_p_my[i][j+1];
			}
		}

		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				printf("%d ",d+a[i][j]);
			}printf("\n");
		}
		printf("\n");
		for(i=0;i<=r;i++)
		{
			for(j=0;j<=c;j++)
			{
				printf("%d ",sum_m[i][j]);
			}printf("\n");
		}
		printf("\n");
		for(i=0;i<=r;i++)
		{
			for(j=0;j<=c;j++)
			{
				printf("%d ",sum_p_mx[i][j]);
			}printf("\n");
		}
		printf("\n");
		for(i=0;i<=r;i++)
		{
			for(j=0;j<=c;j++)
			{
				printf("%d ",sum_p_my[i][j]);
			}printf("\n");
		}

		int start=r<c?r:c;
		for(k=start;k>=3;k--)
		{
			if(can(k))
				break;
		}
		printf("Case #%d: ",ca++);
		if(k>=3)
			printf("%d\n",k);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
