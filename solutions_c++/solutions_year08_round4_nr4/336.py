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
#define Maxn 1000
#define Maxk 5

#define pb(a) push_back(a);
#define mk(a , b) make_pair(a , b)

using namespace std;

typedef vector<int> vi;
typedef pair<int , int> ii;

FILE *in = fopen("d.in" , "r");
FILE *op = fopen("d.out" , "w");

void init(void);
void process(int);
void out(void);

int k;
int n;
char str[Maxn  + 1];
int p[Maxk + 1];
int visit[Maxk + 1];
char output[Maxn + 1];
int ans;

int main(void){
	int K;
	fscanf(in , "%d" , &K);
	int i;
	for(i=1; i<=K; i++){
		ans = INT_MAX;
		init();
		process(1);
		fprintf(op , "Case #%d: " , i);
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	fscanf(in , "%d" , &k);
	fscanf(in , "%s" , &str[1]);
	n = strlen(&str[1]);
}

int process2(void){
	int i , j = 1 , t = 0 , cnt = 0;
	output[0] = -1;
	for(i=1; i<=n; i++){
		if(j > k){
			t++;
			j = 1;
		}
		output[i] = str[k * t + p[j]];
		if(output[i] != output[i - 1]) cnt++;
		j++;
	}
	return cnt;
}

void process(int i){
	if(i > k){
		int t = process2();
		if(ans > t){
			ans = t;
		}
	} else{
		int j;
		for(j=1; j<=k; j++){
			if(!visit[j]){
				visit[j] = 1;
				p[i] = j;
				process(i + 1);
				visit[j] = 0;
			}
		}
	}
}

void out(void){
	fprintf(op , "%d\n" , ans);
}
