#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int n;
char a[100][100];
int s[100];

#define pi cos(-1.0)


struct point{
	double x , y;
	double r;
}c[5];

double dis(point a , point b)
{
	double dx = a.x - b.x;
	double dy = a.y - b.y;
	return sqrt(dx * dx + dy * dy);
}

double cal(int x  , int y)
{
	double d , r , s;
	d = dis(c[x] , c[y]) + c[x].r + c[y].r;

	//printf("%.7lf\n" , d/2);

	return d/2;
}

int main()
{
	freopen("test.in" , "r" , stdin);
	freopen("test.out" , "w" , stdout);
	int t;
	int cas = 1;
	scanf("%d" , &t);
	while (t --){

		scanf("%d" , &n);
		int i;
		for (i = 0 ; i < n ; i ++){
			scanf("%lf %lf %lf" , &c[i].x , &c[i].y , &c[i].r);
		}

		
		printf("Case #%d: " ,cas);
		cas ++;

		double ans = 99999;

		if (n == 1){
			printf("%.7lf\n" , c[0].r);
			continue;
		}
		if (n == 2){
			printf("%.7lf\n" ,  max(c[0].r , c[1].r) );
			continue;
		}

		ans = min(ans , max( cal(0 , 1) , c[2].r ));
		ans = min(ans , max( cal(0 , 2) , c[1].r ));
		ans = min(ans , max( cal(1 , 2) , c[0].r ));

		printf("%.7lf\n" , ans);

		
	}

}