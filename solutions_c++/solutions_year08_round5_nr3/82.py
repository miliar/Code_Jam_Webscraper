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

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb(a) push_back(a);
#define mk(a , b) make_pair(a , b)
#define Maxr 80
#define Maxc 80
#define Maxn 3200

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

int r , c;
bool Map[Maxr + 1][Maxc + 1];
int ans;
int nmr[Maxr + 1][Maxc + 1];
bool network[Maxn + 1][Maxn + 1];
int Back[Maxn + 1];
int visit_l[Maxn + 1];
int visit_r[Maxn + 1];
int vn;
int ln , rn;
const int pn = 6;
const int py[pn + 10] = {0 , -1 , -1 , 0 , 0 , 1 , 1};
const int px[pn + 10] = {0 , -1 , 1 , 1 , -1 , 1 , -1};

int main(void){
	int K;
	fscanf(in , "%d" , &K);
	FOR(i , 1 , K){
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
	fscanf(in , "%d %d" , &r , &c);
	FOR(i , 1 , r){
		FOR(j , 1 , c){
			char c;
			fscanf(in , "%c" , &c);
			if(c == '\n' || c == ' '){
				fscanf(in , "%c" , &c);
			}
			Map[i][j] = (c == 'x' || c == 'X');
		}
	}
	ln = rn = 0;
	vn = 0;
	memset(visit_l , 0 , sizeof(visit_l));
	memset(visit_r , 0 , sizeof(visit_r));
	memset(Back , 0 , sizeof(Back));
	memset(network , 0 , sizeof(network));
	memset(nmr , 0 , sizeof(nmr));

	int i , j;
	for(i=1; i<=r; i++){
		for(j=1; j<=c; j+=2){
			if(!Map[i][j]){
				nmr[i][j] = ++ln;
			}
		}
		for(j=2; j<=c; j+=2){
			if(!Map[i][j]){
				nmr[i][j] = ++rn;
			}
		}
	}
	ans = ln + rn;

	int k , y , x;
	for(i=1; i<=r; i++){
		for(j=1; j<=c; j+=2){
			if(nmr[i][j] == 0) continue;
			for(k=1; k<=pn; k++){
				y = i + py[k];
				x = j + px[k];
				if(y >= 0 && y <= r && x >= 0 && x <= c && nmr[y][x]){
					network[nmr[i][j]][nmr[y][x]] = true;
				}
			}
		}
	}

//	fprintf(op , "%d %d\n" , ln , rn);
}

bool path(int li){
	int i;
	for(i=1; i<=rn; i++){
		if(network[li][i] && visit_r[i] != vn){
			visit_r[i] = vn;
			int ii = Back[i];
			if(ii){
				if(visit_l[ii] != vn){
					visit_l[ii] = vn;
					if(path(ii)){
						network[ii][i] = true;
						network[li][i] = false;
						Back[i] = li;
						return true;
					}
				}
			} else{
				network[li][i] = false;
				Back[i] = li;
				return true;
			}
		}
	}
	return false;
}

void process(void){
	FOR(i , 1 , ln){
		vn++;
		visit_l[i] = vn;
		if(path(i)){
			ans--;
		}
	}

/*
	{
		int cnt = 0 , l = 0;
		int Queue[Maxr * Maxc + 1];
		memset(visit_l , 0 , sizeof(visit_l));
		memset(visit_r , 0 , sizeof(visit_r));
		FOR(i , 1 , rn){
			if(Back[i]){
				visit_l[Back[i]] = -1;
			}
		}
		FOR(i , 1 , ln){
			if(!visit_l[i]){
				visit_l[i] = 1;
				Queue[++l] = i;
			} else{
				visit_l[i] = 0;
			}
		}
		while(cnt != l){
			cnt++;
			int from = Queue[cnt];
			FOR(i , 1 , rn){
				if(network[from][i] && !visit_r[i]){
					visit_r[i] = 1;
					int ii = Back[i];
					if(!visit_l[ii]){
						l++;
						visit_l[ii] = 1;
						Queue[l] = ii;
					}
				}
			}
		}
		FOR(l , 1 , ln){
			if(!visit_l[l]) continue;
			FOR(i , 1 , r){
				for(int j = 1; j<=c; j+=2){
					if(nmr[i][j] == l){
						nmr[i][j] = -1;
					}
				}
			}
		}
		FOR(l , 1 , rn){
			if(visit_r[l]) continue;
			FOR(i , 1 , r){
				for(int j = 2; j<=c; j+=2){
					if(nmr[i][j] == l){
						nmr[i][j] = -1;
					}
				}
			}
		}
		FOR(i , 1 , r){
			FOR(j , 1, c){
				if(nmr[i][j] == 0){
					fprintf(op , "x");
				} else if(nmr[i][j] == -1){
					fprintf(op , "v");
				} else{
					fprintf(op , ".");
				}
			}
			fprintf(op , "\n");
		}
	}*/
}

void out(void){
	fprintf(op , "%d\n" , ans);
}
