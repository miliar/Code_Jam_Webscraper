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
# define MAXN 1
# define mp make_pair
# define pb push_back
# define SORT(v) sort(v.begin(), v.end())
# define pii pair<int,int>
# define vii vector< pii >
# define psi pair<string,int>

int tc;

int main (void){
	scanf("%d", &tc);
	for(int i = 0; i < tc; i++){
		printf("Case #%d: ", i + 1);
		int N, S, p;
		scanf("%d%d%d", &N, &S, &p);
		int resp = 0;
		for(int j = 0 ; j < N; j++){	
			int score;
			scanf("%d", &score);
			int p1 = 10, p2 = 10, p3 = 10;
			int iter = 0;
			while(1){
				if( p1 + p2 + p3 == score ){
					if( p3 >= 0 and p1 >= 0 ){
						if( (p3 - p1) == 2 and S ){
							resp++;
							S--;
						}
						else if( p3 - p1 < 2 ) resp++; 
					}
					break;
				}
				else{
					if( iter % 3 == 0 ) p1--;
					if( iter % 3 == 1 ) p2--;
					if( iter % 3 == 2 ){
						if( p3 > p ) p3--;
					}
				}
				iter++;
			}
		}
		printf("%d\n", resp);
	}
/*	for(int c = 0; c < 3; c++){
		gets(linha1);
		gets(linha2);
		int len = strlen(linha1);
		for(int i = 0; i < len; i++)
			if( linha1[i] != ' ')
				mapa[linha2[i] - 'a'] = linha1[i];
	}
	
	for(char i = 'a'; i <= 'z'; i++){
		printf("mapa[%d] = '%c';\n", i-'a', mapa[i-'a']);
	}
*/
	return 0;
}