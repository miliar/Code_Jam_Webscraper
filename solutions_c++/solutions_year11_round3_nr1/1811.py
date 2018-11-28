#include<iostream>
using namespace std;
int main()
{
	int tc,tbc;
	cin>>tc;
	tbc=tc;
	while(tc--)
	{
		int r,c;
		cin>>r>>c;
		char arr[r][c];
		for(int i=0;i<r;i++)
			cin>>arr[i];

		//Check
		bool poss=true;
		for(int i=0;i<r && poss;i++)
		{
			int cnt=0;
			for(int j=0;j<c && poss;j++)
			{
				if(arr[i][j]=='#')cnt++;
			}
			if(cnt%2!=0) poss=false;
		}
		for(int j=0;j<c && poss;j++)
		{
			int cnt=0;
			for(int i=0;i<r && poss;i++)
			{
				if(arr[i][j]=='#')cnt++;
			}
			if(cnt%2!=0) poss=false;
		}		
		for(int i=0;i<r && poss;i++)
		{
			for(int j=0;j<c-1 && poss;j++)
			{
				if(arr[i][j]=='#')
				{
					if(arr[i][j+1]=='#')j++;
					else poss=false;
				}
			}
		}
		for(int j=0;j<c && poss;j++)
		{
			for(int i=0;i<r-1 && poss;i++)
			{
				if(arr[i][j]=='#')
				{
					if(arr[i+1][j]=='#')i++;
					else poss=false;
				}
			}
		}
		
		cout<<"Case #"<<tbc-tc<<":"<<endl;
		if(poss)
		{
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
				{
					if(arr[i][j]=='#')
					{
						arr[i][j]='/';
						arr[i][j+1]='\\';
						arr[i+1][j]='\\';
						arr[i+1][j+1]='/';
					}
				}
			}
			
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++) cout<<arr[i][j];
				cout<<endl;
			}
		}
		else
		{
			cout<<"Impossible"<<endl;
		}
	}
	return 0;
}
