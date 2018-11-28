#include <cstdio>
#include <algorithm>

using namespace std;
int com[26][26];
bool opp[26][26];
int stack[200];
int n, m, t, c;
char s[100];

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);


	scanf("%d", &t);
	for (int k = 1; k <= t; k++){
		memset(com, 0, sizeof(com));
		memset(opp, 0, sizeof(opp));
		scanf("%d", &c);
		for (int i = 0; i < c; i++){
			scanf("%s", s);
			com[s[0]-'A'][s[1]-'A'] = s[2] - 'A';
			com[s[1]-'A'][s[0]-'A'] = s[2] - 'A';
		}
		scanf("%d", &c);
		for (int i = 0; i < c; i++){
			scanf("%s", s);
			opp[s[0] - 'A'][s[1] - 'A'] = 1;
			opp[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		scanf("%d%s", &n, s);
		m = 0;
		for (int i = 0; i < n; i++){
			stack[m++] = s[i] - 'A';
			if (m > 1 && com[stack[m - 1]][stack[m - 2]]){
				stack[m - 2] = com[stack[m - 1]][stack[m - 2]];
				m--;
			}
			for (int j = 0; j < m - 1; j++)
				if (opp[stack[j]][stack[m - 1]]){
					m = 0;
					break;
				}
		}
		printf("Case #%d: [", k);
		for (int i = 0; i < m; i++)
			if (i < m - 1) printf("%c, ", stack[i] + 'A');
			else printf("%c", stack[i] + 'A');
		printf("]\n");
	}
	return 0;
}