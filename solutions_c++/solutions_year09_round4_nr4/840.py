#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>


#define __int64 long long
#define MAX(a,b) ((a)>(b)?(a):(b))
//#define MAX(a,b,c) (((a)>(b))?((a)>(c)?(a):(c)):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define dist(x1,y1, x2, y2) sqrt((double)(((x1)-(x2))*((x1)-(x2))+((y1)-(y2))*((y1)-(y2))))

//#define MIN(a,b,c) ((a)<(b)?(a)<(c)?(a):(c):(b))

int main(){
    freopen("map.in", "rt",stdin);
    freopen("map.out", "wt",stdout);
	int t;
	char str[1000];
		
    scanf("%d\n", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		int n;scanf("%d\n", &n);
		int x[100],y[100],r[100];
		for (int i = 0; i < n; i++)
			scanf("%d%d%d", &x[i], &y[i], &r[i]);
		double ans = 10;
		switch (n){
			case 1: ans = r[0];
					break;
			case 2: ans = MAX(r[0], r[1]);
				break;
			case 3:
				ans = MIN(MAX(r[0], (dist(x[1],y[1], x[2],y[2])+r[1]+r[2])/2),MAX(r[1], (dist(x[0],y[0], x[2],y[2])+r[0]+r[2])/2));
				ans = MIN(ans,MAX(r[2], (dist(x[0],y[0], x[1],y[1])+r[1]+r[0])/2));
				break;
		}
		printf("%.6f\n", ans);
	}
 }
