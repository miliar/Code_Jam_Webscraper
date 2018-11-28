#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
#define pb push_back

int normal[40], surp[40];

void pre(){
	memset(normal, -1, sizeof normal);
	memset( surp, -1, sizeof surp);
	
	for(int i = 0; i <= 10; ++i){
		for(int j = 0; j <= 10; ++j){
			for(int k = 0; k <= 10; ++k ){
				if(abs(i-j) > 2 || abs(i-k) > 2 || abs(j-k) > 2) continue;
				
				int soma = i + j + k;
				int best = max(i,max(j,k));
				
				if(abs(i-j) == 2 || abs(i-k) == 2 || abs(j-k) == 2) surp[soma] = max( surp[soma], best );
				else normal[soma] = max( normal[soma], best );
			}
		}
	}

}

int t[200];
int tmp[200];
bool ok[200];

int main(){
	pre();
	
	int casos;
	scanf( "%d", &casos );
	for( int ca = 1; ca <= casos; ++ca ){
		int n, s, p;
		scanf( "%d%d%d", &n, &s, &p);
		for( int i = 0; i < n; ++i ) scanf( "%d", t + i );
		for(int i = 0; i < n; ++i){
			if(~normal[t[i]]){
				tmp[i] = normal[t[i]];
				ok[i] = true;
			}else{
				tmp[i] = surp[t[i]];
				ok[i] = false;
				--s;
			}
		}
		
		while(s--){
			int ind = -1, best;
			for(int i = 0; i < n; ++i ){
				if(!ok[i]) continue;
				if(!surp[t[i]]) continue;
				if(ind == -1 || (tmp[i] < p && surp[t[i]] >= p) ){
					ind = i;
					best = surp[t[i]];
				}
			}
			ok[ind] = false;
			tmp[ind] = best;
		}
		int cont = 0;
		for(int i = 0; i < n; ++i){
			if(tmp[i] >= p) ++cont;
		}
		printf( "Case #%d: %d\n", ca, cont );
		
		
	}
	
}

