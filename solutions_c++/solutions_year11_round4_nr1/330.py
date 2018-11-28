#include<cstdio>
#include<iostream>
#include<cstdlib>
using namespace std;
struct node{
	double b, e, s;
}way[10000];

int cmp(const void * a, const void *b ){
	if(((node*)a)->s > ((node*)b)->s)return 1;
	else return -1;
}
void work(int x)
{
	int X, S, R, N;
	double t;
	printf("Case #%d: ",x);
	scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
	double L = X;
	for(int i = 0 ; i < N; i++){
		scanf("%lf%lf%lf", &way[i].b, &way[i].e,&way[i].s);
		L-=way[i].e - way[i].b;
	}
	qsort(way, N, sizeof(way[0]), cmp);
	double ans = 0;
	if(L <= R * t){
		t-=L/(R*1.0);
		ans += L/(R*1.0);
		int begin = -1;
		for(int i = 0; i< N; i++){
			if(way[i].e-way[i].b <= (R+way[i].s) * t){
				double tee=(way[i].e - way[i].b) / (R*1.0+ way[i].s); 
				ans += tee;
				t-= tee;
			}
			else {
				ans += t;
				way[i].e -= (R + way[i].s)* t;
				t = 0;
				begin = i;
				break;
			}
		}
		
		if(begin != -1)for(int i = begin; i <N; i++){
			ans+=(way[i].e -way[i].b)/(S*1.0 + way[i].s);
		}
	}
	else {
		ans +=t;
		L -= R*t;
		t = 0;
		ans += L/(S*1.0);
		for(int i = 0; i< N;i++)ans+=(way[i].e-way[i].b)/(way[i].s+S*1.0);
		
	}
	printf("%.10lf\n", ans);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
