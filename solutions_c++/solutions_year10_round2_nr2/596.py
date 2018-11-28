#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;
int main()
{
	int notimes;
	scanf("%d",&notimes);
	
	int N,K,T;
	long long int B;
	long long int pos[100];
	int speed[100];
	for(int cp=1;cp<=notimes;cp++ )
	{
		cin>>N>>K>>B>>T;
		for(int i=1;i<=N;i++)
			cin>>pos[i];
		for(int i=1;i<=N;i++)
			cin>>speed[i];
		
		int coun=0;
		int chicks=0;
		long long int total=0;
		int flag=0;
		for(int i=N;i>=1;i--)
		{
			if( pos[i]+ speed[i]*T >= B)
			{
				total+=coun;
				chicks++;
			}
			else
				coun++;
			if(chicks==K)
			{
				flag=1;
				break;
			}
		}
		if( flag==1)
		{	
			cout<<"Case #"<<cp<<": "<<total<<endl;
		}
		else
			cout<<"Case #"<<cp<<": "<<"IMPOSSIBLE"<<endl;
			
	}
	return 0;
}
