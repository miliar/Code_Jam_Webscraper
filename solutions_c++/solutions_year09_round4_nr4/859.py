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
using namespace std;
const double PI = acos(-1.0);
#define FOR(a,b) for(int i = a; i< b; ++i)
#define SORT(a,b) sort(a.begin(),a.end(),b)
#define MEMS(a,b) memset(a,b,sizeof(a))
template<class T>
inline T gcd(T a , T b) { if(a == 0 || b == 0 || a == b) return max(a,b); return a>b?gcd(a%b,b) : gcd(a,b%a);}
string intToStr(long long n) { char p[100];sprintf(p,"%lld",n);return string(p);}
int strToInt(string s) { istringstream sin(s); int r; sin >> r; return r;} 

struct Circle
{
	int x;
	int y;
	int r;
};

vector<Circle> All;
bool cmp(Circle a, Circle b)
{
	return a.r < b.r;
}
double dis(Circle a, Circle b)
{
	return sqrt(0.0+(a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y));
}
double chk(Circle a, Circle b, Circle c)
{
	return max(a.r+0.0,(dis(b,c)+b.r+c.r)/2);
}
int main()
{
	int S = 0;
	cin >> S;
	int n;
	for(int TT = 1; TT <= S ; ++TT)
	{
		cin >> n;
		Circle c;
		All.clear();
		for(int i = 0; i< n ; ++i)
		{
			cin >> c.x >> c.y >> c.r;
			All.push_back(c);
		}
		double ans = 0;
		if(n == 1) ans = All[0].r;
		else if(n == 2)
		{
			ans = max(All[0].r,All[1].r);
		}
		else 
		{
			ans = 10000000.0;
			//sort(All.begin(),All.end(),cmp);
			ans = min(ans,chk(All[0],All[1],All[2]));
			ans = min(ans,chk(All[1],All[2],All[0]));
			ans = min(ans,chk(All[2],All[1],All[0]));
		}
		printf("Case #%d: %.6lf\n",TT,ans);
	}
	return 0;
}