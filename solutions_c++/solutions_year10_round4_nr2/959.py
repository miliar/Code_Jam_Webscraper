#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<math.h>
#include<cmath>

using namespace std;


int main()
{
	int notimes;
	scanf("%d",&notimes);
	int arr[1500],P,mark[1500];
	for(int cp=1;cp<=notimes;cp++ )
	{
		cin>>P;
		for(int i=0;i<1035;i++)
		{
			arr[i]=0;
		}

		for(int i=0;i<pow(2,P);i++)
		{
			cin>>arr[i];
			arr[i]= P- arr[i];
		}
		
		int temp;
		for(int i=P-1;i>=0;i--)
		{
			for(int j=0;j<pow(2,i);j++)
				cin>>temp;	
		}
		
		int level=P;
		int start=0;
		int iter=1;
			
		int total =0;
//		for(int i=0;i<pow(2,P);i++)
//			cout<<arr[i]<<" ";
//		cout<<endl;
		while(level>0)
		{
			start=0;
			iter=1;
			for(int i=0;i<pow(2,P);)
			{	
				if( i==pow(2,level)*iter )
				{
					start= pow(2,level)*iter;
					iter++;
				}
				if( arr[i]> 0 )
				{
					for(int j=start; j< pow(2,level)*iter ; j++)
					{
						arr[j]--;
					}
					total++;
		//			cout<<i<<" "<<level<<" "<<iter<<endl;
					i= pow(2,level)*iter;
				}
				else
					i++;
			}
			
		//	for(int i=0;i<pow(2,P);i++)
		//		cout<<arr[i]<<" ";
		//	cout<<endl;

			level--;
		}
		cout<<"Case #"<<cp<<": "<<total<<endl;
	}
	return 0;
}
