#define forn(i, n) for(int i = 0; i<(int) n; i++)
#define ford(i, n) for(int i = (int)n -1; i>=0 ; i--)
#define pb push_back 
#define mp make_pair
#define se second
#define fi first
#define ll long long
#define PI 	3.14159265358979323846264338327950288

#include <vector>
#include <list>
#include <map>
#include <set>
//#include <multiset>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define sss 2000000
using namespace std;
 long long mm[sss+10];
 //pair<int,int> cell[1010];
 int goat[2][2];
 int q[20][2];
 double dist(int x1, int y1, int x2, int y2){
	return sqrt((x1-x2+0.0)*(x1-x2+0.0)+(y1-y2+0.0)*(y1-y2));
}
 int t, n, m;
 double ans[12];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	forn(tn, t)
	{
		scanf("%d", &n);	
		scanf("%d", &m);	
		forn(i, 2)
			forn(j, 2)
				scanf("%d", &goat[i][j]);
		forn(i, m)
			forn(j, 2)
				scanf("%d", &q[i][j]);
		double d = dist(goat[0][0], goat[0][1],goat[1][0], goat[1][1]);
		forn(i, m)
		{
			double r0 = dist(goat[0][0],goat[0][1], q[i][0], q[i][1]);
			double r1 = dist(goat[1][0],goat[1][1], q[i][0], q[i][1]);
			double d0d1 = (r0*r0-r1*r1)/d;
			double d0 = (d0d1+d)/2;
			double d1 = (-d0d1+d)/2;
			double ssum = 0;
			double m2 = sqrt((d0+r0)*(r0-d0));
			double t0 = 2* acos(d0/r0);
			double t1 = 2* acos(d1/r1);
			//cerr<<ssum<<endl;
			ssum += r0*r0*0.5 * (t0-sin(t0));
			ssum += r1*r1*0.5 * (t1-sin(t1));
			ans[i] = ssum;
		}
		
		printf("Case #%d: ", tn+1);
		forn(i, m)
			printf("%.12lf ", ans[i]);
		printf("\n");
	}
	return 0;
}
