#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

const int nmax = 205;
int lx[nmax], ly[nmax], ux[nmax], uy[nmax];
pair<int, pii> t[nmax];
double tx[nmax], tu[nmax], tl[nmax], tb[nmax];

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		int w, L, U, g;
		scanf("%d%d%d%d", &w, &L, &U, &g);
		for(int i=0;i<L;i++)
		{
			scanf("%d%d", lx+i, ly+i);
		}
		for(int i=0;i<U;i++)
		{
			scanf("%d%d", ux+i, uy+i);
		}
		printf("Case #%d:\n",test_case);

		int k=0;
		for(int i=0, j=0; i<L && j<U; k++)
		{
			if(lx[i] == ux[j])
			{
				tx[k] = lx[i];
				tl[k] = ly[i++];
				tu[k] = uy[j++];
			}
			else if(lx[i] < ux[j])
			{
				tx[k] = lx[i];
				tl[k] = ly[i++];
				tu[k] = uy[j-1] + (double)(uy[j] - uy[j-1]) / (ux[j] - ux[j-1]) * (tx[k] - ux[j-1]);
			}
			else
			{
				tx[k] = ux[j];
				tu[k] = uy[j++];
				tl[k] = ly[i-1] + (double)(ly[i] - ly[i-1]) / (lx[i] - lx[i-1]) * (tx[k] - lx[i-1]);
			}
			tb[k] = tu[k] - tl[k];
		}
		//for(int i=0; i<k; i++)			printf("%lf %lf %lf\n", tx[i], tu[i], tl[i]);
		double A=0;
		for(int i=1; i<k; i++)
			A += (tb[i] + tb[i-1])/2*(tx[i] - tx[i-1]);
		//printf("%lf\n", A);
		A /= g;
		double ap = 0, ac = 0;
		for(int i=1; i<k && g>1; i++)
		{
			ac = ap + (tb[i] + tb[i-1])/2*(tx[i] - tx[i-1]);
			while(ac >= A && g>1)
			{
				double a = A - ap;
				double b1 = tb[i-1], b2 = tb[i], h = tx[i] - tx[i-1];
				double d;
				if(b1 == b2)
					d = a/b2;
				else
				{
					double s1 = b1*h / (b1-b2);
					double s2 = sqrt(h*(-2*a*b1+2*a*b2+b1*b1*h)) / (b1-b2);
					d = s1 - s2;
					if(d < 0)
						d = s1 + s2;
				}
				double x = tx[i-1] + d;
				printf("%.6lf\n", x);
				//printf("  %lf %lf\n", d, (b1+(b2-b1)*d/h)/2*d);
				ap = 0;
				ac -= A;
				tx[i-1] = x;
				tb[i-1] = b1 + (b2-b1)*d/h;
				g--;
			}
			ap = ac;
			//printf("%lf\n", ap);
		}
    }
    return 0;
}
