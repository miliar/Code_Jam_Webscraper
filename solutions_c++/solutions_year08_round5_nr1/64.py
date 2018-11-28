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
#include<cassert>
#define Maxn 300
#define ST 150

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb(a) push_back(a);
#define mk(a , b) make_pair(a , b)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int , int> ii;

FILE *in = fopen("input.txt" , "r");
FILE *op = fopen("output.txt" , "w");

void init(void);
void process(void);
void out(void);

char Matrix[Maxn + 1][Maxn + 1];
char Visit[Maxn + 1][Maxn + 1];
int ans;
queue< ii >  Q;

int minx , maxx;
int miny , maxy;

const int sty = ST , stx = ST;
const int pn = 4;
const int py[pn] = {-1 , 0 , 1 , 0};
const int px[pn] = {0 , 1 , 0 , -1};
const int pb[pn] = {1 , 2 , 4 , 8};
//R->+1
//L->-1

int main(void){
	int K;
	fscanf(in , "%d" , &K);
	FOR(i , 1 , K){
		minx = miny = INT_MAX;
		maxx = maxy = INT_MIN;
		init();
		process();
		fprintf(op , "Case #%d: " , i);
//		fprintf(stderr , "%d\n" , i);
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	int n;
	int y = sty , x = stx , b = 0;
	int r;
	const int Maxl = 40;
	char command[Maxl  + 1];
	ans = 0;
	memset(Matrix , 0 , sizeof(Matrix));
	memset(Visit , 0 , sizeof(Visit));
	fscanf(in , "%d" , &n);
	FOR(i , 1 , n){
		fscanf(in , "%s %d" , command , &r);
		int cl = strlen(command) - 1;
//		fprintf(op , "%s\n" , command);
//		fprintf(stderr , "%d %d %d\n" , i , y , x);
		FOR(j , 1 , r){
			FOR(k , 0 , cl){
				if(command[k] == 'F'){
					y += py[b];
					x += px[b];
					assert(x >= 0 && x <= Maxn && y >= 0 && y <= Maxn);
					if(b == 0){//up
						Matrix[y + 1][x] |= 2;
						Matrix[y + 1][x + 1] |= 8;
					} else if(b == 2){//down
						Matrix[y][x] |= 2;
						Matrix[y][x + 1] |= 8;
					} else if(b == 1){//right
						Matrix[y][x] |= 4;
						Matrix[y + 1][x] |= 1;
					} else{//left
						Matrix[y][x + 1] |= 4;
						Matrix[y + 1][x + 1] |= 1;
					}
				} else if(command[k] == 'L'){
					b--;
					b += pn;
					b %= pn;
				} else{
					b++;
					b %= pn;
				}
			}
		}
	}
}

void process(void){
	Q.push(mk(0 , 0));
	Visit[0][0] = 16;
	while(!Q.empty()){
		int y = Q.front().first;
		int x = Q.front().second;
		Q.pop();
		FOR(i , 0 , pn - 1){
			if(!(Matrix[y][x] & pb[i])){
				int t = y + py[i];
				int t2 = x + px[i];
				if(t >= 0 && t <= Maxn && t2 >= 0 && t2 <= Maxn && !Visit[t][t2]){
					Visit[t][t2] = 16;
					Q.push(mk(t , t2));
				}
			}
		}
	}
	FOR(i , 0 , Maxn){
		FOR(j , 0 , Maxn){
			if(Visit[i][j] == 0){
				miny = min(miny , i);
				maxy = max(maxy , i);
				minx = min(minx , j);
				maxx = max(maxx , j);
			}
		}
	}
	//사방체크
	for(int y=0, ry=Maxn; y<=Maxn; y++, ry--){
		for(int x=0, rx=Maxn; x<=Maxn; x++, rx--){
			//down
			if((Matrix[ry][x] & 4) || (ry + 1 <= Maxn && (Visit[ry + 1][x] & 4))){
				Visit[ry][x] |= 4;
			}
			//up
			if((Matrix[y][x] & 1) || (y - 1 >= 0 && (Visit[y - 1][x] & 1))){
				Visit[y][x] |= 1;
			}
			//left
			if((Matrix[y][x] & 8) || (x - 1 >= 0 && (Visit[y][x-1] & 8))){
				Visit[y][x] |= 8;
			}
			//right
			if((Matrix[y][rx] & 2) || (rx + 1 <= Maxn && (Visit[y][rx+1] & 2))){
				Visit[y][rx] |= 2;
			}
		}
	}
	FOR(i , 0 , Maxn){
		FOR(j , 0 , Maxn){
			if(!(Visit[i][j] & 16)) continue;
			if(((Visit[i][j] & 8) && (Visit[i][j] & 2)) || ((Visit[i][j] & 1) && (Visit[i][j] & 4))){
				ans++;
			}
		}
	}
}

void out(void){
	fprintf(op , "%d\n" , ans);
}
