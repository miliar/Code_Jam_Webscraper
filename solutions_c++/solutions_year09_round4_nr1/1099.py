#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <ctime>

using namespace std;


int c[41],N;   

int done()
{
for(int i=0;i<N;++i)
    if (c[i]>i) return 0;
return 1;
}

int main()
{
int T;
char str[1000];
cin.getline(str,1000);
sscanf(str,"%d",&T);


for(int tc=1;tc<=T;++tc)
{
   
cin.getline(str,1000);	
sscanf(str,"%d",&N);
   for(int i=0;i<N;++i)
   {
	cin.getline(str,1000);
        int z=0;
	for(int j=N-1;j>=0;--j)
		if (str[j]=='0') ++z;
		else break;
        c[i]=N-z-1; 
     //   cout<<c[i]<<endl; 		
   }	
   int ans=0;
  if (!done())  {
  	for(int i=0;i<N;++i)
  	{
		if (c[i]>i) {
		 //  cout<<"===="<<c[i]<<' '<<i<<endl;
			int j=i;
			for(int k=j+1;k<N;++k)
			{  
			  // cout<<"=j"<<j<<' '<<c[k]<<endl;
			   if (c[k]<=j) {	
				while(k-1>=j)
					{++ans;swap(c[k],c[k-1]);--k;}
			    break;
			    }
			}
		}
	  if (done()) break;
	}
  }
   cout<<"Case #"<<tc<<": "<<ans<<endl;
}

}
