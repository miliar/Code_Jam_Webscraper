#include<iostream>
#include<cstring>
using namespace std;
int fun(int n,int a,int b)
{
	int k[2000];
	int i;
	int nn=n;
	for(i=0;i<1999;i++)
	{
		k[i]=0;
	}
	int t[5];
	int tt=0;
	while(nn>0)
	{
		t[tt++]=nn%10;
		nn/=10;
	}
	int sum=0;
	if(tt==1) return 0;
	else if(tt==4) return 0;
	else if(tt==2)
	{
		int temp;
		if(t[0]==0) return 0;
		else temp=t[0]*10+t[1];
		if(temp>n && temp<=b && temp>=a) sum++;
	}
	else if(tt==3)
	{
		int temp;
		if(t[0]!=0) 
		{
			temp=t[0]*100+t[2]*10+t[1];
		if(temp>n && temp<=b && temp>=a) sum++;
		}
		if(t[1]!=0)
		{
			temp=t[1]*100+t[0]*10+t[2];
		if(temp>n && temp<=b && temp>=a) sum++;
		}
	}
	return sum;
}
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	int i;
	for(i=1;i<=T;i++)
	{
			int a,b;
			scanf("%d%d",&a,&b);
			int c,sum=0;
			for(c=a;c<=b;c++)
			{
				sum+=fun(c,a,b);
			}
			cout<<"Case #"<<i<<": "<<sum<<endl;

	}

		
	
return 0;
}