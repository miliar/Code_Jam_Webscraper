#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int tc, t, n, e, opp[300][300];
char s[105], S[105], com[300][300];

int main(){
	scanf("%d",&tc);
	for (int C=1; C<=tc; C++){

		memset(com, 0, sizeof(com));
		memset(opp, 0, sizeof(opp));

		scanf("%d", &n);
		while (n--){
			scanf("%s", s);
			com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
		}
		
		scanf("%d", &n);
		while (n--){
			scanf("%s", s);
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = 1;
		}
		
		scanf("%d%s", &n, s);
		t = 0;
		for (int i=0; i<n; i++){

			if (t>0 && com[S[t-1]][s[i]]!=0) S[t-1] = com[S[t-1]][s[i]];
			else{
				e = 0;
				for (int j=0; j<t; j++){
					if (opp[S[j]][s[i]]) e = 1;
				}
				if (e) t = 0;
				else S[t++] = s[i];
			}
		}
		
		S[t] = 0;
		printf("Case #%d: ", C);
		for (int i=0; i<t; i++) printf("%c%c%c", i?' ':'[', S[i], i<t-1?',':']');
		if (!t) printf("[]");
		printf("\n");
		
	}
	return 0;
}
