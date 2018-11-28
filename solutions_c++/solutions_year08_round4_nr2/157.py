#include <iostream>
#include <fstream>
using namespace std;
int n,m,tar;
struct point
{
	int x,y;
};

int main()
{
	int a,b,x,y,t,s,nn,ii,t1;
	ifstream cin("b-large.in");
	ofstream cout("b-large.out");
	point p1,p2,p3;
	cin >>nn;
	for (ii=1;ii<=nn;ii++)
	{
	cin >>n >>m >>tar;
	p1.x=-1;p1.y=-1;
	for (a=1;a<=m;a++)
	{
		t1=tar/a;
		for (b=t1;b<=n;b++)
		{
			for (x=0;x<=a;x++)
			{
				if (x==0)
				{
					if (a*b!=tar) continue;
					x=0;y=0;
					p1.x=0;p1.y=m;
					p2.x=y;p2.y=m-a;
					p3.x=b;p3.y=m-x;
					break;
				}
					
				t=a-x;
				s=(2*a*b-tar-b*x-b*t);
				if (s<0) continue;
				if (s%(a-t)==0)
				{
					if (x==0) y=0; else y=s/(a-t);
					p1.x=0;p1.y=m;
					p2.x=y;p2.y=m-a;
					p3.x=b;p3.y=m-x;
					break;
				}
			}
			if (p1.x>=0) break;
		}
	if (p1.x>=0) break;
	}
	cout <<"Case #" <<ii <<":";
	if (p1.x==-1) cout <<" IMPOSSIBLE" <<endl;
	else 
		cout <<" " <<p1.x <<" " <<p1.y <<" " <<p2.x <<" " <<p2.y <<" " <<p3.x <<" " <<p3.y <<endl;
	}
	return 0;
}


