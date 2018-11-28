#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#define EPS 1e-9
using namespace std;
int main(){
	int test, t;
	int speed[200];
	int x, S, r, w, n;
	double time;
	int a, b, s;
	double ans;
	double ns;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	scanf("%d", &test);
	for(t=1; t<=test; t++){
		printf("Case #%d: ", t);
		scanf("%d%d%d%lf%d", &x, &S, &r, &time, &n);
		for(int i=0; i<x; i++)
			speed[i] = S;
		for(int i=0; i<n; i++){
			scanf("%d %d %d", &a, &b, &s);
			for(int j=a; j<b; j++)
				speed[j] += s;
		}
		sort(speed, speed+x);
		ans = 0;

		for(int i=0; i<x; i++){
			if(time < EPS){
				ans += 1.0 / speed[i];
			}
			else{
				ns = speed[i] - S + r;
				if(ns * time > 1){
					time -= 1.0 / ns;
					ans += 1.0 / ns;
				}
				else{
					ans += time;
					ans += (1.0-ns*time) / speed[i];
					time = 0;
				}
			}
		}
		printf("%lf\n", ans);
	}
}