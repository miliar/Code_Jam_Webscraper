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

char linha[1024];
int tc;

int main (void){
	char mapa[32];
	mapa[0] = 'y';
	mapa[1] = 'h';
	mapa[2] = 'e';
	mapa[3] = 's';
	mapa[4] = 'o';
	mapa[5] = 'c';
	mapa[6] = 'v';
	mapa[7] = 'x';
	mapa[8] = 'd';
	mapa[9] = 'u';
	mapa[10] = 'i';
	mapa[11] = 'g';
	mapa[12] = 'l';
	mapa[13] = 'b';
	mapa[14] = 'k';
	mapa[15] = 'r';
	mapa[16] = 'z';
	mapa[17] = 't';
	mapa[18] = 'n';
	mapa[19] = 'w';
	mapa[20] = 'j';
	mapa[21] = 'p';
	mapa[22] = 'f';
	mapa[23] = 'm';
	mapa[24] = 'a';
	mapa[25] = 'q';

	int tc;
	gets(linha);
	sscanf(linha, "%d", &tc);
	for(int i = 0; i < tc; i++){
		printf("Case #%d: ", i + 1);
		gets(linha);
		int len = strlen(linha);
		for(int j = 0; j < len; j++){
			if( linha[j] == ' ') printf(" ");
			else printf("%c", mapa[linha[j]-'a']);
		}
		printf("\n");
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