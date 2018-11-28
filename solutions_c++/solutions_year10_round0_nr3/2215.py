#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int main()
{
  int i,t;
  cin>>t;
  
  for(i=0;i<t;i++)
  {
    int r,k,n,j,m;
    int size,temp,temp1,euros=0;
    queue<int> g;
    
    cin>>r>>k>>n;
    
    for(j=0;j<n;j++)
    {
      cin>>temp;
      g.push(temp);
    }
   
    for(j=0;j<r;j++)
    {
      size=0;
      
      for(m=0;m<n;m++)
      {
	temp1=g.front();
	
	if(size+temp1<=k)
	{size+=temp1;
	
	g.pop();
	g.push (temp1);}
	
	else
	  break;
	}
      euros+=size;
    }
  
  cout<<"Case #"<<i+1<<": ";
  cout<<euros<<"\n";
  }
  
 return 0;
}