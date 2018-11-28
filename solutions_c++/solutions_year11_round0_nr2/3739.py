#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std;

int T,N,C,D;
char arr[200];
int idx=0;
char cb[20][4];
char dp[20][3];
int main()
{
  freopen("in.txt","r",stdin);
  cin>>T;
  for(int caseid = 1;caseid <=T;++caseid)
  {
    cin>>C;
    for(int i=0;i<C;++i)
    {
      cin>>cb[i];
    }
    cin>>D;
    for(int i=0;i<D;++i)
    {
      cin>>dp[i];
    }
    cin>>N;
    cin>>arr;
    for(int i=1;i<N;++i)
    {
      if(C==1)
      {
	if((arr[i]==cb[0][1]&&arr[i-1]==cb[0][0])||(arr[i]==cb[0][0]&&arr[i-1]==cb[0][1]))
	{
	  arr[i-1]=' ';
	  arr[i]=cb[0][2];
	  continue;
	}
      }
      if(D==1)
      {
	if(arr[i]==dp[0][0])
	{
	  char ot = dp[0][1];
	  for(int j=0;j<i;++j)
	    if(ot==arr[j])
	    {
	      for(int k=0;k<=i;++k)
		arr[k]=' ';
	      break;
	    }
	}
	else if(arr[i]==dp[0][1])
	{
	  char ot = dp[0][0];
	  for(int j=0;j<i;++j)
	    if(ot==arr[j])
	    {
	      for(int k=0;k<=i;++k)
		arr[k]=' ';
	      break;
	    }
	}
      }
      
    }
    
    cout<<"Case #"<<caseid<<": [";
    int fst=1;
    for(int i=0;i<N;++i)
    {
      if(arr[i]!=' ')
      {
	if(fst)
	  cout<<arr[i],fst=0;
	else 
	  cout<<", "<<arr[i];
      }
    }
    cout<<"]"<<endl;
  }
  
  
}
