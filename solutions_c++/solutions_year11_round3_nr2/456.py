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

int l, t, n, c;
double r[1010];

bool read(){
	//if() return false;	
	
	scanf("%d%d%d%d", &l, &t, &n, &c);
	int a;
	
	for(int i = 0; i < c; i++){
		scanf("%d", &a);
		for(int j = i; j < n; j+=c){
			r[j] = a;
		}
	}
	
	for(int i = 0; i < n; i++){
		//r[i] += r[i-1];
		//printf("%.3lf\n", r[i]);
	}
	
	return true;
}

int cn = 1;

double solve(int a, int b){
	int star = 0;
	double time = 0;
	double rem;
	double walk;
	
	for(int i = 0; i < n; i++){
		
		if(i != a && i != b ){
			time += 2*r[star];
			star++;
		}
		else{
			//printf("Oi\n");
			if(time > t ){
				time += r[star];
				star++;
			} else{
				rem = t-time;
				walk = 0.5*rem;
				if(walk > r[star]) walk = r[star];
				if(rem < 0) walk = 0;
				time += walk*2;				
				time += (r[star]-walk);
				star++;
			}
		}
	}
	
	return time;
}


void process(){
	double res = 100000000;
	double temp;
	
	int x, y;
	//printf("%d\n", t);
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			x = i;
			y = j;
			if(l < 2) x = -1;
			if(l < 1) y = -1;
			temp = solve(x,y);
			if(temp < res) res = temp;
		}
	}
	
	res += 0.5;
	
	int ret = (int) res;
	
	printf("Case #%d: %d\n",cn++, ret);
	

	
	
}

int main(){
	
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	
	return 0;
}
