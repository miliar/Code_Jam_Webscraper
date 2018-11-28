#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

ifstream fin("atc");
#define cin fin

void stuff()
{
	int i,j,N,M,R,C;
	char m[100][100];
	int res[100][100]={0};
	vector<int> v;
	set<int> s;
	cin>>R>>C;
	for(i=0;i<R;i++)
		for(j=0;j<C;j++)
			cin>>m[i][j];
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)
		{
			if(m[i][j]=='#')
			{
				if(i==R-1 || j==C-1 || m[i+1][j]!='#' || m[i+1][j+1]!='#' || m[i][j+1]!='#')
				{
					cout<<endl<<"Impossible"<<endl;;
					return;
				}
				m[i][j]='/';
				m[i][j+1]='\\';
				m[i+1][j]='\\';
				m[i+1][j+1]='/';
			}
		}
	}	
	cout<<endl;
	for(i=0;i<R;i++)
	{
		for(j=0;j<C;j++)
			cout<<m[i][j];
		cout<<endl;
	}

}

int main(void)
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		stuff();
	}
}
