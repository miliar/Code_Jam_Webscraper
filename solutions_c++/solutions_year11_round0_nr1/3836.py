#include <iostream>
#include <stdio.h>
using namespace std;

struct ab
{
	int x;
	char b;
}a[100];

int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("1.out","w",stdout);
    int t,i=1;
    cin>>t;
    while(t--)
    {
    	int n,j,B=1,O=1,p=0,q=0,min=0,b[100]={0},o[100]={0},mb,mo,sb=0,so=0;
    	cin>>n;
    	for(j=0;j<n;j++)
    	{
    		cin>>a[j].b>>a[j].x;
    		if(a[j].b=='B')
    		b[p++]=a[j].x;
    		else
    		o[q++]=a[j].x;
    	}
    	for(j=0;j<n;j++)
    	{
    		if(a[j].b=='B')
    		{
    			if(B<b[sb])
    			mb=1;
    			else
    			mb=-1;
    			if(O<o[so])
    			mo=1;
    			else
    			mo=-1;
    			for(;B!=b[sb];B+=mb)
    			{
    				min++;
    				if(O!=o[so])
    				O+=mo;
    			}
    			min++;
    			if(O!=o[so])
    			O+=mo;
    			sb++;
    		}
    		else if(a[j].b=='O')
    		{
    			if(B<b[sb])
    			mb=1;
    			else
    			mb=-1;
    			if(O<o[so])
    			mo=1;
    			else
    			mo=-1;
    			for(;O!=o[so];O+=mo)
    			{
    				min++;
    				if(B!=b[sb])
    				B+=mb;
    			}
    			min++;
    			if(B!=b[sb])
    			B+=mb;
    			so++;
    		}
    	}
    	cout<<"Case #"<<i++<<": "<<min<<endl;
    }
    return 0;
}