//////////
//
//	Auther: hazy
//	Pro ID:	
//	Pro Profile:  
//	Attention!!: 	
//	Created @ 2008_6
//
//////////
#include <iostream>
#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
using namespace std;
const int MAXN = 810;
typedef long long i64;


int 	cas, T;

int 	n;
i64		a[MAXN], b[MAXN];

int main()
{
	int 	i, j;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d", &n);
		for (i=0; i<n; i++)
			cin >> a[i];
		//	scanf("%lf", &a[i]);
		for (i=0; i<n; i++)
			cin >> b[i];
			
		//	scanf("%lf", &b[i]);
			
		sort(a, a+n);
		sort(b, b+n);
		
		i64		rnt = 0;
		for (i=0; i<n; i++)
			rnt += a[i] * b[n-i-1];
	//	cout << rnt << endl;
	//	printf("%.0lf\n", rnt);
		printf("Case #%d: ", ++T);
		cout << rnt << endl;
	}

	return 0;
}
