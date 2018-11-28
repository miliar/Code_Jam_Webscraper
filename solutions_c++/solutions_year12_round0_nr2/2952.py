#include <fstream>
#include <vector>
#include <iostream>
int dp[31][10];
using namespace std;
void main()
{
	for(int i=0;i<31;i++)
		for(int j=0;j<10;j++)
			dp[i][j]=-1;
	for(int i=0;i<=10;i++)
	{
		int arr[6][3]={{0,0,0},{1,0,0},{1,1,0},{2,0,0},{2,2,0},{2,1,0}};
		int surprise[]={0,0,0,1,1,1};
		for(int j=0;j<6;j++)
		{
			int a,b,c;
			a=b=c=i;
			a+=arr[j][0];
			b+=arr[j][1];
			c+=arr[j][2];
			dp[a+b+c][a]=(dp[a+b+c][a]==0)?0:surprise[j];
		}
	}
	ifstream cin("input.in");
	ofstream cout("output.out");
	int T,N,S,p,x;
	cin>>T;
	cin.get();
	for(int n=1;n<=T;n++)
	{
		cin>>N>>S>>p;
		int count=0;
		for(int i=0;i<N;i++)
		{	cin>>x;
			int f=-1;
			for(int k=p;k<=10;k++)
			{
				
				if(dp[x][k]==0 || (dp[x][k]==1 && f!=0))
					f=dp[x][k];
			}
			if(f==0)
				count++;
			else if(S>0 && f==1)
			{
				count++;
				S--;
			}
		}
		cin.get();
		cout<<"Case #"<<n<<": "<<count<<endl;
	}	
}