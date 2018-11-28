#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int mx(int a,int b)
{
	return a>b?a:b;
}
int main()
{
	//freopen("a.in","r",stdin);
	freopen("n.txt","w",stdout);
	int t1,t2;
	int o,b,t,i,k=0;
	int n,r,p,pos;
	char f;
	cin>>t;
	//cout<<t;
	while(t--)
	{
		k++;
		o=1,b=1;
		t1=0,t2=0;
		cin>>n;
		for(i=0;i<n;i++)
		{
            cin>>f>>pos;
			if(f=='O')
			{
				t1+=abs(pos-o);
				t1=mx(t1,t2)+1;
				o=pos;
			}
			else if(f=='B')
			{
				t2+=abs(pos-b);
            	t2=mx(t1,t2)+1;
				b=pos;
			}
		}	
		printf("Case #%d: ",k);
		cout<<mx(t1,t2)<<endl;
	}
	return 0;
}
