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
const double EPS = 1e-6;

int comp(double a, double b){
	if(a + EPS < b) return -1;
	if(b + EPS < a) return 1;
	return 0;
}

const int inf = 0x7f7f7f7f;
const double pi=acos(-1.0);
const double eps = 1e-8;

int r, c, d;
char buf[1000];
int b[555][555];

bool read(){
	
	scanf("%d%d%d", &r, &c, &d);
	for(int i = 0; i < r; i++){
		scanf("%s", buf);
		for(int j = 0; j < c; j++){
			b[i][j] = buf[j]-48+d;
			//printf("%d ", b[i][j]);
		}
	}	
			
	return true;
}

int cn = 1;

bool mass(int y, int x, int k){
	//printf("%d %d %d\n", y, x, k);
	double xv = 0;
	double yv = 0;
	double yc = (y+y+k-1)/2.0;
	double xc = (x+x+k-1)/2.0;
	for(int i = y; i < y+k; i++){
		for(int j = x; j < x+k; j++){
			if(i == y || i == y+k-1){
				if(j == x || j == x+k-1) continue;
			}
			
			//printf("y: %d %d %lf\n", i, j
			
			yv += (i-yc)*b[i][j];
			xv += (j-xc)*b[i][j];
		}
	}
	//printf("%.3lf %.3lf\n", yc, xc);
	//printf("%.8lf %.8lf\n", yv, xv);
	//while(1);
	return (comp(xv, 0) == 0) && (comp(yv, 0) == 0);
}

void process(){
	printf("Case #%d: ", cn++);

	int hi = 0;

	for(int k = 3; k <= r; k++){
		for(int i = 0; i < r; i++){
			for(int j = 0; j < c; j++){
				if(i+k <= r && j+k <= c) if(mass(i,j,k)) hi = max(hi, k);
			}
		}
	}
	//ln;
	//mass(0,1,3);
	//mass(0,0,3);
	//mass(0,0,4);
	//mass(0,0,5);
	//mass(1,1,3);
	//mass(1,1,4);
	//mass(1,1,5);
	
	if(hi == 0) printf("IMPOSSIBLE\n");
	else printf("%d\n", hi);
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases; scanf("%d", &cases);
	
	while(cases-- && /**/ read()){		
		process();
	}
	
	//while(1);
	
	return 0;
}
