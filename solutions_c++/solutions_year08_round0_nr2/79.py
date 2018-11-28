#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 110;

struct Tnode{
	int st, ed;
} a[MAXN], b[MAXN];

bool compare_st(const Tnode&a, const Tnode&b)
{
	return a.st<b.st;	
}

bool compare_ed(const Tnode&a, const Tnode&b)
{
	return a.ed<b.ed;	
}

int t, n, m;
bool f1[MAXN], f2[MAXN];

void init()
{
	int i, x1, y1, x2, y2;
	
	scanf("%d", &t);
	scanf("%d%d", &n, &m);
	for (i=1; i<=n; i++){
		scanf("%d:%d %d:%d", &x1, &y1, &x2, &y2);
		a[i].st=x1*60+y1;
		a[i].ed=x2*60+y2;
	}
	for (i=1; i<=m; i++){
		scanf("%d:%d %d:%d", &x1, &y1, &x2, &y2);
		b[i].st=x1*60+y1;
		b[i].ed=x2*60+y2;
	}		
}

void calc(Tnode a[MAXN], int n, Tnode b[MAXN], int m)
{
	int i, j, s;
	
	sort(b+1, b+m+1, compare_ed);
	sort(a+1, a+n+1, compare_st);
	i=1; j=1; s=0;
	while (i<=n && j<=m){
		if (a[i].st-t>=b[j].ed){
			i++; j++;
		}
		else
		{
			i++; s++;
		}
	}
	s+=(n-i+1);
	printf("%d", s);		
}

void work()
{
	int i, j, s;
	
	calc(a, n, b, m);
	printf(" ");
	calc(b, m, a, n);
	printf("\n");
}

int main()
{
	int cas=0, tt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tt);
	while (tt--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
	
	return 0;
}
