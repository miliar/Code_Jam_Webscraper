#include<iostream>

using namespace std;

int main(void)
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int r,c;
		cin>>r>>c;
		char mat[r][c];
	
		for(int j=0;j<r;j++)
			for(int k=0;k<c;k++)
				cin>>mat[j][k];
	
		int rem=0;
		for(int j=0;j<r;j++)
		{
			for(int k=0;k<c;k++)
			{
				if(mat[j][k]=='#')
				{
					if(mat[j][k+1]=='#' && mat[j+1][k]=='#' && mat[j+1][k+1]=='#')
					{
						mat[j][k]='/';
						mat[j+1][k+1]='/';
						mat[j][k+1]=(char)92;
						mat[j+1][k]=(char)92;
					}
					else
					{
						rem=1;
						break;
					}
				}
			}
		
			if(rem==1)
				break;
		}
		
		if(rem==1)
			cout<<"Case #"<<i+1<<":"<<endl<<"Impossible"<<endl;
		
		else 
		{
			cout<<"Case #"<<i+1<<":"<<endl;
			for(int j=0;j<r;j++)
			{
				for(int k=0;k<c;k++)
					cout<<mat[j][k];
				cout<<endl;
			}
		}
	}
	
	return 0;
}