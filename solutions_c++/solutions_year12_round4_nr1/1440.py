#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>


using namespace std;

int t,n,D[100000],L[100000],des,A[10005][10005],ans,d;

int main()
{
  cin>>t;
  
  for(int q=1;q<=t;q++)
  {
    cin>>n;
    for(int i=1;i<=n;i++)
    {
      cin>>D[i];
      cin>>L[i];
    }
    
    cin>>des;
    
    for(int i=1;i<=n;i++)
      for(int j=1;j<=n;j++)
      {
	A[i][j]=-1;
      }
     L[1]=D[1];
    
    ans=-1;

      if((2*D[1])>=des)
      {
	ans=1;
      }
      
      
      
      else

      {
	ans=-1;

    for(int i=n-1;i>=1;i--)
    {
      for(int j=i+1;j<=n;j++)
      {
	if(L[i]<(D[j]-D[i]))
	{
	  break;
	}
	
	
	d=D[j]-D[i];
	
	
	if(L[j]<(D[j]-D[i]))
	{
	  d=L[j];
	}
	
	if(d+D[j]>=des)
	{
	  A[i][j]=1;	
	  continue;
	}
	
	for(int k=j+1;k<=n;k++)
	{
	  if((D[k]-D[j])>d)
	    break;
	  if(A[j][k]==1)
	  {
	    A[i][j]=1;
	    break;
	  }
	}
      }
    }
    
    for(int i=2;i<=n;i++)
    {
      if((D[i]-D[1])>D[1])
	break;
      if(A[1][i]==1)
      {
	ans=1;
	break;
      }
    
    
     }
      }
      
      cout<<"Case #"<<q<<": ";
      if(ans==1)
	cout<<"YES\n";
      else
	cout<<"NO\n";
  }
}
	  
	
	
	
    
    
  