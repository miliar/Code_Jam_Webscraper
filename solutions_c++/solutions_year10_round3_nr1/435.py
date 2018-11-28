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

	int N;
	int arr[10001][2];
	for(int cp=1;cp<=notimes;cp++ )
	{
		cin>>N;
		long int total=0;
		for(int i=0;i<N;i++)
		{
			cin>>arr[i][0]>>arr[i][1];
			for(int j=0;j<i;j++)
			{
				if( ( arr[j][0] > arr[i][0] && arr[j][1]< arr[i][1] ) || ( arr[j][0] < arr[i][0] && arr[j][1] > arr[i][1] ) )
					total++;
			}
		}
		
			
		cout<<"Case #"<<cp<<": "<<total<<endl;
	}
	return 0;
}
