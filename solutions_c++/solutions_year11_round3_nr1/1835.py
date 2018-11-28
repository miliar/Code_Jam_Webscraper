#include <iostream>

using namespace std;

int main()
{
	int t,r,c;
	char pic[50][50];
	int i,j;
	int testCase=1;
	int flag=0;
	cin>>t;
	while(t--)
	{
		flag=0;
		cin>>r>>c;

		for(i=0;i<r;i++)
			for(j=0;j<c;j++)
				cin>>pic[i][j];

		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(pic[i][j]== '#' && pic[i][j+1]== '#' && pic[i+1][j]== '#' && pic[i+1][j+1]== '#')
				{
					pic[i][j]='/';
					pic[i+1][j+1]='/';
					pic[i][j+1]='\\';
					pic[i+1][j]='\\';				}
			}
		}

/*		for(i=0;i<r;i++){
			for(j=0;j<c;j++)
			cout<<pic[i][j];
		cout<<endl;}*/

		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(pic[i][j]=='#')
				{
					cout<<"Case #"<<testCase++<<":"<<endl<<"Impossible"<<endl;
					flag=1;
					break;
				}
			}
			if(flag==1) break;
		}
		if(flag==1) continue;
		cout<<"Case #"<<testCase++<<":"<<endl;
		for(i=0;i<r;i++){
			for(j=0;j<c;j++)
			cout<<pic[i][j];
		cout<<endl;
		}
	}
	return 0;
}
