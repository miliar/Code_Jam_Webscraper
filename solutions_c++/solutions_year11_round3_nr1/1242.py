#include<iostream>
using namespace std;
int main()
{
	int note;
	cin>>note;
	for(int caseno=1;caseno<=note;caseno++)
	{
		cout<<"Case #"<<caseno<<":"<<endl;
	char arr[100][100];
	int r,c;
	cin>>r>>c;
	int count=0;
	for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
		{	cin>>arr[i][j];if(arr[i][j]=='#')count++;}
	for(int i=1;i<=r;i++)
		for(int j=1;j<=c;j++)
		{
			if(i+1<=r&&j+1<=c)
				if(arr[i][j]=='#'&&arr[i][j+1]=='#'&&arr[i+1][j]=='#'&&arr[i+1][j+1]=='#')
				{
					arr[i][j]='/';
					arr[i+1][j]='\\';
					arr[i][j+1]='\\';
					arr[i+1][j+1]='/';
					count-=4;
				}
		}
        if(count!=0)
		cout<<"Impossible"<<endl;
	else
	{
		for(int i=1;i<=r;i++)
		{
			
			for(int j=1;j<=c;j++)
				cout<<arr[i][j];
			cout<<endl;
		}
		
	}
}
}
