#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>

#define ll long long

using namespace std;

struct Point{
	Point(int _x =0,int _y = 0) : x(_x), y(_y) {};
	int x,y;
};

vector <Point> up,down;
int W,L,U,G,x,y;
const double eps=1e-8;

double S(vector <Point> & p,double l)
{
	double s=0;
	for(int i=1;i<p.size();i++)
	{
		if (l<p[i].x)
		{
			double cy=p[i-1].y+1.0*(p[i].y-p[i-1].y)/(p[i].x-p[i-1].x)*(l-p[i-1].x);
			s+=0.5*(p[i-1].y+cy)*(l-p[i-1].x);
			break;
		}
		else
			s+=0.5*(p[i-1].y+p[i].y)*(p[i].x-p[i-1].x);
	}
	return s;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int TT=1;TT<=T;++TT)
	{
		printf("Case #%d:\n",TT);
		scanf("%d%d%d%d",&W,&L,&U,&G);
		up.clear(); down.clear();
		for(int i=0;i<L;i++)
		{
			scanf("%d%d",&x,&y);
			down.push_back(Point(x,y+1005));
		}
		for(int i=0;i<U;i++)
		{
			scanf("%d%d",&x,&y);
			up.push_back(Point(x,y+1005));
		}
		double tot=S(up,W)-S(down,W),one=tot/G;
//		cout << tot << endl;
//		cout << S(up,5)-S(down,5) << endl;
		double last=0,cs=one;
		for(int i=0;i<G-1;i++)
		{
			double l=last,r=W;
			for(int t=0;t<100;t++)
			{
				double m=(l+r)/2;
				double val=S(up,m)-S(down,m);
				if (val<cs) l=m;
				else r=m;
			}
			last=(l+r)/2;
			printf("%.7lf\n",last);
			cs+=one;
		}
	}
	return 0;
}
