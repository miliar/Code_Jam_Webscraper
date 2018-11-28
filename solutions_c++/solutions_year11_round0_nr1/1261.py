#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

struct Node{
	int step, id;
};
char str[10];
int MAX(int a, int b){
	return a > b ?  a: b;
}
int ABS(int a){
	if(a < 0) a = -a;
	return a;
}
void solve(int cas){
	Node a, b;
	int n, i, x;
	a.step = 0;
	b.step = 0;
	a.id = 1;
	b.id = 1;
	
	scanf ("%d", &n);
	for(i = 1; i <= n; i ++){
		scanf ("%s%d", str, &x);
		if(str[0] == 'O'){
			if( ( b.step - a.step ) >= ABS(x - a.id)){
				a.id = x;
				a.step = b.step+1;
			}else{
				a.step += ABS(x-a.id)+1;
				a.id = x;
			}
		}else{
			if( ( a.step - b.step ) >= ABS(x - b.id)){
				b.id = x;
				b.step = a.step+1;
			}else{
				b.step += ABS(x-b.id)+1;
				b.id = x;
			}
		}
	}
	x = MAX(a.step , b.step);
	printf ("Case #%d: %d\n", cas, x);
}
int main(){
	int T, i;
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	scanf ("%d", &T);
	for(i = 1; i <= T; i ++){
		solve(i);
	}
	return 0;
}