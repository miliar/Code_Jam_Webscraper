#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


char spell[150];
char trans[30][30];
int pode[30][30], no[30][30], stacked[30], stack[150], top, a,n, rune,cn, topo;

char base[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};



int main() {
	for (int i=0; i < 8; ++i) base[i] -= 'A';
	
	int cases;
	scanf("%d",&cases);
	
	while (cases--) {
		++cn;
		
		scanf("%d",&a);
		for (int i=0; i < a; ++i) {
			scanf("%s",spell);
			pode[ spell[0]-'A' ][ spell[1]-'A' ] = pode[ spell[1]-'A' ][ spell[0]-'A' ] = cn;
			trans[ spell[0]-'A' ][ spell[1]-'A' ] = trans[ spell[1]-'A' ][ spell[0]-'A' ] = spell[2]-'A';	
		}
		scanf("%d",&a);
		for (int i=0; i < a; ++i) {
			scanf("%s",spell);
			no[ spell[0]-'A' ][ spell[1]-'A' ] = no[ spell[1]-'A' ][ spell[0]-'A' ] = cn;
		}
		
		topo=0;
		memset(stacked,0,sizeof(stacked));
		
		scanf("%d",&n);
		scanf("%s",spell);
		for (int i=0; i < n; ++i) {
			rune = spell[i]-'A';
			
			if (topo && pode[ stack[topo-1] ][ rune ] == cn ) {
				a = stack[topo-1];
				stacked[ a ]--;
				stack[topo-1] = trans[a][rune];
				stacked[ trans[a][rune] ]++;
			}
			else {
			
				for (int k=0; k < 8; ++k) {
					if ( no[rune][ base[k] ] != cn ) continue;
					if ( !stacked[ base[k] ] ) continue;
				
					memset(stacked,0,sizeof(stacked));
					topo=0;
					goto end;
				}
			
			
				stack[topo++] = rune;
				stacked[rune]++;
			}
			end: continue;
		}
		
		printf("Case #%d: [",cn);
		for (int i=0; i < topo; ++i) {
			if (i) printf(", ");
			printf("%c",stack[i]+'A');
		}
		printf("]\n");
		
	}
	
}
