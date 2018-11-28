#include<iostream>

using namespace std;

void main()
{
	int T,N[50],R[50],k[50],g[50][10],cost[50];
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	while (T<1 || T>50)
	{
		cout<<"Invalid input (T max = 50). Enter again"<<endl;
		cin>>T;
	}
	for(int i=0;i<T;i++)
	{
		cin>>R[i]>>k[i]>>N[i];
		for(int j=0;j<N[i];j++)
			cin>>g[i][j];
	}

	int sum=0,temp,flag=0;

	for(i=0;i<T;i++)
	{
		cost[i]=0;
		if(R[i]>=1 && R[i]<=1000 && k[i]>=1 && k[i]<=100 && N[i]>=1 && N[i]<=10)
		{
			for(int j=0;j<N[i];j++)
				if(g[i][j]<=k[i] && g[i][j]>=1 && g[i][j]<=10 )
				flag=0;
				else flag=1;
			
			for(int l=0;l<R[i];l++)
			{
			sum=0;
			for(j=0;j<N[i];j++)
			{
				if((sum+g[i][0])<=k[i])
				{
					sum+=g[i][0];
					temp=g[i][0];
					for(int m=0;m<N[i];m++)
					g[i][m]=g[i][m+1];
					g[i][N[i]-1]=temp;
				}
				else 
				{
					break;
				}

			}
			
			cost[i] += sum;
		}
		}
		else flag=1;
	if(flag==1) cout<<"Case #"<<i+1<<": Invalid input data"<<endl;
	else cout<<"Case #"<<i+1<<": "<<cost[i]<<endl;
	}
}

			
