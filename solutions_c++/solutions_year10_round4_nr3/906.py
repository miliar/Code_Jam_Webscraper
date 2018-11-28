#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>

using namespace std;


int main()
{
	int notimes;
	scanf("%d",&notimes);
	int R;
	int X1,X2,Y1,Y2;
	int arr[105][105],copy[105][105];
	for(int cp=1;cp<=notimes;cp++ )
	{
		cin>>R;
		for(int i=1;i<=100;i++)
		{
			for(int j=1;j<=100;j++)
			{
				arr[i][j]=0;
			}
		}

		for(int i=0;i<R;i++)
		{
			cin>>X1>>Y1>>X2>>Y2;
			for(int j=X1;j<=X2;j++)
			{
				for(int k=Y1;k<=Y2;k++)
				{
					arr[j][k]=1;
				}
			}
		}
/*		for(int i=1;i<=6;i++)
		{
			for(int j=1;j<=6;j++)
			{
				cout<<arr[i][j]<<" ";
			}
			cout<<endl;
		}
*/	
		int flag=1;
		int T=0;
		while(flag==1)
		{
			flag=0;
			for(int i=1;i<=100;i++)
			{
				for(int j=1;j<=100;j++)
				{
					if( ( ( (i-1)>0 && arr[i-1][j]==1 ) || ( (j-1)>0 && arr[i][j-1]==1 ) ) && arr[i][j]==1 )
					{
						flag=1;
						copy[i][j]=1;
					}
					else
						copy[i][j]=0;
					if( ( (i-1)>0 && arr[i-1][j]==1 ) && ( (j-1)>0 && arr[i][j-1]==1 ) && arr[i][j]==0 )
					{ 
						copy[i][j]=1; 
						flag=1; 
					}			
				}
			}
			for(int i=1;i<=100;i++)
				for(int j=1;j<=100;j++)
					arr[i][j]=copy[i][j];
			T++;
		}
		
		cout<<"Case #"<<cp<<": "<<T<<endl;
	}
	return 0;
}
