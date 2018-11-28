#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

int x1[1000],y1[1000],x2[1000],y2[1000];
int n;

bool Left(int x1,int y1,int x2,int y2,int x3,int y3)
{
  return ((x2-x1)*(y3-y1) -(x3-x1)*(y2-y1)) > 0;
}

int main()
{
int tc;
cin >>tc;

for(int t=1;t<=tc;++t)
{
cin>>n;

for(int i=0;i<n;++i) {
	cin>>y1[i]>>y2[i];
	x1[i]=4;x2[i]=8;
}
int ans=0;
for(int i=0;i<n;++i)
	for(int j=i+1;j<n;++j) {
	  
	    bool l = Left(x1[i],y1[i],x2[i],y2[i],x1[j],y1[j]);
	    l = l ^ Left(x1[i],y1[i],x2[i],y2[i],x2[j],y2[j]);
	    
            bool r = Left(x1[j],y1[j],x2[j],y2[j],x1[i],y1[i]);
	    r = r ^ Left(x1[j],y1[j],x2[j],y2[j],x2[i],y2[i]);
	    if (l&&r) 
		++ans;
    }

cout<<"Case #"<<t<<": "<<ans<<endl;
}

}
