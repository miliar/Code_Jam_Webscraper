#include <iostream>
#include <math.h>
using namespace std;
#define MAX(a,b) ((a)>(b)?(a):(b))
int main()
{
	int t;
	int n,r,p,c,i,j,ot,bt,op,bp;
	
	char b;
	cin>>t;
	for(c=1;c<=t;c++)
	{
		cin>>n;
		ot=bt=0;
		op=bp=1;
		for(i=0;i<n;i++)
		{
			cin>>b>>j;
			if(b=='O')
			{
				ot+=abs(op-j);
				if(ot<bt) ot=bt;
				ot++;op=j;
			}
			else if(b=='B')
			{
				bt+=abs(bp-j);
				if(bt<ot) bt=ot;
				bt++;bp=j;
			}
		}
		cout<<"Case #"<<c<<": "<<MAX(ot,bt)<<endl;
	}
}
