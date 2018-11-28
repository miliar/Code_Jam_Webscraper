#include<iostream>
#include<string>

using namespace std;

int r,c;
string m[51];

bool solve()
{
	for(int i=0;i<r;i++)for(int j=0;j<c;j++)
	{
		if(m[i][j]=='#')
		{
			if(i+1>=r||j+1>=c)return false;
			if(m[i+1][j]!='#'||m[i][j+1]!='#'||m[i+1][j+1]!='#')return false;
			m[i][j]='/';
			m[i][j+1]='\\';
			m[i+1][j]='\\';
			m[i+1][j+1]='/';
		}
	}
	return true;
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>r>>c;
		for(int j=0;j<r;j++)
			cin>>m[j];
		cout<<"Case #"<<i+1<<':'<<endl;
		if(solve())
		{
			for(int i=0;i<r;i++)
			{
				cout<<m[i]<<endl;
			}
		}else{
			cout<<"Impossible\n";
		}
	}
	return 0;
}
