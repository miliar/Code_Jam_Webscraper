#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	char a[4][4];
	int i,j,c,b,d,e,x,k,p,t,l=1;
freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	std:cin>>t;
	while(l<=t)
	{
	x=0;b=0;c=0;d=0;e=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
cin>>a[i][j];
		}
	}
		cout<<"Case #"<<l<<":";
	for(i=0;i<4;i++)
	{
	b=0;c=0;d=0;
		for(j=0;j<4;j++)
		{
			if(a[i][j]=='X')
				b++;
			else if(a[i][j]=='O')
				c++;
			else if(a[i][j]=='T')
				d++;
			else if(a[i][j]=='.')
				e++;
		}
		if((b==3&&d==1)||(b==4&&d==0))
		{
			cout<<" X won\n";
			b=0,c=0,d=0;
			x=1;
			break;
		}
		if((c==3&&d==1)||(c==4&&d==0))
		{
			cout<<" O won\n";
			b=0,c=0,d=0;
			x=1;
			break;

		}
		if(x!=1)
		{
			b=0,c=0,d=0;
			p=i;
			for(k=0;k<4;k++)
			{
				if(a[k][p]=='X')
					b++;
				else if(a[k][p]=='O')
					c++;
				else if(a[k][p]=='T')
					d++;
				else if(a[k][p]=='.')
					e++;
			}
			if((b==3&&d==1)||(b==4&&d==0))
			{
				cout<<" X won\n";
				b=0,c=0,d=0;
				x=1;
				break;

			}
			if((c==3&&d==1)||(c==4&&d==0))
			{
				cout<<" O won\n";
				b=0,c=0,d=0;
				x=1;
				break;

			}
		}
	}
	if(x!=1)
	{
		b=0,c=0,d=0;
		i=0,j=0;
		while(i<4)
		{

				if(a[i][j]=='X')
					b++;
				else if(a[i][j]=='O')
					c++;
				else if(a[i][j]=='T')
					d++;
				else if(a[i][j]=='.')
					e++;
					j=++i;
			}
		if((b==3&&d==1)||(b==4&&d==0))
		{
			cout<<" X won\n";
			b=0,c=0,d=0;
			x=1;

		}
		if((c==3&&d==1)||(c==4&&d==0))
		{
			cout<<" O won\n";
			b=0,c=0,d=0;
			x=1;

		}
	}
	if(x!=1)
	{
		b=0,c=0,d=0;
		for(i=0;i<4;i++)
		{
		for(j=0;j<4;j++)
		{
		if((i+j)==3)
		{
				if(a[i][j]=='X')
					b++;
				else if(a[i][j]=='O')
					c++;
				else if(a[i][j]=='T')
					d++;
				else if(a[i][j]=='.')
				e++;
				}
			}
			}
		if((b==3&&d==1)||(b==4&&d==0))
		{
			cout<<" X won\n";
			b=0,c=0,d=0;
			x=1;
		}
		if((c==3&&d==1)||(c==4&&d==0))
		{
			cout<<" O won\n";
			b=0,c=0,d=0;
			x=1;
		}
	}
	if(x==0&&e==0)
	{
	cout<<" Draw\n";
	}
	else if(x==0&&e>0)
	cout<<" Game has not completed\n";
	++l;
	}
	return 0;
}


