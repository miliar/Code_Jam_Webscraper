#include <iostream>

using namespace std;

#define fi(n) for (int i=0;i<n;i++)
#define fj(n) for (int j=0;j<n;j++)

struct pt{int x,y;};

int main()
{
	int c;
	cin>>c;
	for (int xx=0;xx<c;xx++)
	{
		int m,n,a;
		cin>>m>>n>>a;
		pt px[3000];int u=0;
		fi(m+1)fj(n+1)
		{
			px[u].x=i;
			px[u].y=j;
			u++;
		}
		bool xd=1;
		if (a<=2600)
		//fi(u)
		{
			for (int j=0;j<u;j++)
				for (int k=0;k<u;k++)
				{
					int x1=0;
					int x2=px[j].x;
					int x3=px[k].x;
					int y1=0;
					int y2=px[j].y;
					int y3=px[k].y;
					if (abs(x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)==a)
					{
						cout<<"Case #"<<xx+1<<": "<<x1<<' '<<y1<<' '
						<<x2<<' '<<y2<<' '<<x3<<' '<<y3<<endl;
						j=k=99999;xd=0;
					}
				}
			//cout<<i<<endl;
		}
		if (xd)
		cout<<"Case #"<<xx+1<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}