#include <cstdio>
#include <iostream>
#include <cmath>
#include <map>

using namespace std;

const int MAXN = 20000; 
const int MAXC = 26+1; 

map <string, int> dict;
int N, M, tests, test, i, j, k, p, passed, minnum; 
string word[MAXN]; 
bool show[MAXN][MAXC];

int num[MAXN], kd[MAXN], list[MAXN]; 
bool add[MAXN];
int tot[MAXN];
string now[MAXC][MAXN];

int main() {
    freopen("2.in","r",stdin); 
    freopen("2.out","w",stdout);

    scanf("%d",&tests);
    
    for (test = 1; test <= tests; ++test){
		scanf("%d %d\n", &N, &M); 
		for (i = 0; i < N; ++i ) {
			cin >> word[i];
			for ( j = 0; j < 26; ++j ) show[i][j] = false;
			for ( j = 0; j < word[i].size(); ++j ) show[i][word[i][j] - 'a'] = true;
			for (j = 0; j < 26; ++j ) if (show[i][j]) ++num[i]; 
		}
		
		printf("Case #%d:", test); 
		passed = 0;
		
		for ( i = 0; i < M; ++i ) {
			string l;
			cin >> l;
			for (k = 0; k < 26; ++k) list[k] = int(l[k] - 'a'); 
			
			dict.clear();
			for ( j = 0; j < N; ++j ) {
				now[0][j] = word[j];
				for ( k = 0; k < word[j].size(); ++k ) now[0][j][k]='*';
				if ( dict[now[0][j]] == 0 ) dict[now[0][j]] = ++passed;
				kd[j] = dict[now[0][j]]-1;
				for ( k = 0; k < 26; ++k ){
					now[k+1][j] = now[k][j];
					if ( show[j][list[k]] )
						for ( p = 0; p < word[j].size(); ++p )
							if ( word[j][p] == l[k] )
								now[k+1][j][p] = l[k];
				}
			}
			
			memset(tot, 0, sizeof(tot));
			for ( j = 0; j < 26; ++j ){
				memset(add, 0, sizeof(add));
				dict.clear(); passed = 0;
				for ( k = 0; k < N; ++k )
					if ( show[k][list[j]] ) add[kd[k]]=1;
				for ( k = 0; k < N; ++k )
					if ( add[kd[k]] && ! show[k][list[j]] )
						tot[k]++;
				for ( k = 0; k < N; ++k ){
					if ( dict[now[j+1][k]] == 0 )
						dict[now[j+1][k]] = ++passed;
					kd[k] = dict[now[j+1][k]]-1;					
				}
			}
			string ans;
			
            minnum = -1;
			for ( j = 0; j < N; ++j )
				if ( tot[j] > minnum ){
					minnum = tot[j]; ans = word[j];
				}
			cout<<' '<<ans;
		}
		printf("\n");
	}
}
