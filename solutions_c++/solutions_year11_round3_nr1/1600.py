#include<cstring>
#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
main()
{
	int test,m,n,i,j,cas=1;
	int arr[52][52];
	string inp[51];
	scanf("%d",&test);
	while(cas<=test)
	{
		cin>>m>>n;
		memset(&arr,-1,sizeof(arr));
		for(i=1;i<=m;i++)
		{
			cin>>inp[i];
			for(j=1;j<=n;j++)
			{
				if(inp[i][j-1]=='.')
					arr[i][j]=0;
				else
					arr[i][j]=1;
			}
		}
		int flag=0;
		for(i=1;i<=m;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(arr[i][j]==1)
				{
					if(arr[i][j+1]!=1 || arr[i+1][j]!=1 || arr[i+1][j+1]!=1)
					{
						flag=1;
						break;
					}
					inp[i][j-1]='/';
					inp[i][j]='\\';
					inp[i+1][j-1]='\\';
					inp[i+1][j]='/';
					arr[i][j]=arr[i][j+1]=arr[i+1][j]=arr[i+1][j+1]=0;
				}
			}
			if(flag==1)
				break;
		}
		if(flag==0)
		{
			cout<<"Case #"<<cas<<":"<<endl;
			for(i=1;i<=m;i++)
				cout<<inp[i]<<endl;
		}
		else
			cout<<"Case #"<<cas<<":"<<endl<<"Impossible"<<endl;
		cas++;
	}
}
			
		
			
				
					
		
	
	
