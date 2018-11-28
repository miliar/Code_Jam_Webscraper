#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <deque>
#include <cstring>
#include <cstdio>
#include <vector>
#include<cmath>

using namespace std;
 
 
int main()
{
freopen("C-small-attempt1.in","r",stdin);
freopen("output.txt","w",stdout);
	int t;
cin>>t;
for(int x=1;x<=t;x++)
{
int a,b, c,d,f; int e; int g,re;
int y=0;
	cin>>a>>b;
	c=a;
	while(c!=0)
	{c=c/10;
	 y++;
	}re=0;int ret=0;

	for(;a<b;a++)
	{               
                                
		d=a;e=0;
		for(;e<y;e++)
		{	f=d%10;
			g=d/10;
			double h=f*pow(10,y-1)+g; int rr=(int)h;
			if(h>a && h<=b)
			{ret++;}//cout<<a<<" "<<h<<endl;}
			d=(int)h;
		}
	}

	cout<<"Case #"<<x<<": "<<ret<<endl;
}
return 0;
}