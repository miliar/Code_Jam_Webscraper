#include<stdio.h>
#include<math.h>

int db[2000001][10];


void calc(int n)
{
	int m=n;
	int r;
	int dig=0;
	int c=0;
	int num;
	while(m>0)
	{
		m=m/10;
		c++;
	}
	
	m=n;

	while(m>0)
	{	dig++;
		int p=pow(10,dig);
		r=n%p;
		m=n/p;
		
		num=m+r*pow(10,c-dig);
		
		if(num>n)
		{
			int chk=0;
			for(int i=1;i<=db[n][0];i++)
				if(num==db[n][i])
				{
					chk=1;
					break;
				}
				
			if(chk==0)
			{
				db[n][0]++;
				db[n][db[n][0]]=num;
			}
		}
		
	}

}
int main()
{
	//int db[2000001][10];
	
	for(int i=0;i<2000001;i++)	
		for(int j=0;j<10;j++)
			db[i][j]=0;

		for(int i=0;i<2000001;i++)
			calc(i);
			
		int n,a,b;
		
		scanf("%d",&n);
		int t=0;
		while(n--)
		{
			t++;
			scanf("%d %d",&a,&b);
			int count=0;
			for(int i=a;i<=b;i++)
			{
				for(int j=1;j<=db[i][0];j++)
					if(db[i][j]<=b)
					{
						count++;
					//	printf("(%d %d)\n",i,db[i][j]);
					}
			}
			
			printf("Case #%d: %d\n",t,count);
		}
}