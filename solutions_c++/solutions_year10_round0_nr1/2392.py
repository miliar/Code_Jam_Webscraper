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

#define INF 2000000000
#define mp make_pair

using namespace std;

int cases, n, k;
int counter = 1;
int mult[40];

void init(){
	mult[0] = 1;
	for(int i = 1; i < 32; i++){
		mult[i] = 2*mult[i-1];
	}
}

bool read(){
	if(!cases--) return false;
	scanf("%d%d", &n, &k);	
	return true;
}

void process(){	
	if(k == 0 || k%(mult[n]) != mult[n] - 1) printf("Case #%d: OFF\n", counter++);
	else printf("Case #%d: ON\n", counter++);
}

int main(){

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &cases);
	init();
	while(read()){		
		process();
	}
	
	return 0;
}
