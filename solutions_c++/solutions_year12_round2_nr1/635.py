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
# define MAXN 256
# define mp make_pair
# define pb push_back
# define SORT(v) sort(v.begin(), v.end())
# define pii pair<int,int>
# define vii vector< pii >
# define psi pair<string,int>
# define EPS 1e-9

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

int s[MAXN];

int main (void){

	int T = read_tc();
	int N, total;
	for(int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);
		/*****************************CODE STARTS HERE ***************************************************/
		scanf("%d", &N);
		total = 0;
		for(int i = 0; i < N; i++){
			scanf("%d", &s[i]);
			total += s[i];
		}
		
		for(int i = 0; i < N; i++){
			int temp = 200;
			double resp = 1.0;
			double lo = 0.0, hi = 1.0;
			while( temp-- ){
				double mid = lo + (hi-lo)/2;
				double sum = mid;
				for(int j = 0; j < N; j++){
					if( i == j ) continue;
					double teste = (double) (total*mid - s[j] + s[i])/total;
					if( cmp(teste,0) >= 0 ) sum += teste;
				}
				if( cmp(sum,1.0) >= 0 ){
					hi = mid;
					resp = mid;
				}
				else lo = mid;
			}
			if( i == 0 ) printf("%.6f", resp*100);
			else printf(" %.6f", resp*100);
		}
		
		/*****************************CODE ENDS HERE ***************************************************/
		printf("\n");
	}
	return 0;
}