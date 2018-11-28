#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<climits>
#include<utility>
#include<cstdlib>
#include<cstring>
using namespace std;
int main()
{
	int t, nu=1;
	scanf("%d", &t);
	while(nu<=t)
	{
		char arr[4][4];
		int  extra[4][2]={0};
		//for(int i=0 ; i<4 ; i++)
		//{
		//	for(int j=0 ; j<1 ;j++)
		
//		extra[0][4]={0 , 0 , 0 , 0};
//		extra[1][4]={0 , 0 , 0 , 0};
		char ans;
		int flag=0;
		int  countdot=0;
		for(int i=0 ; i<4; i++)
		{
			int sum1=0, sum2=0, count=0, set=0, flag1=0 , flag2=0 ;
			for(int j=0 ; j<4 ; j++)
			{
				cin>>arr[i][j];
				if(arr[i][j]=='O')
				{
					extra[j][0]=extra[j][0]+1;
					flag1=1;
				//	sum1=sum1+extra[i][0];
				}
				else if(arr[i][j]=='X')
				{
					extra[j][1]=extra[j][1]+1;
					flag2=1;
				//	sum=sum+extra[i][0];
				}
				else if(arr[i][j]=='T')
				{
						extra[j][0]=extra[j][0]+1;
						extra[j][1]=extra[j][1]+1;
						//count++;
			//			sum=sum+extra[i];
				}
				else
				{
					countdot++;
					set=1;
				}
			}
			if( (flag1==0|| flag2==0 ) && set==0)
			{
				//cout<<"ENTER COLOUMN"<<"\n";

				if(flag1==1 && flag2==0 )
				{
					ans='O';
					flag=1;
					for(int p=i+1 ; p<4 ; p++)
					{
						for(int q=0 ; q<4 ; q++)
						{
							cin>>arr[p][q];
						}
					}
					break;
				}
				else if(flag2==1 && flag1==0 )
				{
					flag=1;	
					ans='X';
					for(int p=i+1 ; p<4 ; p++)
					{
						for(int q=0 ; q<4 ; q++)
						{
							cin>>arr[p][q];
						}
					}
					break;
				}
			}
		}			
		if(flag==1)
		{
			//cout<<ans<<"\n";
			cout<<"Case #"<<nu<<": "<<ans<<" won"<<"\n";
		}
		else
		{
		//	cin>>nu;
			for(int p=0 ; p<4 ; p++)
		/*	{
				cout<<extra[p][0];
				cout<<extra[p][1];
			}*/
			//cout<<extra[3][0]<<extra[3][1]<<"\n";
			for(int i=0 ; i<4 ; i++)
			{
				if(extra[i][0]==4)
				{
					ans='O';
					flag=1;
					break;
				}
				if(extra[i][1]==4)
				{
					ans='X';
					flag=1;
					break;
				}

			}
		
			if(flag==1)
			{		
		//		cin>>nu;
			//	cout<<"ENTER ROW";
				cout<<"Case #"<<nu<<": "<<ans<<" won"<<"\n";
			}
			else
			{
		//		cin>>nu;
				int count1=0, count2=0;
			//	char m=arr[0][0];
				for(int i=0 ; i<4 ; i++)
				{
					if(arr[i][i]=='O')
						count1++;
					else if(arr[i][i]=='X')
						count2++;
					else if(arr[i][i]=='T')
					{
						count1++;count2++;
					}	
				}
				if(count1==4)
				{
			//		cout<<"ENTER DIAG1"<<"\n";
					cout<<"Case #"<<nu<<": O won"<<"\n";
				}
				else if(count2==4)
				{
					cout<<"Case #"<<nu<<": X won"<<"\n";
				}
				else
				{
				//	m=arr[3][0];
					count1=0, count2=0;
					for(int i=0 ; i<4 ; i++)
					{
						if(arr[i][3-i]=='O')
							count1++;
						else if(arr[i][3-i]=='X')
							count2++;
						else if(arr[i][3-i]=='T')
						{
							count1++;count2++;
						}
					}		
					
					if(count1==4)
					{
			//			cout<<"ENTER DIAG2"<<"\n";
						cout<<"Case #"<<nu<<": "<<"O won"<<"\n";
					}
					else if(count2==4)
					{
			//			cout<<"ENTER DIAG2"<<"\n";
						cout<<"Case #"<<nu<<": X won"<<"\n";
					}
					else
					{
			//			cout<<"ENTER DIAG2"<<"\n";
						if(countdot==0)
						cout<<"Case #"<<nu<<": Draw"<<"\n";
						else
						cout<<"Case #"<<nu<<": Game has not completed"<<"\n";
					}
				}
			}
		}	
		nu++;
	}
	return 0;
}
