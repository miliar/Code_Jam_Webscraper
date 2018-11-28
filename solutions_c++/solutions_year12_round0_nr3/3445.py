#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main () 
{   
	int a,b;
	char buffer[4],buffer1[4];
	long sum,product,sum1,product1;
	int test,ans=0,k=1;
	cin>>test;
	while(test--)
	{  ans = 0;
	   cin>>a>>b;
	   int temp[1000] = {0};
	   
	  for(int i=a;i<=b;i++)
	  {   
			//if(temp[i]==0)
			
		itoa(i,buffer,10);
		for(int j = i+1;j <= b;j++)
		{
			itoa(j,buffer1,10);
			if(strlen(buffer)==strlen(buffer1))
			{    //cout<<"dsf";
				if(strlen(buffer)==3)
				{ 
					if((buffer[2]==buffer1[0] && buffer[1]==buffer1[2] &&  buffer[0] == buffer1[1]) || (buffer[1] == buffer1[0] && buffer[0] == buffer1[2] && buffer[2] == buffer1[1] ))
				 { ans++;
				  temp[j] = 1;
				  //temp[i] = 1;
				  }
				}
				else
				if(strlen(buffer)==2)
				{  
					if (buffer[1] == buffer1[0] && buffer[0]==buffer1[1])
					{
						ans++;
				        temp[j] = 1;
				        //temp[i] = 1;
					}
				  }
				else 
				if(strlen(buffer)==1)
				{
					ans=0;
				    temp[j] = 1;
				    //temp[i] = 1;
				}
			}
		}
      }
    printf("Case #%d: %d\n",k,ans);
	k++; 
   }
   
	system("pause");
  return 0;
}
