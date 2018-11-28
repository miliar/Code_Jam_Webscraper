#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <iostream>

#define ln printf("\n")

using namespace std;

const int inf = 0x7f7f7f7f;
const double pi=acos(-1.0);
const double eps = 1e-8;

int r[20];
int n;

bool read(){
	//if() return false;	
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++){
		scanf("%d", &r[i]);
	}
		
	return true;
}

bool test(int v, int pos){
	return (v & (1 << pos)) != 0;
}

void printbits(int v, int size){
	for(int i = size-1; i >= 0; i--){
		printf("%d", test(v, i));
	} 
	printf("\n");
}

int eval(int mask){
	int res = 0;
	for(int i = 0; i < n; i++){
		if(test(mask, i)) res += r[i];
	}
	
	return res;
}

int biteval(int mask){
	int res = 0;
	
	for(int i = 0; i < n; i++){
		if(test(mask, i)) res ^= r[i];
	}
	
	return res;
}

int cn = 1;

void process(){
	int tot = (1 << (n))-1;
	//printbits(tot, 10);
	int best = -1;
		
	for(int i = 1; i < tot; i++){
	//	printbits(i, 10);
	//	printbits(~i, 10);
		//printf("bit - %d %d\n", biteval(i), biteval(~i));
		//printf("nor - %d %d\n", eval(i), eval(~i));
		//printf("----\n");
		if(biteval(i) == biteval(~i)) best = max(best, max(eval(i), eval(~i)));
	}
	printf("Case #%d: ", cn++);
	if(best == -1) printf("NO\n");
	else printf("%d\n", best);
}

int main(){
	freopen("a.txt", "r", stdin);	
	freopen("b.txt", "w", stdout);
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
//	while(1);
	
	return 0;
}
