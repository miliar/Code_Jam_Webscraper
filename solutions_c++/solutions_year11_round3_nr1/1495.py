// 1.cpp : Defines the entry point for the console application.
//


#include <iostream>
using namespace std;
	int n_row,n_col;
	char s[50][50];
bool fill(int i, int j,char ch)
{
	if(i>=n_row||j>=n_col) return false;
	if(s[i][j]=='#')
	{
		s[i][j]=ch;
		return true;
	}	
	else
	 return false;
}
bool isvalidandfill(int i, int j)
{
	return fill(i,j,'/')&&fill(i,j+1,'\\')&&fill(i+1,j,'\\')&&fill(i+1,j+1,'/');
}
void solve()
{
	int i,j;
	cin>>n_row;
	cin>>n_col;
	for(i=0;i<n_row;i++)
	{
		cin>>s[i];
	}
	for(i=0;i<n_row;i++)
	{
		for(j=0;j<n_col;j++)
		{
			if(s[i][j]=='#')
			{
				if(!(isvalidandfill(i,j)))
				{
					cout<<"Impossible\n";
					return;
				}
			}
		}
	}
	for(i=0;i<n_row;i++)
	{
		for(j=0;j<n_col;j++)
		{
			cout<<s[i][j];
		}
		cout<<"\n";
	}
}
int main(int argc, char* argv[])
{
	int num_test;
	cin>>num_test;
	for(int i=0;i<num_test;i++)
	{
		cout<<"Case #"<<i+1<<":\n";
		solve();
	}
		
	return 0;
}