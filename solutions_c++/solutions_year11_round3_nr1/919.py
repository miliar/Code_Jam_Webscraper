#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cctype>
#include <cstring>
#include <cmath>

#include <vector>

#include <queue>
#include <stack>

#include <algorithm>

using namespace std;

int main()
{
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-out.txt","w",stdout);
	freopen("A-large(1).in","r",stdin); freopen("A-large-out.txt","w",stdout);
	
	int t,k;
	
	int r,c,i,j,okay;
	
	char mat[100][100];
	
	cin>>t;
		
	for(k=1;k<=t;k++)
	{
		cin>>r>>c;
		
		
		for(i=0;i<r;i++)
			cin>>mat[i];
			
		for(i=0;i<(r-1);i++)
		{
			for(j=0;j<(c-1);j++)
			{
				if(mat[i][j]=='#' && mat[i+1][j]=='#' && mat[i][j+1]=='#' && mat[i+1][j+1]=='#')
				{
					mat[i][j]='/';
					mat[i][j+1]='\\';
					mat[i+1][j]='\\';
					mat[i+1][j+1]='/';
				}
			}
		}
		
		okay=1;
		
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			 if(mat[i][j]=='#') 
			 {
				 okay=0;
				 break;
			 }
		 }
		 
		 cout<<"Case #"<<k<<":"<<endl;
		 
		 if(okay==0) cout<<"Impossible"<<endl;
		 else
		 {
			 for(i=0;i<r;i++)
			 {
				for(j=0;j<c;j++) cout<<mat[i][j];
				
				cout<<endl;
			}
		 }
		
		
	}

	return 0;
}





