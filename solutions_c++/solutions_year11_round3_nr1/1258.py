#include<iostream>
using namespace std;

int main()
{	
	int t,r,c,flag=1;
	char grid[50][50];
	cin>>t;
	
	for(int tc=1; tc<=t; tc++)
 	{  
 	    cin>>r;
 	    cin>>c;
 	    flag=1;
 	    
		for(int i=0;i<r;i++)
 	      for(int j=0;j<c;j++)
 	         cin>>grid[i][j];
     
       for(int i=0;i<r;i++)
 	      for(int j=0;j<c;j++)
 	      {
	   		  if(grid[i][j]=='#')
	   		  {
			      if(grid[i][j+1]=='#' && grid[i+1][j]=='#' && grid[i+1][j+1]=='#')
		   		  {
					 grid[i][j]='/';
					 grid[i][j+1]='\\';
					 grid[i+1][j]='\\';
					 grid[i+1][j+1]='/';
		          }
			  	  else
			  	      flag=0;
			  }	 
          }  
	   
	   cout<<"Case #"<<tc<<":"<<endl;
	   
	   if(flag==0)
		  cout<<"Impossible"<<endl;
       else
       {	
          for(int i=0;i<r;i++)
 	      {
   		      for(int j=0;j<c;j++)
 	             cout<<grid[i][j];
	   	      cout<<endl;
		   }
	   }
	   	   	   
	}
	  	   
	//system("pause");
 	return 0;
}
