#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

typedef long long LL;
typedef pair< int, int > PRII;
typedef pair< double ,double > PRDD;
typedef vector< string > VS;
typedef vector< int > VI;

#define Size(a) ((int)a.size())
#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))

#define x first
#define y second
#define p_b push_back
#define m_p make_pair
#define oo 1000000000
#define eps 1e-7
const double pi = acos(-1.0);

#define maxn 1000 + 10
#define dis(i,j) (sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j])))

int n;
double W,L,r[maxn],x[maxn],y[maxn],u[maxn][maxn],sum[maxn],total;

double calc( int j )
{
	int i;
	double s = 0,t;

	for( i = 1 ; i <= n ; ++i )
		if( i != j )
			{
				t = u[i][j];
				u[i][j] = u[j][i] = sqr(max(r[i]+r[j]-dis(i,j),0.0));
				sum[i] = sum[i]-t+u[i][j];
			}
	sum[j] = 0;
	for( i = 1 ; i <= n ; ++i )
		sum[j] += u[j][i];
	for( i = 1 ; i <= n ; ++i )
		s += sum[i];
	return s;
}

int main()
{
    int T,Test;
	int i,j,a,b;
	double dt,t,k;

//	srand((unsigned)time(NULL));
	freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    
	scanf("%d",&Test);
	for( T = 1 ; T <= Test ; ++T )
		{
			scanf("%d%lf%lf",&n,&W,&L);
			for( i = 1 ; i <= n ; ++i )
				scanf("%lf",&r[i]);
			do	{
					for( i = 1 ; i <= n ; ++i )
						{
							x[i] = fmod(rand()*rand(),W);
							y[i] = fmod(rand()*rand(),L);
						}
					total = 0;
					for( i = 1 ; i <= n ; ++i )
						{
							sum[i] = 0;
							for( j = 1 ; j <= n ; ++j )
								if( i != j )
									{
										u[i][j] = sqr(max(r[i]+r[j]-dis(i,j),0.0));
										sum[i] += u[i][j];
									}
							total += sum[i];
						}

					dt = (W+L)/2.0;
					for( a = 1 ; a <= 200 ; ++a, dt *= 0.8 )
						for( b = 1 ; b <= 300 ; ++b )
							{
								for( j = 1, i = 1 ; i <= n ; ++i )
									if( sum[i]/r[i]/r[i] > sum[j]/r[j]/r[j] )
										j = i;
								k = (double)rand()/(rand()+1);
								x[j] += dt*cos(k);
								y[j] += dt*sin(k);
								t = calc(j);
								if( x[j] >= 0 && x[j] <= W && y[j] >= 0 && y[j] <= L && t < total )
									total = t;
								else
									{
										x[j] -= dt*cos(k);
										y[j] -= dt*sin(k);
										calc(j);
									}
							}
				}while( total > eps );
			
			printf("Case #%d:",T);
			for( i = 1 ; i <= n ; ++i )
				printf(" %lf %lf",x[i],y[i]);
			printf("\n");
		}

    return 0;
}
