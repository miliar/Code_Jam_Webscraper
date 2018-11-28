#include <iostream>
using namespace std;

int buf[1050]={0},num[1050]={0};

int main(void)
{
	freopen("tpark.in","r",stdin);
	freopen("tpark.out","w",stdout);
	int T;
	cin>>T;
	for(int M=1;M<=T;M++)
	{
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;i++)
			scanf("%d",&buf[i]);
		bool tag=false;
		int now=0,time,sall=0;
		for(int i=0;i<r;i++)
		{
			int sum=0;
			int st=now;
			while(1)
			{
				sum+=buf[now];
				if(sum>k)
				{
					sum-=buf[now];
					break;
				}
				num[i]=sum;
				now=(now+1)%n;
				if(now==st) break;
			}
			sall+=sum;
			/*if(now==0)
			{
				tag=true;
				time=i;
				break;
			}*/
		}
		//if(tag==false)
		{
			printf("Case #%d: %d\n",M,sall);
		}
		/*else
		{
			int t=sall*(r/(time+1));
			t+=num[r%(time+1)-1];
			printf("Case #%d: %d\n",M,t);
		}*/
	}
	return 0;
}