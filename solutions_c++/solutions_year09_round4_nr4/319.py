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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
bool mp[41][41];
int N;
#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
int x[41];
int y[41];
int r[41];
double square(int x) {return (double)x*x;}
double getDistance(int x1,int y1,int x2,int y2)
{
	return sqrt(square(x1-x2)+square(y1-y2));
}
int main()
{
	int tc;
	cin>>tc;int cs=0;
	while(tc--) {
		++cs;
		int n;
		cin>>n;
		fir(i,0,n) cin>>x[i]>>y[i]>>r[i];
		double ans=1e20;
		if (n<3)
		{
			ans=0;
			fir(i,0,n) ans=max(ans,(double)r[i]);
		}
		else
		fir(i,0,3) fir(j,i+1,3) {
			double dst=getDistance(x[i],y[i],x[j],y[j]);
			dst+=r[i]+r[j];
			dst/=2.0;
			fir(k,0,3) if (k!=i && k!=j) dst=max(dst,(double)r[k]);
			ans=min(ans,dst);
		}
		printf("Case #%d: %.7lf\n",cs,ans);
	}
	return 0;
}