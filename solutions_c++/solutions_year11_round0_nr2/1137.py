#include <stdio.h>
#include <cstring>

int n, opp[300][300], opp_t, com_t, top;
char com[200][5], list[300], str[300];

int main()
{
	int t;
	scanf("%d", &t);
	for(int q=1; q<=t; ++q) {
		scanf("%d", &com_t);
		for(int i=0; i<com_t; ++i) scanf("%s", com[i]);
		scanf("%d", &opp_t);
		memset(opp, 0, sizeof opp);
		for(int i=0; i<opp_t; ++i) {
			char tmp[5];
			scanf("%s", tmp);
			int a = tmp[0] - 'A', b = tmp[1] - 'A';
			opp[a][b] = opp[b][a] = 1;
		}

		scanf("%d", &n);
		scanf("%s", str);
		top = 0;
		for(int i=0; i<n; ++i) {
			list[top++] = str[i];
			for(int j=0; j<com_t; ++j) {
				if(top < 2) break;
				if( (com[j][0] == list[top-2] && com[j][1] == list[top-1]) || (com[j][1] == list[top-2] && com[j][0] == list[top-1]) ) {
					top -= 2;
					list[top++] = com[j][2];
				}
			}
			for(int j=0; j<top; ++j) {
				for(int k=j+1; k<top; ++k) {
					if(opp[list[j]-'A'][list[k]-'A']) top = 0;
				}
			}
		}
		printf("Case #%d: [", q);
		for(int i=0; i<top; ++i) printf("%c%s", list[i], (i < top-1) ? ", " : "");
		puts("]");
	}
	return 0;
}

