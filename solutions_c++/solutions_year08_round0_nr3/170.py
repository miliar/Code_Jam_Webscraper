#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
#define pi 3.14159265358

double f,R,v,r,g, s0, res, sx;
double get(double a, double b)
{
	return (b*sqrt(R*R-b*b)-a*sqrt(R*R-a*a)+R*R*(asin(b/R)-asin(a/R)))/2.0;
}
double s;
int proceed()
{
	int i, j, k=1, n, first=1;
	double cur=0.0, h1, h2, next, x;
	s=0.0;
	while(1)
	{
		if (k==1)
		{
			k=0;
			if (first)
			{
				first=0;
				s+=get(cur, min(cur+r, R));
				cur=cur+r;
			}
			else
			{
				s+=get(cur, min(cur+2.0*r, R));
				cur=cur+2.0*r;
			}
			if (cur>R)
				break;
		}
		else
		{
			k=1;
			double NEXT;
			next=min(R, cur+g);
			NEXT=next;
			h1=sqrt(R*R-cur*cur);
			h2=sqrt(R*R-next*next);
			if (h1<=r)
			{
				s+=get(cur, R);
				break;
			}

			if (h2<=r)
			{
				x=sqrt(R*R-r*r);
				s+=get(x, R);
				s+=(x-cur)*r;
				next=x;
			}
			else
				s+=g*r;
			int type;
			n=(int)((h1-r)/(g+2.0*r));
			double u, w;
			if (h1-(2.0*r+g)*(double)n-r>g)
			{
				type=1;
				w=min(next,sqrt(R*R-((2.0*r+g)*(double)n+r+g)*((2.0*r+g)*(double)n+r+g)));
			}
			else
			{
				type=0;
				w=min(next,sqrt(R*R-((2.0*r+g)*(double)n+r)*((2.0*r+g)*(double)n+r)));
			}
			u=cur;
			while(1)
			{
				if (type==0)
				{
					type=1;
					s+=(w-u)*2.0*r*(double)n;
					u=w;
					if (w>=next-1e-8)
						break;
					n--;
					w=min(next,sqrt(R*R-((2.0*r+g)*(double)(n)+r+g)*((2.0*r+g)*(double)(n)+r+g)));
				}
				else
				{
					type=0;
					s+=(get(u,w)-(w-u)*((2.0*r+g)*(double)(n)+g+r)+(w-u)*2.0*r*(double)(n));
					u=w;
					if (w>=next-1e-8)
						break;
					w=min(next,sqrt(R*R-((2.0*r+g)*(double)(n)+r)*((2.0*r+g)*(double)(n)+r)));
				}
			}


l2:;
			if (NEXT>next+1e-8)
				break;
			next=NEXT;
			cur=next;
			if (cur>R-1e-8)
				break;
		}
	}
	return 0;
}

int main()
{
	ifstream fin("a.in");
	freopen ("a.out","w",stdout);
	int i, j, n, k, l, m, t, T;
	fin>>T;
	for (t=1;t<=T;t++)
	{
		fin>>f>>R>>v>>r>>g;
		s0=pi*R*R;
		sx=s0;
		r+=f;
		R=R-v-f;
		g-=2.0*f;
		sx-=(pi*R*R);
		if (R<0 || g<0)
		{
			res=1;
			goto l1;
		}
		proceed();
		res=(sx+4.0*s)/s0;
l1:;
		printf ("Case #%d: %.6lf\n",t,res);
	}
	fin.close();
	return 0;
}