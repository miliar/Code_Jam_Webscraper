//a=o..... b=b;;;
#include<iostream>
using namespace std;
int mod(int m)
{
	if(m<0)
	{
		return (0-m);
	}
	else
		return m;
}
int main()
{
	int t,c=1,i,n;
	cin>>t;
	while(t)
	{
		t--;
		cin>>n;
		int button_o=0,button_b=0,time=0;
	//	char ch;
		int p=n+1;
		int b[p],o[p];
		char a[p];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			if(a[i]=='O')
			{
				cin>>o[button_o];
				button_o++;
			}
			else
			{
				cin>>b[button_b];
				button_b++;
			}
		}
		o[button_o]=o[button_o-1];
		b[button_b]=b[button_b-1];
		int o_pos=1,b_pos=1,oc=0,bc=0;
		for(i=0;i<n;i++)
		{
			int x,y;
			if(a[i]=='O')
			{
				x=mod(o[oc]-o_pos);
				o_pos=o[oc];
				x++;
				time=time+x;
				oc++;
				y=b[bc]-b_pos;
				if(x>mod(y))
				{
					b_pos=b[bc];
				}
				else
				{
					b_pos=b_pos+((y/mod(y))*x);
				}
			}
			else
			{
				x=mod(b[bc]-b_pos);
				b_pos=b[bc];
				x++;
				time=time+x;
				bc++;
				y=o[oc]-o_pos;
				if(x>=mod(y))
				{
					o_pos=o[oc];
				}
				else
				{
					o_pos=o_pos+((y/mod(y))*x);
				}
			}
		}
		cout<<"Case #"<<c<<": "<<time<<"\n";
		c++;
	}
	return 0;
}