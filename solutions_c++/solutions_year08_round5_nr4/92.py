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
#define MOD 10007

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb(a) push_back(a);
#define mk(a , b) make_pair(a , b)
#define Maxn 100

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

int Dy[Maxn + 1][Maxn + 1];
bool Map[Maxn + 1][Maxn + 1];
int H , W;

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
	int R;
	fscanf(in , "%d %d %d" , &H , &W , &R);
	memset(Map , 0 , sizeof(Map));
	memset(Dy , 0 , sizeof(Dy));
	FOR(i , 1 , R){
		int h , w;
		fscanf(in , "%d %d" , &h , &w);
		Map[h][w] = true;
	}
}

void process(void){
	Dy[1][1] = 1;
	FOR(i , 2 , H){
		FOR(j , 2 , W){
			if(Map[i][j]) continue;
			int y , x;
			y = i - 2;
			x = j - 1;
			if(y >= 1 && x >= 1){
				Dy[i][j] += Dy[y][x];
				Dy[i][j] %= MOD;
			}
			y = i - 1;
			x = j - 2;
			if(y >= 1 && x >= 1){
				Dy[i][j] += Dy[y][x];
				Dy[i][j] %= MOD;
			}
		}
	}
}

void out(void){
	fprintf(op , "%d\n" , Dy[H][W]);
}
