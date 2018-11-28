#include <cstdio>
#define REP(i,n) for(int i = 0; i < n; i++)
using namespace std;

int dictionary[5010][20];
int pattern[20][30];
int L, N, D;
int main()
{
	scanf("%d %d %d", &L, &D, &N);
	getchar();
	REP(i, D){
		REP(j, L){
			char temp;
			scanf("%c", &temp);
			dictionary[i][j] = temp-'a';
		}
		getchar();
	}
	REP(i, N){

		REP(o, 20){
			REP(p,30)
				pattern[o][p]=0;
		}
		int pos = 0;
		bool opened = 0;
		while (true){
			char temp;
			scanf ("%c", &temp);
		//	printf ("%c\n", temp);
			if (temp == '\n'){
				int match = 0;
				REP(x, D){
					bool ok = 1;
					REP(c, L){
						if (!pattern[c][dictionary[x][c]])
							ok=0;
					}
					if (ok)
						match++;
				}
				printf ("Case #%d: %d\n", i+1, match);
				break;
			}
			else if(temp == '(')
				opened = 1;
			else if (temp == ')'){
				opened = 0;
				pos++;
			}
			else{
				pattern[pos][temp-'a'] = 1;
				if(!opened)
					pos++;
			}
		}
	}
	return 0;
}
