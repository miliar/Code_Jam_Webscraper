#include<iostream>
#include<cstring>
using namespace std;
void tobinary(int m,int *b)
{
	int i=0;
	while (m>0)
	{
		b[i++]=m%2;
		m/=2;
	}
	while(i<=30)
	{
		b[i++]=0;
	}
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
		int n;
		scanf("%d",&n);
		int x[1100],j;
		int b[1100][40];
		int min=1000001;
		int sum=0;
		for(j=1;j<=n;j++)
		{
			scanf("%d",&x[j]);
			if(x[j]<min) min=x[j];
			sum+=x[j];
			tobinary(x[j],&b[j][0]);
		}
		int k;
		bool yes=true;
		for(j=0;j<=30;j++)
		{
			int many=0;
			for(k=1;k<=n;k++)
				many+=b[k][j];
			if(many%2==1){yes=false;break;}
		}
		if(yes)
		{
			cout<<"Case #"<<i<<": "<<sum-min<<endl;
		}
		else 
		{
			cout<<"Case #"<<i<<": "<<"NO"<<endl;
		}


	}

		
	
return 0;
}