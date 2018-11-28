#include <iostream>

using namespace std;

int main()
{
  int caseNo,n,k,cases;
  char board[50][50],temp,board2[50][50];
  cin>>cases;
  for(caseNo=1;caseNo<=cases;caseNo++)
    {
      cin>>n>>k;
      for(int i=0;i<n;i++)      
	{
	  cin>>board2[i];
	}
      for(int i=0;i<n;i++)
	{
	  for(int j=0;j<n;j++)
	    {
	      board[j][n-i-1]=board2[i][j];
	    }
	}

      for(int i=0;i<n;i++)
	{
	  int pointer=n,j;
	  for(j=n-1;j>=0;j--)
	    {
	      for(pointer--;pointer>=0;pointer--)
		if(board[pointer][i]=='R'||board[pointer][i]=='B') break;
	      if(pointer>=0)
		{if(pointer!=j)
		    {board[j][i]=board[pointer][i];
		      board[pointer][i]='.';}}
	      else break;
	    }
	  for(;j>=0;j--)
	    board[j][i]='.';
	}
      //rotation finished
      //horizondal
      bool red=false,blue=false;
      
      for(int i=0;i<n;i++)
	{
	  int count=1;
	  char value=board[i][0];
	  for(int j=1;j<n;j++)
	    {if(board[i][j]==value)
		count++;
	      else 		{
		  count=1;
		  value=board[i][j];
	      }
	      if(count==k)
	      {
		 if(value=='R'){ red=true;}
		 else if(value=='B') blue=true;
	      }
		
	    }
	}
      for(int i=0;i<n;i++)
	{
	  int count=1;
	  char value=board[0][i];
	  for(int j=1;j<n;j++)
	    {if(board[j][i]==value)
		count++;
	      else 
		{
		  count=1;
		  value=board[j][i];
		}
	      if(count==k)
		{ if(value=='R') {red=true;}
		  else if(value=='B') blue=true;
		}
		
	    }
	}
       for(int i=0;i<=n-k;i++)
	{
	  for(int j=0;j<=n-k;j++)
	    {int l;
	      for(l=1;l<k ;l++)
		if(board[i][j]!=board[i+l][j+l]) break;
	      if(l>=k)
		{if(board[i][j]=='R') {red=true;}
		  else if(board[i][j]=='B') blue=true;
		}
	    }
	}
      for(int i=0;i<=n-k;i++)
	{
	  for(int j=k-1;j<n;j++)
	    {int l;
	      for(l=1;l<k;l++)
		if(board[i][j]!=board[i+l][j-l]) break; 
	      if(l>=k)
		{if(board[i][j]=='R') {red=true;}
		  else if(board[i][j]=='B') blue=true;
		}
	    }
	}
      cout<<"Case #"<<caseNo<<": ";
      if(red && blue)
	cout<<"Both"<<endl;
      else if(red)
	cout<<"Red"<<endl;
      else if(blue)
	cout<<"Blue"<<endl;
      else cout<<"Neither"<<endl;


      
    }
}
