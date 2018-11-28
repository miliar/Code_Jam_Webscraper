#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

int T,R,C;
char cake[64][64];

int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int t;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		
		cout<<"Case #"<<t<<": "<<endl;
		cin>>R>>C;
		int i,j;
		string str;
		for(i=0;i<R;++i)
		{
			cin>>cake[i];
		}
		while(true)
		{
			bool found=false;
			for(i=0;i<R-1;++i)
			{
				for(j=0;j<C-1;++j)
				{
					if(cake[i][j]=='#'&&cake[i][j+1]=='#'
						&& cake[i+1][j]=='#' && cake[i+1][j+1]=='#')
					{
						found=true;
						break;
					}
				}
				if(found) break;
			}
			if(!found) break;
			cake[i][j]='/';
			cake[i][j+1]='\\';
			cake[i+1][j]='\\';
			cake[i+1][j+1]='/';
		}
		bool ok=true;
		for(i=0;i<R;++i)
			for(j=0;j<C;++j)
				if(cake[i][j]=='#')
				{
					ok=false;
					break;
				}
		if(ok)
		{
			for(i=0;i<R;++i)
			{
				for(j=0;j<C;++j)
					cout<<cake[i][j];
				cout<<endl;
			}
		}
		else cout<<"Impossible"<<endl;

	}

	return 0;
}
