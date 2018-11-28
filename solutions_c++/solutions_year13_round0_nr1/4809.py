#include<iostream>

using namespace std;

int t,draw,A[5][5],ans1,x;
char ch;

int main()
{
  cin>>t;
  
  for(int q=1;q<=t;q++)
  {
    draw=1;
    for(int i=1;i<=4;i++)
      for(int j=1;j<=4;j++)
      {
	cin>>ch;
	if(ch=='.')
	{
	  draw=0;
	  A[i][j]=0;
	}
	if(ch=='X')
	  A[i][j]=1;
	if(ch=='O')
	  A[i][j]=2;
	if(ch=='T')
	  A[i][j]=3;
      }
    ans1=-1;
      
    for(int i=1;i<=4;i++)
    {
      x=1;
      for(int j=1;j<=4;j++)
      {
	if((A[i][j]!=1)&&(A[i][j]!=3))
	  x=0;
      }
      if(x==1)
	ans1=1;
    }
    
    for(int i=1;i<=4;i++)
    {
      x=1;
      for(int j=1;j<=4;j++)
      {
	if((A[i][j]!=2)&&(A[i][j]!=3))
	  x=0;
      }
      if(x==1)
	ans1=2;
    }
    
    for(int i=1;i<=4;i++)
    {
      x=1;
      for(int j=1;j<=4;j++)
      {
	if((A[j][i]!=1)&&(A[j][i]!=3))
	  x=0;
      }
      if(x==1)
	ans1=1;
    }
    
    for(int i=1;i<=4;i++)
    {
      x=1;
      for(int j=1;j<=4;j++)
      {
	if((A[j][i]!=2)&&(A[j][i]!=3))
	  x=0;
      }
      if(x==1)
	ans1=2;
    }
    
    x=1;
    for(int i=1;i<=4;i++)
    {
	if((A[i][i]!=1)&&(A[i][i]!=3))
	  x=0;      
    }
    if(x==1)
	ans1=1;
    
    
    x=1;
    for(int i=1;i<=4;i++)
    {
	if((A[i][i]!=2)&&(A[i][i]!=3))
	  x=0;      
    }
    if(x==1)
	ans1=2;
    
    
    
    x=1;
    for(int i=1;i<=4;i++)
    {
	if((A[5-i][i]!=1)&&(A[5-i][i]!=3))
	  x=0;      
    }
    if(x==1)
	ans1=1;
    
    x=1;
    for(int i=1;i<=4;i++)
    {
	if((A[5-i][i]!=2)&&(A[5-i][i]!=3))
	  x=0;      
    }
    if(x==1)
	ans1=2;
    
    
    if(ans1==-1)
    {
      if(draw==1)
	ans1=0;
    }
    
    
    cout<<"Case #"<<q<<": ";
    if(ans1==-1)
      cout<<"Game has not completed\n";
    if(ans1==0)
      cout<<"Draw\n";
    if(ans1==1)
      cout<<"X won\n";
    if(ans1==2)
      cout<<"O won\n";
  }
}
    
    
    
      
      
      
      
    