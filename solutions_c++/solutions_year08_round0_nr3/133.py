#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
 
using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a)) 

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}

#define PI 3.1415926535897932384626433832795

bool IsIn(double x, double y, double r)
{
	return (x*x + y*y <= r*r);
}

double cross(double x1, double y1, double x2, double y2)
{
	return x1*y2 - x2*y1;
}

double scalar(double x1, double y1, double x2, double y2)
{
	return x1*x2 + y1*y2;
}

double seg_area(double x1, double y1, double x2, double y2, double r)
{
	double phi = 0.0;
	double c = cross(x1, y1, x2, y2);
	double s = scalar(x1, y1, x2, y2);
	if (fabs(s) < 1e-9)
		phi = PI*0.5*(c > 0.0 ? 1.0 : -1.0);
	else
	{
		phi = atan(c / s);
		if (s < 0.0)
			phi *= (c >= 0.0 ? 1.0 : -1.0)*PI;
	}
	phi = fabs(phi);
	double ret = 0.5 * phi * r*r - 0.5 * fabs(c);
	return ret;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	cin>>N;
	REP(test, N)
	{
		double f, R, t, g, r;
		cin>>f>>R>>t>>r>>g;


		double area = 0.0;
		double total = PI * R * R / 4.0;

		g -= 2*f;
		if (g < 0.0)
			g = 0.0;
		R -= (t + f);
		if (R < 0.0)
			R = 0.0;

		for (double y = r+f; y < R; y += (g + 2*r + 2*f))
			for (double x = r+f; x*x + y*y < R*R; x += (g + 2*r + 2*f))
			{
				double nx = x + g, ny = y + g;
				if (IsIn(nx, ny , R))
				{
					area += g*g;
					continue;
				}

				double lx = x, ly = ny;
				double rx = nx, ry = y;
			
				double fl = IsIn(lx, ly, R);
				double fr = IsIn(rx, ry, R);
				double fn = IsIn(nx, ny, R);


				if (fl && fr)
				{
					double tx = sqrt(R*R - ny*ny);
					double ty = sqrt(R*R - nx*nx);
					area += (nx - x)*(ty - y) + (ny - ty)*(tx - x) + 0.5*(ny - ty)*(nx - tx);
					area += seg_area(tx, ny, nx, ty, R);
					continue;
				}

				if (fl && !fr)
				{
					double tx1 = sqrt(R*R - ny*ny);
					double tx2 = sqrt(R*R - y*y);
					area += (ny - y)*(tx1 - x) + 0.5*(ny - y)*(tx2 - tx1);
					area += seg_area(tx1, ny, tx2, y, R);
					continue;
				}

				if (!fl && fr)
				{
					double ty1 = sqrt(R*R - x*x);
					double ty2 = sqrt(R*R - nx*nx);
					area += (nx - x)*(ty2 - y) + 0.5*(nx - x)*(ty1 - ty2);
					area += seg_area(x, ty1, nx, ty2, R);
					continue;
				}

				if (!fl && !fr)
				{
					double ty = sqrt(R*R - x*x);
					double tx = sqrt(R*R - y*y);
					area += 0.5*(ty - y)*(tx - x);
					area += seg_area(x, ty, tx, y, R);
					continue;
				}

			}

		
		double res = 1.0 - area / total;
		printf("Case #%d: %.6f\n", test+1, res);
	}
	return 0;
}