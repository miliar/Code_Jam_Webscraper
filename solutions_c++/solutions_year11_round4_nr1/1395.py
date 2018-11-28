#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int tree[1000005];
struct node{
	int st, ed, len;
	int w;
}st[1000005];
int contain[1000005];
int x, s, r, n, tot, t, n_case=0;
void update(int x, int val){
	for(int idx = x; idx < 1000005; idx += (idx)&(-idx)){
		tree[idx] += val;
	}
}
int read(int x){
	int sum = 0;
	for(int	idx = x; idx > 0; idx -= idx&(-idx)){
		sum += tree[idx];
	}
	return sum;
}
void solve(){
	sort(contain+1, contain+1+x);
	/*for(int i = 1; i <= x; i++){
		printf("%d %d\n", i, contain[i]);
	}*/
	double sum = 0.0;
	int idx;
	for(idx = 1; idx <= x; idx++){
		if(sum+1.0/double(contain[idx]+r-s) < t-1e-12){
			sum+=1.0/double(contain[idx]+r-s);
		} else break;
	}
	if(idx <= x){
		//printf("t = %d sum = %f\n", t, sum);
		double x1 = ((double(t)-sum)*double(contain[idx]+r-s))/(double(contain[idx]+r-s)),x2 = (1.0-(double(t)-sum)*double(contain[idx]+r-s))/(double(contain[idx]));
		sum += ((double(t)-sum)*double(contain[idx]+r-s))/(double(contain[idx]+r-s)) + (1.0-(double(t)-sum)*double(contain[idx]+r-s))/(double(contain[idx]));
		//printf("x1 = %f x2 = %f idx = %d x = %d\n", x1, x2, idx, x);
		//printf("idx = %d\n", idx);
		for(int i = idx+1; i <= x; i++){
			//printf("findxx %d\n", contain[i]);
			sum += 1.0/double(contain[i]);
		}	
	}
	printf("Case #%d: %.9f\n", ++n_case, sum);
}
void input(){
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	for(int i = 0; i < n; i++){
		scanf("%d%d%d", &st[i].st, &st[i].ed, &st[i].w);
		st[i].len = st[i].ed - st[i].st;
		st[i].st += 1;
		//printf("w = %d\n", st[i].w);
		//tot += st[i].w * st[i].len;
	}
	memset(tree, 0, sizeof(tree));
	for(int i = 0; i < n; i++){
		update(st[i].st, st[i].w);
		update(st[i].st+st[i].len, -st[i].w);
	}
	update(1, s), update(1+x, -s);
	/*for(int i = 0; i < 25; i++){
		printf("level = %d is %d\n", i, read(i));	
	}
	printf("%d\n", L);*/
	tot = 0;
	for(int i = 0; i <= x; i++){
		contain[i] = read(i);
		tot += contain[i];
	}
	/*for(int i = 0; i <= x; i++){
		printf("%d %d\n", i, contain[i]);
		//if(i == x) printf("\n");	
	}*/
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int CC;
	scanf("%d", &CC);
	while(CC--){
		input();		
		solve();
		//return 0;
	}	
}
              
