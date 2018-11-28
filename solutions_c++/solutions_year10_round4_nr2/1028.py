#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>

using namespace std;

int main()
{
  int noCase,cases;
  int m[2<<10];
int temp;
 long int np;

  cin>>cases;
  for(noCase=1;noCase<=cases;noCase++)
    {
      int p;
      cin>>p;
      np=0;
      //memset(,0,sizeof(int)*(2<<p));
      for(long int i=0;i<(1<<p);i++)
	{cin>>m[i];
	  //	  cout<<m[i]<<endl;
	}
      for(int i=0;i<p;i++)
	{
	  for(long int j=0;j<(1<<(p-i-1));j++)
	    {  cin>>temp;
	      //      cout<<"junk data : "<<temp<<endl;
	    }
	}
      for(int i=1;i<=p;i++)
	{
	  for(long int j=0;j<(1<<(p-i));j++)
	    {
	      bool flag=true;
	      for(long int k=(1<<i)*j;k<(1<<i)*(j+1) && flag;k++)
		{if(m[k]<i)
		    flag=false;
		}
	      np+=flag;
	    }
	}
      //cout<<"not playing "<<np<<endl;
      cout<<"Case #"<<noCase<<": "<<(1<<p)-np-1<<endl;
    }
  
}
