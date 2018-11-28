//////////////////////////
// Author:
// Date:
// Title:
// Function:
//////////////////////////
#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

#define xin fin
#define xout fout
#define f(i,a,b) for (i=a;i<=b;i++)
struct P
{
	int a,b;
};

bool cmp(P a, P b)
{
	return a.a < b.a;
};
int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");
	register int z,i,j;
	int s,n,t,aa,bb,h;
	P p[1001];
	xin >> t;

	f(z,1,t)
	{
		xin >> n;
		//memset(b,0,sizeof(b));
		h = 0;
		f(i,0,n-1)
		{
			xin >> aa >> bb;
			//b[bb] = true;
			p[i].a = aa;
			p[i].b = bb;

		}
		sort(p,p+n,cmp);
		s = 0;
		f(i,0,n-1)
		{
			f(j,0,i-1)
			{
				if (p[i].b < p[j].b)
				{
					s++;
				}
			}
		}
		xout << "Case #" << z << ": " << s << endl;
	}
	return 0;
}
