#include <iostream>

#include <algorithm>
#include <string>
#include <stack>
#include <deque>
#include <cstring>
#include <cstdio>
#include <vector>
 
using namespace std;
 
 
int main()
{
       freopen("B-small-attempt0.in","r",stdin);
       freopen("outpu.txt","w",stdout);
 
        int cas;
cin>>cas;
int q,s,p;
for(int num=1;num<=cas;num++)
{int in[100];
cin>>q>>s>>p;
for(int a=0;a<q;a++)
cin>>in[a];
int ret=0;
if(p==0)
ret=q;
else
for(int ind =0;ind<q;ind++)
	{	
		if(in[ind]<1)in[ind]=-10;in[ind]-=p;in[ind]/=2;
		if(p-in[ind]<=1)
		ret++;
		else
		if(p-in[ind]<=2 && s>0)
		{s--;ret++;}
	}
cout<<"Case #"<<num<<": "<<ret<<endl; 
}
return 0;
};