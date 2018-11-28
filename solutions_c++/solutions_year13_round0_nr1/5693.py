#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <sstream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    
    long long n;
    cin>>n;
	
	for(int j=1;j<=n;j++)
	{
		vector<string> V;
		
		for(int k=0;k<4;k++)
		{
			string x;
			cin>>x;
			V.push_back(x); 
		}
		
		bool flag=false;
		
		for(int k=0;k<4;k++)
		{
			int cntX=0;int cntO=0;
			
			for(int i=0;i<4;i++)
			{
				if(V[k][i] == 'X') 
					cntX++;
				if(V[k][i] == 'O') 
					cntO++;
				if(V[k][i] == 'T')
				{
					cntX++;cntO++;
				}
			}
			
			if(cntX == 4) 
			{
				cout<<"Case #"<<j<<": X won"<<endl;
				 flag=true;
				break;
			}
			if(cntO == 4)
			{
				cout<<"Case #"<<j<<": O won"<<endl;
				flag=true;
				break;
			}
			
			cntX=0;cntO=0;
				
			for(int i=0;i<4;i++)
			{
				if(V[i][k] == 'X') 
					cntX++;
				if(V[i][k] == 'O') 
					cntO++;
				if(V[i][k] == 'T')
				{
					cntX++;cntO++;
				}
			}
			
			if(cntX == 4) 
			{
				cout<<"Case #"<<j<<": X won"<<endl;
				flag=true;
				break;
			}
			if(cntO == 4)
			{
				cout<<"Case #"<<j<<": O won"<<endl;
				flag=true;
				break;
			}
		}
		
			int cntX=0;int cntO=0;
			
			for(int k=0;k<4;k++)
			{
				if(V[k][k] == 'X')
					cntX++;
				if(V[k][k] == 'O')
					cntO++;
				if(V[k][k] == 'T')
				{
						cntX++;cntO++;
				}
			}
			
			if(cntX == 4) 
			{
				cout<<"Case #"<<j<<": X won"<<endl;
				flag=true;
			}
			if(cntO == 4)
			{
				cout<<"Case #"<<j<<": O won"<<endl;
				flag=true;
			}
			
			cntX=0;cntO=0;
			
			for(int k=0;k<4;k++)
			{
				if(V[k][3-k] == 'X')
					cntX++;
				if(V[k][3-k] == 'O')
					cntO++;
				if(V[k][3-k] == 'T')
				{
						cntX++;cntO++;
				}
			}
			
			if(cntX == 4) 
			{
				cout<<"Case #"<<j<<": X won"<<endl;
				flag=true;
			}
			if(cntO == 4)
			{
				cout<<"Case #"<<j<<": O won"<<endl;
				flag=true;
			}	
			
			if(!flag)
			{
				int cntdot=0;
				
				for(int k=0;k<4;k++)
				{
					for(int i=0;i<4;i++)
					{
						if(V[k][i] == '.') cntdot++;
					}
				}
				
				if(cntdot > 0)
					cout<<"Case #"<<j<<": Game has not completed"<<endl;
				else
					cout<<"Case #"<<j<<": Draw"<<endl;
			}	   
	}
    return 0;
}
