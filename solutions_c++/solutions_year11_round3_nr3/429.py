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
int n, l, h;
int r[1010];

bool read(){
	//if() return false;	
	
	scanf("%d%d%d", &n, &l, &h);
	
	for(int i = 0; i < n; i++){
		scanf("%d", &r[i]);
	}
	
	//printf("%d %d %d\n", n, l ,h);
	
	return true;
}

int cn = 1;

bool ok(int x){
	//printf("Trying %d\n", x);
	for(int i = 0; i < n; i++){
		if(x%r[i] != 0 && r[i]%x != 0) return false;
	}
	
	return true;
}

void process(){
	int res = -1;
	
	for(int i = l; i <= h; i++){
		if(ok(i)){
			res = i;
			break;
		}
	}
	
	printf("Case #%d: ", cn++);
	if(res == -1) printf("NO\n");
	else printf("%d\n", res);
	
}

int main(){
	
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	
	return 0;
}
