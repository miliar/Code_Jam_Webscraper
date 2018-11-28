#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
	int tc, r, c;
	string b[55];
	cin>>tc;
	for(int T=1; T<=tc; T++)
	{
		cin>>r>>c;
		for(int i=0; i<r; i++)
			cin>>b[i];
		
		bool pos = true;
		for(int i=0; (i<r) && pos; i++)
			for(int j=0; j<c; j++)
			{
				if(b[i][j]!='#')
					continue;
				if( i+1<r && j+1<c && b[i+1][j]=='#' && b[i][j+1]=='#' && b[i+1][j+1]=='#' )
				{
					b[i][j]='/'; b[i][j+1]='\\';
					b[i+1][j]='\\'; b[i+1][j+1]='/';
				}
				else
				{
					pos = false;
					break;
				}
			}

		cout<<"Case #"<<T<<":"<<endl;
		if(!pos)
			cout<<"Impossible"<<endl;
		else
		{
			for(int i=0; i<r; i++)
				cout<<b[i]<<endl;
		}
	}
	return 0;
}
