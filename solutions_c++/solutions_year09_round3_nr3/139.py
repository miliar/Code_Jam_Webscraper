#include <iostream>
#include <fstream>

using namespace std;

ifstream ci("b3.in");
ofstream co("b3.out");

int T,p,q,a[100],b[100][100],c;

int get(int x,int y)
{
	int c=0,l=(x==0)?1:a[x-1]+1,r=(y==q-1)?p:a[y+1]-1,d;
	if (b[x][y]==-1)
	{
	if (x!=y)
	{
		c=get(x+1,y);
		for (int i=x+1;i<y;++i)
		{
			d=get(x,i-1)+get(i+1,y);
			if (d<c)
				c=d;
		}
		d=get(x,y-1);
		if (d<c)
			c=d;
	}
	b[x][y]=c+r-l;
	return c+r-l;
	}
	return b[x][y];
}

int main()
{
	ci>>T;
	for (int t1=0;t1<T;++t1)
	{
		ci>>p>>q;
		for (int i=0;i<q;++i)
		{
			ci>>a[i];
		}
		for (int i=0;i<q;++i)
			for (int j=0;j<q;++j)
				b[i][j]=-1;
		for (int i=0;i<q-1;++i)
			for (int j=i+1;j<q;++j)
				if (a[j]<a[i])
				{
					c=a[j];
					a[j]=a[i];
					a[i]=c;
				}
				co<<"Case #"<<t1+1<<": "<<get(0,q-1)<<endl;
	}
	return 0;
}