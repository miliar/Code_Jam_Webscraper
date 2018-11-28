#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
#define MM(a , x) memset(a , x , sizeof(a))
#define sqr(x) ((x) * (x))
#define abs(x) ((x > 0) ? (x) : -(x))
#define REP(i , n) for ((i) = 0; (i) < (n); ++(i))
#define FOR(i , a , b) for ((i) = (a); (i) <= (b); ++(i))
#define FORD(i , a , b) for ((i) = (a); (i) >= (b); --(i))
typedef long long LL;

int n , m , tot , ans , nowa , nowb , T , testcase;
vector<int> a , b;
int order[108][2] , pa , pb;

void init()
{
	scanf("%d " , &n);
	a.clear(); b.clear();
	int i , j , k;
	FOR (i , 1 , n)
	{
		char ch;
		scanf("%c %d " , &ch , &k);
		if (ch == 'O') a.push_back(k); else b.push_back(k);
		if (ch == 'O') order[i][0] = 1; else order[i][0] = 2;
		order[i][1] = k;
	}
	nowa = nowb = 1;
}

void work()
{
	ans = 0;
	pa = pb = 0;
	int i , j , k , tp;
	FOR (i , 1 , n)
	{
		if (order[i][0] == 1)
		{
			tp = abs(a[pa] - nowa) + 1;
			nowa = a[pa];
			pa++;
			if (abs(b[pb] - nowb) <= tp)
			{
				nowb = b[pb];
			}
			else
			{
				nowb += tp * (b[pb] > nowb ? 1 : -1);
			}
			ans += tp;
		}
		else
		{
			tp = abs(b[pb] - nowb) + 1;
			nowb = b[pb];
			pb++;
			if (abs(a[pa] - nowa) <= tp)
			{
				nowa = a[pa];
			}
			else
			{
				nowa += tp * (a[pa] > nowa ? 1 : -1);
			}
			ans += tp;
		}
	}
	printf("Case #%d: %d\n" , T , ans);
}

int main()
{
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d\n" , &testcase);
	FOR (T , 1 , testcase)
	{
		init();
		work();
	}
	return 0;
}
