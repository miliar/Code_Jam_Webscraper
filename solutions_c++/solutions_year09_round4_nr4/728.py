#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <string>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)))
#define Out(x) (cout << #x << " = " << x << endl)

template<class T> inline T sqr(T x){return x*x;}
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T> inline void out(T x, int n){  for(int i = 0; i < n; ++i)  cout << x[i] <<" " ;    cout << endl;    }
template<class T> inline void out(T x, int n, int m){  for(int i = 0; i < n; ++i)    out(x[i], m);    cout << endl;    }
template<class T> inline void out(char * x) { for(int i =0;i< (int) strlen(x); i++)  cout << x[i] <<" " ;    cout << endl;  }


const double pi = acos(-1.0);
const double Eps = 1e-5;
const int INF = 0x7fffffff;

struct p
{
	double x;
	double y;
	double r;
}point[3];


double dist(double x1,double y1,double x2,double y2)
{
	return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

int main()
{
        freopen("D-small-attempt4.in","r",stdin);
		freopen("D-small-attempt4.out","w",stdout);

        //freopen("D-large.in","r",stdin);
        //freopen("D-large.out","w",stdout);

		int T;
		scanf("%d",&T);

		double R,R0,R1,R2,R3;
		double temp;
		int i;
		for(int cases =1 ; cases <= T;cases++)
		{

			int n;
			scanf("%d",&n);

			R=INF;
			R1=R2=R3=0;
			for(i=0;i<n;i++)
				scanf("%lf %lf %lf",&point[i].x,&point[i].y,&point[i].r);

			if(n==1)
				R=point[0].r;
			else if(n==2)
			{
				if(point[0].r>point[1].r)
                                        R=point[0].r;
                                else
                                        R=point[1].r;
			}
			else if(n==3)
			{
			     temp=(dist(point[0].x,point[0].y, point[1].x,point[1].y)+point[0].r+point[1].r)/2;
			     R0=point[2].r;
				checkmax(R1,temp);
				checkmax(R1,R0);

				 temp=(dist(point[0].x,point[0].y, point[2].x,point[2].y)+point[0].r+point[2].r)/2;
				 R0=point[1].r;
				checkmax(R2,temp);
				checkmax(R2,R0);

				 temp=(dist(point[2].x,point[2].y, point[1].x,point[1].y)+point[2].r+point[1].r)/2;
				 R0=point[0].r;
				checkmax(R3,temp);
				checkmax(R3,R0);

				//cout<<R1<<" "<<R2<<" "<<R3<<endl;
				checkmin(R,R1);
				checkmin(R,R2);
				checkmin(R,R3);
			}
			printf("Case #%d: %.6lf\n",cases,R);
		}
        return 0;
}
