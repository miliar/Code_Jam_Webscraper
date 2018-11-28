#include<cstdio>
#include<climits>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<sstream>
#define Maxn 50

#define pb(a) push_back(a);
#define mk(a , b) make_pair(a , b)

using namespace std;

typedef vector<int> vi;
typedef pair<int , int> ii;

FILE *in = fopen("b.in" , "r");
FILE *op = fopen("b.out" , "w");

void init(void);
void process(void);
void out(void);

int n , m , A;

int main(void){
	int i , K;
	fscanf(in , "%d" , &K);
	for(i=1; i<=K; i++){
		init();
		fprintf(op , "Case #%d: " , i);
		process();
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	fscanf(in , "%d %d %d" , &n , &m , &A);
}

int ccw(int ax , int ay , int bx , int by , int cx , int cy){
	int rtn = (ax * by + bx * cy + cx * ay) - (ay * bx + by * cx + cy * ax);
	if(rtn < 0) rtn = -rtn;
	return rtn;
}

void process(void){
	int cx , cy;
	int ay = 0 , ax;
	int bx = 0 , by;
	for(cx=0; cx<=n; cx++){
		for(cy=1; cy<=m; cy++){
			if(n * m  >= A){
				for(ax=0; ax<=n; ax++){
					for(by=0; by<=m; by++){
						if(ccw(ax , ay , bx , by , cx ,cy) == A){
							fprintf(op , "%d %d %d %d %d %d\n" , ax , ay , bx , by , cx , cy);
							return;
						}
					}
				}
			}
		}
	}
	fprintf(op , "IMPOSSIBLE\n");
}

void out(void){
}
