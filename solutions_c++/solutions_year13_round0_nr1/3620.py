#include<stdio.h>

int main()
{
  char board[5][5];
  int n=4;
  int t,i,j;
  int rowx=0,rowo=0,count=0;
  bool x=false,y=false,full=false;
  
  FILE* fin=fopen("in.txt","r");
  FILE* fout=fopen("out.txt","w");
  
  fscanf(fin,"%d",&t);
  
  while(t--)
  {
    count++;
    x=false,y=false,full=false;
    
    for(i=0;i<n;i++)
      fscanf(fin,"%s",board[i]);
    
    //row wise check
    
    for(i=0;i<n;i++)
    {
      rowx=0,rowo=0;
      for(j=0;j<n;j++)
      {
	if(board[i][j]=='.')
	  break;
	
	if(board[i][j]=='X')
	  rowx++;
	
	else if(board[i][j]=='O')
	  rowo++;
	
	else
	{
	  rowx++;
	  rowo++;
	}
      }
      
      if(rowx==4)
      {
	x=true;
	break;
      }
      
      else if(rowo==4)
      {
	y=true;
	break;
      }
    }
    
    
    //column wise check
    
    if(x==false&&y==false)
    {
      for(i=0;i<n;i++)
      {
	  rowx=0,rowo=0;
	
	  for(j=0;j<n;j++)
	  {
	  if(board[j][i]=='.')
	    break;
	  
	  if(board[j][i]=='X')
	    rowx++;
	  
	  else if(board[j][i]=='O')
	    rowo++;
	  
	  else
	  {
	    rowx++;
	    rowo++;
	  }
	}
      
	if(rowx==4)
	{
	  x=true;
	  break;
	}
	
	else if(rowo==4)
	{
	  y=true;
	  break;
	}
      }
    }
    
    //on-diagonal check
    
    if(x==false&&y==false)
    {
	rowx=0,rowo=0;
	
	for(i=0;i<n;i++)
	{
	  if(board[i][i]=='.')
	    continue;
	  
	  else if(board[i][i]=='X')
	    rowx++;
	  
	  else if(board[i][i]=='O')
	    rowo++;
	  
	  else
	  {
	    rowx++;
	    rowo++;
	  }
	}
	
	if(rowx==4)
	  x=true;
	else if(rowo==4)
	  y=true;
    }
    
    //off-diagonal check
    
    if(x==false&&y==false)
    {
	rowx=0,rowo=0;
	
	for(i=0;i<n;i++)
	{
	  if(board[i][3-i]=='.')
	    continue;
	  
	  else if(board[i][3-i]=='X')
	    rowx++;
	  
	  else if(board[i][3-i]=='O')
	    rowo++;
	  
	  else
	  {
	    rowx++;
	    rowo++;
	  }
	}
	
	if(rowx==4)
	  x=true;
	else if(rowo==4)
	  y=true;
    }
    
    
    
    //none of x or y has won
    if(x==false&&y==false)
    {
      full=true;
      
      for(i=0;i<n;i++)
      {
	for(j=0;j<n;j++)
	{
	  if(board[i][j]=='.')
	  {
	    full=false;
	    break;
	  }
	}
      }
    }
    
    if(x==true)
      fprintf(fout,"Case #%d: X won\n",count);
    
    else if(y==true)
      fprintf(fout,"Case #%d: O won\n",count);
    
    else if(full==true)
      fprintf(fout,"Case #%d: Draw\n",count);
    
    else
      fprintf(fout,"Case #%d: Game has not completed\n",count);
  }
  
  return 0;
}
	    
	  
	
	
	
    
    
    
    
