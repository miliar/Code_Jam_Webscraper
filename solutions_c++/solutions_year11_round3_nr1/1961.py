#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;

int main()
{
	int t,r,c,iter=1,i,j,flag = 1;
	char pic[100][100];
	ifstream ifile ("smallB.txt");
	ofstream cout ("output.txt");
	ifile>>t;
	while(t)
	{
		pic[0][0] = '\0';
		flag = 1;		
		ifile>>r;
		ifile>>c;
		for(i=0;i<r+1;i++)
        	{  for(j=0;j<c+1;j++)
		    { 
			pic[i][j]='-';
		    }
		}
		for(i=0;i<r;i++)
        	{  for(j=0;j<c;j++)
		    { 
			ifile>>pic[i][j];
		    }
		}
		
		for(i=0;i<(r);i++)
           	{
		  for(j=0;j<(c);j++)
		  {
			if(pic[i][j]=='#'&& pic[i+1][j+1]=='#' && pic[i+1][j]=='#' && pic[i][j+1] =='#')
			{
			  
				pic[i][j] = pic[i+1][j+1] = '/';
				pic[i+1][j] = pic[i][j+1] = '\\';
			 
			}
			else if(pic[i][j] == '#')
			{
				flag = 0;				
				
			}
		  }
		}
		cout<<"Case #"<<iter<<":\n";
		if(flag==0)
		{
			cout<< "Impossible\n";
		}
		else
		{
		for(i=0;i<r;i++)
        	 { for(j=0;j<c;j++)
		    {
			cout<<pic[i][j];
		    }
			cout<<"\n";
		}
		}
		iter++;
		t--;
	}
	return 0;
}

