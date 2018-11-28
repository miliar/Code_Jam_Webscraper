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

int num[110];
int turn[110];
int n;

bool read(){
	//if() return false;	
	scanf("%d", &n);	
	char buf[10];
	int temp;
	
	for(int i = 0; i < n; i++){
		scanf("%s", buf);
		scanf("%d", &temp);		
		if(buf[0] == 'B') turn[i] = 0;
		else turn[i] = 1;
		num[i] = temp;	
	}

	return true;
}


int getnext(int cur, int robot){
	for(int i = cur+1; i < n; i++) if(turn[i] == robot) return i;
	return -1;
}

int cn = 1;

void process(){
	int o, b;
	int res = 0;
	int cur = 0;
	
	o = getnext(-1, 1);
	b = getnext(-1, 0);
	
	int po = 1;
	int pb = 1;
	
//	printf("%d %d\n", num[o], num[b]);
	
	while(o != -1 || b != -1){
		//printf("Blue is at %d and wants to go to %d pursuing goal %d\n", pb, num[b], b);
		//printf("Orange is at %d and wants to go to %d pursuing goal %d\n", po, num[o], o);
		
		if(b != -1 && pb == num[b] && turn[cur] == 0){
			//printf("Blue pushed button %d\n", num[b]);
			b = getnext(b, 0);
			if(po > num[o]) po--;
			if(po < num[o]) po++;
			cur++;
		}
		else if(o != -1 && po == num[o] && turn[cur] == 1){
			//printf("Orange pushed button %d\n", num[o]);
			o = getnext(o, 1);
			if(pb > num[b]) pb--;
			if(pb < num[b]) pb++;
			cur++;
		}
		else{
			//printf("Blue and orange walking\n");
			if(po > num[o]) po--;
			if(po < num[o]) po++;
			if(pb > num[b]) pb--;
			if(pb < num[b]) pb++;
		}
			res++;
	}
	
	printf("Case #%d: %d\n", cn++, res);
	
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);	
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	//while(1);
	
	return 0;
}
