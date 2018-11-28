#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <math.h>

using namespace std;
int row,col;
char ar[102][102];
char arr[102][102];
int i,ii;
int ncase;
int blue,red;
int t,k;
int x;
char c;

int check (char c,int x, int y, int incx, int incy)
{
  //cout<<c<<" "<<x<<" "<<y<<" "<<incx<<" "<<incy;
  int num = 1;
  int cur = 1;
  int i,ii;
  i = x+incx;
  ii = y + incy;
  while (i<=t && cur < k && ii<=t && i>0 & ii>0)
  {
    if (arr[i][ii]==c)
	{
	  num++;
	}
	else
	{
	  //cout<<"returning 1 - "<<i<<","<<ii<<" "<<cur<<num<<endl;
	  return 1;
	}
	i+=incx;
	ii+=incy;
	cur++;
  }  
  if (num==k) 
  {
    if (c=='R')
	{ 
	  //cout<<"returning -1"<<endl;
	  return -1;
	}
	else
	{
	  //cout<<"returning -2"<<endl;
	  return -2;
	}
  }
  else
  {
    //cout<<"returning 1 : "<<num<<endl;
	return 1;
  }
}

int main()
{
  cin>>ncase;
  for (int p=1;p<=ncase;p++)
  {
    for (i=0;i<=t+1;i++)
	{
	  for (ii=0;ii<=t+1;ii++)
	  {
	    ar[i][ii]='.';
	  }
	}
    blue = 0;
	red = 0;
    //sult = 1;
    cin>>t>>k;
	for (i = 1;i<=t;i++)
	{
	x = t;
	  for (ii=1;ii<=t;ii++)
	  {
	    cin>>c;

		if (c!='.')
		{
		  x--;
		  for (int iii=x;iii<=t;iii++)
		  {
		    ar[i][iii]=ar[i][iii+1];
		  }
		  ar[i][t]=c;
		}
	  }
	}
	
	for (i=1;i<=t;i++)
	{
	  for (ii=1;ii<=t;ii++)
	  {
	    if (ar[i][ii]!='R' && ar[i][ii]!='B') { ar[i][ii]='.';}
	    arr[ii][t-i+1] = ar[i][ii];
	  }
	}
	
	for (i=1;i<=t;i++)
	{
	  for (ii=1;ii<=t;ii++)
	  {
	    if (arr[i][ii]=='R'||arr[i][ii]=='B') 
		{
		  if (arr[i-1][ii-1]!=arr[i][ii]) 
		  {
		    if (check(arr[i][ii],i,ii,1,1)==-1)
			{ 
			  red = 1;
			}
			if (check(arr[i][ii],i,ii,1,1)==-2)
			{ 
			  blue = 1;
			}
		  }
		  if (arr[i-1][ii+1]!=arr[i][ii]) 
		  {
		    if (check(arr[i][ii],i,ii,1,-1)==-1)
			{
			  red = 1;
			}
			if (check(arr[i][ii],i,ii,1,-1)==-2)
			{
			  blue = 1;
			}
		  }
		  if (arr[i][ii-1]!=arr[i][ii]) 
		  {
		    if (check(arr[i][ii],i,ii,0,1)==-1)
			{
			  red = 1;
			}
			if (check(arr[i][ii],i,ii,0,1)==-2)
			{
			  blue = 1;
			}
			
		  }
		  if (arr[i-1][ii]!=arr[i][ii]) 
		  {
		    if (check(arr[i][ii],i,ii,1,0)==-1)
			{
			  red = 1;
			}
			if (check(arr[i][ii],i,ii,1,0)==-2)
			{
			  blue=1;
			}
		  }
		}
	  }
	}
	cout<<"Case #"<<p<<": ";
	if (red==1&&blue==1)
	{
	  cout<<"Both"<<endl;
	}
	else if (red==0&&blue==0)
	{ 
	  cout<<"Neither"<<endl;
	}
	else if (red==1&&blue==0)
	{
	  cout<<"Red"<<endl;
	}
	else if (red==0&&blue==1)
	{
	  cout<<"Blue"<<endl;
	}
  }
/*
  for (i=1;i<=t;i++)
	{
	  for (ii=1;ii<=t;ii++)
	  {
	    cout<<arr[i][ii];
	  }
	  cout<<endl;
	}
*/
  return 0;
}
