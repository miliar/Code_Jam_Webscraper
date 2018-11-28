#include<iostream>
#include<iomanip>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;
#define PII pair<double, double>
PII Q[111];
int N, M;
PII goats[110];
#define PI 3.141592653
double getdist(PII A, PII B)
{
	return sqrt((A.first-B.first)*(A.first-B.first) + (A.second-B.second)*(A.second-B.second));
}

double foo(int off)
{
	PII A = goats[0], B = goats[1];
	PII D = Q[off];
	double c = getdist(A, B);
	double r0 = getdist(A, D);
	double r1 = getdist(B, D);
	if(c - 1e-7 < 0)
	{
		return PI * r0 * r0;
	}
	double coscba = (r1*r1 + c*c - r0*r0)/(2*r1*c);
	double cba = acos(coscba);
	double cbd = 2*cba;
	double coscab = (r0*r0+c*c-r1*r1)/(2*r0*c);
	double cab = acos(coscab);
	double cad = 2*cab;

	double area = 0.5*cbd*r1*r1 - 0.5*r1*r1*sin(cbd)+0.5*cad*r0*r0 - 0.5*r0*r0*sin(cad);
	return area;
}
void solve()
{
	int i, j, k;
	for(i = 0; i < M; i++)
	{
		double ar = foo(i);
		cout<<setprecision(20)<<ar<<" ";
	}
	cout<<endl;
}
int main()
{
	int tes;
	cin >> tes;
	int tesnum=0;
	while(tes--)
	{
		tesnum++;
		int i, j, k;
		cin >> N >> M;
		for(i = 0; i < N; i++)
		{
			double a, b;
			cin >> a >> b;
			goats[i].first = a;goats[i].second=b;
		}
		for(i = 0; i < M; i++)
		{
			double a, b;
			cin >> a >> b;
			Q[i].first = a;Q[i].second=b;
		}
		printf("Case #%d: ", tesnum);
		solve();
	}
	return 0;
}
