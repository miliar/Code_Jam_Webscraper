#include<iostream>
#define MAXR 51
#define MAXC 51
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
    	int r,c;
    	cin>>r>>c;
    	char grid[MAXR][MAXC];
    	
    	for(int i=0;i<r;i++)
    	{
    		cin>>grid[i];
    	}
    	
    	int i;
    	for(i=0;i<r;i++)
    	{
    		int j;
    		for(j=0;j<c;j++)
    		{
    			if(grid[i][j]=='#')
    			{
    				if(i<r-1 && j<c-1 && grid[i+1][j]=='#' && grid[i][j+1]=='#' && grid[i+1][j+1]=='#')
    				{
    					grid[i][j]='/';
    					grid[i][j+1]='\\';
    					grid[i+1][j]='\\';
    					grid[i+1][j+1]='/';
    				}
    				else
						break;
    			}
    		}
    		if(j!=c)
    			break;
    	}
    	cout<<"Case #"<<x<<":\n";
    	if(i!=r)
    		cout<<"Impossible\n";
    	else
    	{
    		for(int j=0;j<r;j++)
    		{
    			cout<<grid[j]<<endl;
    		}
    	}
    }
}
