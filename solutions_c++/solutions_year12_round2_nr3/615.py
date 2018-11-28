# include <cstdio>
# include <cstdlib>
# include <cstring>
# include <cmath>
# include <ctime>
# include <string>
# include <algorithm>
# include <vector>
# include <stack>
# include <queue>
# include <set>
# include <iostream>
# include <map>

using namespace std;

# define INF 0x3f3f3f3f
# define MAXN 528
# define mp make_pair
# define pb push_back
# define SORT(v) sort(v.begin(), v.end())
# define pii pair<int,int>
# define vii vector< pii >
# define psi pair<string,int>
# define EPS 1e-7

int cmp(double a, double b){
	if( a + EPS < b ) return -1;
	if( b + EPS < a ) return  1;
	return 0;
}

int read_tc(){
	char linha[128];
	int t;
	gets(linha);
	sscanf(linha, "%d", &t);
	return t;
}

int N;

int s[MAXN];

void print_vet(int k){
	int foi = 0;
	for(int j = 0 ; j < N; j++){
		if( k & (1<<j) ){
			if( foi == 0 ) printf("%d", s[j]);
			else printf(" %d", s[j]);
			foi = 1;
		}
	}
	printf("\n");
}

map<long long, int > mapa;

int main (void){

	int T = read_tc();
	for(int tc = 1; tc <= T; tc++){
		printf("Case #%d:\n", tc);
		/*****************************CODE STARTS HERE ***************************************************/
		scanf("%d", &N);
		mapa.clear();
		for(int i = 0; i < N; i++) scanf("%d", &s[i]);
		
		for(int i = 1; i < (1<<N) - 1; i++){
			long long soma = 0;
			for(int j = 0 ; j < N; j++){
				if( ( i & (1<<j) ) ) soma += s[j];
			}
			if( mapa.find(soma) == mapa.end() ) mapa[soma] = i;
			else{
				print_vet(mapa[soma]);
				print_vet(i);
				break;
			}
		}
		
		/*****************************CODE ENDS HERE ***************************************************/
	}
	return 0;
}