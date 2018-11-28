#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int maxn = 1005;
struct Node 
{
	int x , v;
	double t;
} number[maxn];
int n , x , s , r , t;

void init() 
{
	memset(number , 0 , sizeof(number));
	scanf( "%d%d%d%d%d" , &x , &s , &r , &t , &n );
	for (int i = 0; i < n; i++ )
	{
		int st , ed;
		scanf( "%d%d%d" , &st , &ed , &number[i].v );
		number[i].v += s;
		number[i].x = ed - st;
		x -= ed - st;
	}
	number[n].v = s;
	number[n++].x = x;
}

bool cmp(Node a , Node b) 
{  
	if ( a.v != b.v ) return a.v < b.v;
	else return a.x < b.x;
}

void solve( int Case ) 
{
	sort( number,number+n,cmp);
	double MAXVALUE = t;
	int i = 0;
	while(MAXVALUE > 0 &&i < n)
	{
		if (double(number[i].x)/double(number[i].v+r-s) <= MAXVALUE ) {
			MAXVALUE -= double(number[i].x)/double(number[i].v+r-s);
			number[i].t += double(number[i].x)/double(number[i].v+r-s);
			i++;
		} else
		{
			number[i].t += MAXVALUE;
			MAXVALUE = 0;
		}
	}
	double ans = 0;
	for (int i = 0;i < n;i++)
	{
		ans += number[i].t + (number[i].x-number[i].t*(number[i].v+r-s))/double(number[i].v);
	}
	printf("Case #%d: %.9lf\n" , Case , ans );
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int Case , q = 0;
	scanf("%d",&Case );
	while ( Case-- ) {
		init();
		solve(++q);
	}
	return 0;
}
