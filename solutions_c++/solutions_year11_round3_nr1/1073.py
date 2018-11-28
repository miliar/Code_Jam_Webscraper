#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<climits>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int numCase=1;numCase<=cases;numCase++)
	{
		int r,c;
		cin>>r>>c;
		char **a=new char*[sizeof(char*)*r];
		for(int i=0;i<r;i++)
			a[i]=new char[sizeof(char)*c];

		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
				cin>>a[i][j];
		
		for(int i=0;i<r;i++)
			for(int j=0;j<c;j++)
			{
				if(a[i][j]=='#')
				{
					int count=1;
					if((i+1)<r && a[i+1][j]=='#')
						count++;
					if((j+1)<c && a[i][j+1]=='#')
						count++;
					if((i+1)<r  && (j+1)<c&& a[i+1][j+1]=='#')
						count++;

					if(count==4)
						{
							a[i][j]='/';
							a[i+1][j]='\\';
							a[i][j+1]='\\';
							a[i+1][j+1]='/';
						}
				}
			}
		
		
		cout<<"Case #"<<numCase<<": "<<endl;
		int found=0;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
				if(a[i][j]=='#')
				{
					found=1;
					break;
				}
			if(found==1)
				break;
		}
		if(found==1)
			cout<<"Impossible"<<endl;
		else
		{
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
					cout<<a[i][j];
				cout<<endl;
			}
		}
				
	}
	return 0;
}
