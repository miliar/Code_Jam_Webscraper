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
#define Maxn 10000

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb(a) push_back(a);
#define mk(a , b) make_pair(a , b)

using namespace std;

typedef vector<int> vi;
typedef pair<int , int> ii;

FILE *in = fopen("a.in" , "r");
FILE *op = fopen("a.out" , "w");

void init(void);
void process(void);
void out(void);

int Dy[Maxn + 1][2];
int node[Maxn + 1];
int ch[Maxn + 1];
int n , v;

int main(void){
	int i , K;
	fscanf(in , "%d" , &K);
	for(i=1; i<=K; i++){
		init();
		process();
		fprintf(op , "Case #%d: " , i); 
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	memset(Dy , 0 , sizeof(Dy));
	memset(node , 0 , sizeof(node));
	memset(ch , 0 , sizeof(ch));
	fscanf(in , "%d %d" , &n , &v);
	int i;
	for(i=1; i<=n/2; i++){
		fscanf(in , "%d %d" , &node[i] , &ch[i]);
	}
	for(i = n/2 + 1; i<=n; i++){
		fscanf(in , "%d" , &node[i]);
	}
}

int min(int a , int b){
	if(a > b) return b; else return a;
}

int max(int a , int b){
	if(a < b) return b; else return a;
}

void process(void){
	int i;
	for(i=n/2 + 1; i<=n; i++){
		Dy[i][node[i]] = 0;
		Dy[i][1-node[i]] = INT_MAX;
	}
	for(i=n/2; i>=1; i--){
		int l = i * 2 , r = i * 2 + 1;
		Dy[i][0] = Dy[i][1] = INT_MAX;
		if(node[i] == 1){
			if(Dy[l][1] != INT_MAX && Dy[r][1] != INT_MAX){
				Dy[i][1] = min(Dy[i][1] , Dy[l][1] + Dy[r][1]);
			}
			if(Dy[l][0] != INT_MAX && Dy[r][1] != INT_MAX){
				Dy[i][0] = min(Dy[i][0] , Dy[l][0] + Dy[r][1]);
			}
			if(Dy[l][1] != INT_MAX && Dy[r][0] != INT_MAX){
				Dy[i][0] = min(Dy[i][0] , Dy[l][1] + Dy[r][0]);
			}
			if(Dy[l][0] != INT_MAX && Dy[r][0] != INT_MAX){
				Dy[i][0] = min(Dy[i][0] , Dy[l][0] + Dy[r][0]);
			}
		} else{
			if(Dy[l][1] != INT_MAX && Dy[r][1] != INT_MAX){
				Dy[i][1] = min(Dy[i][1] , Dy[l][1] + Dy[r][1]);
			}
			if(Dy[l][0] != INT_MAX && Dy[r][1] != INT_MAX){
				Dy[i][1] = min(Dy[i][1] , Dy[l][0] + Dy[r][1]);
			}
			if(Dy[l][1] != INT_MAX && Dy[r][0] != INT_MAX){
				Dy[i][1] = min(Dy[i][1] , Dy[l][1] + Dy[r][0]);
			}
			if(Dy[l][0] != INT_MAX && Dy[r][0] != INT_MAX){
				Dy[i][0] = min(Dy[i][0] , Dy[l][0] + Dy[r][0]);
			}
		}
		if(ch[i] == 1){
			if(node[i] == 1){
				if(Dy[l][1] != INT_MAX && Dy[r][1] != INT_MAX){
					Dy[i][1] = min(Dy[i][1] , Dy[l][1] + Dy[r][1] + 1);
				}
				if(Dy[l][0] != INT_MAX && Dy[r][1] != INT_MAX){
					Dy[i][1] = min(Dy[i][1] , Dy[l][0] + Dy[r][1] + 1);
				}
				if(Dy[l][1] != INT_MAX && Dy[r][0] != INT_MAX){
					Dy[i][1] = min(Dy[i][1] , Dy[l][1] + Dy[r][0] + 1);
				}
				if(Dy[l][0] != INT_MAX && Dy[r][0] != INT_MAX){
					Dy[i][0] = min(Dy[i][0] , Dy[l][0] + Dy[r][0] + 1);
				}
			} else{
				if(Dy[l][1] != INT_MAX && Dy[r][1] != INT_MAX){
					Dy[i][1] = min(Dy[i][1] , Dy[l][1] + Dy[r][1] + 1);
				}
				if(Dy[l][0] != INT_MAX && Dy[r][1] != INT_MAX){
					Dy[i][0] = min(Dy[i][0] , Dy[l][0] + Dy[r][1] + 1);
				}
				if(Dy[l][1] != INT_MAX && Dy[r][0] != INT_MAX){
					Dy[i][0] = min(Dy[i][0] , Dy[l][1] + Dy[r][0] + 1);
				}
				if(Dy[l][0] != INT_MAX && Dy[r][0] != INT_MAX){
					Dy[i][0] = min(Dy[i][0] , Dy[l][0] + Dy[r][0] + 1);
				}
			}
		}
	}
}

void out(void){
	if(Dy[1][v] == INT_MAX){
		fprintf(op , "IMPOSSIBLE\n");
	} else{
		fprintf(op , "%d\n" , Dy[1][v]);
	}
}
