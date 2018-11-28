#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <iomanip>

using namespace std;

const double eps = 1e-8;

const int MAXN = 205;
const int MAXP = 1000005;

struct node
{
	int x , y;
}data[MAXN];
int n,d,sum,Case,T;
long double pos[MAXP];
bool cmp(node a,node b) 
{  
	return a.x < b.x;  
}

long double getmin(long double a ,long double b)
{
	return a < b ? a : b;  
}

void init() 
{
	cin >> n >> d;
	sum = 0;
	for(int i = 0;i < n;i++)
	{
		cin >> data[i].x >> data[i].y;
		sum += data[i].y;
	}
	sort(data,data+n,cmp);
}

bool check(long double ans) {
	int t = 0;
	for (int i = 0;i < n;i++)
	{
		for (int j = 1;j <= data[i].y;j++ )
		{
			pos[t++] = data[i].x;
		}
	}
	pos[0] -= ans;
	for(int i = 1;i < t;i++) 
	{
		if (pos[i-1] < pos[i]) {
			if ( pos[i] - pos[i-1] >= d ) pos[i] -= getmin( ans , pos[i]-pos[i-1]-d );
			else {
				if ( pos[i] + ans - pos[i-1] >= d ) pos[i] = pos[i-1] + d;
				else return 0;
			}
		} else {
			if ( pos[i] + ans - pos[i-1] >= d ) pos[i] = pos[i-1] + d;
			else return 0;
		}
	}
	return 1;
}

void solve() 
{
	long double l = 0,r = d * 1.0 * sum;
	while (r - l > eps)
	{
		long double mid = (l+r) / 2.0;
		if (check(mid)) r = mid;
		else l = mid;
	}
	cout << "Case #" << ++Case << ": " << fixed << setprecision(10) << l << endl;
}

int main() 
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	cin >> T;
	while (T--)
	{
		init();
		solve();
	}
	return 0;
}
