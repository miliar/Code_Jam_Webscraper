#include <cstdio>
#include <cstring>

int main()
{
	int T; scanf("%d\n", &T);
	for(int test=1; test<=T; test++) {
		int C, D;
		char Comb[110][3]; char Opos[110][2]; char Str[110];
		char Vysl[110]; int pos=0;
		scanf("%d ", &C); for(int i=0; i<C; i++) scanf("%c%c%c ", &Comb[i][0], &Comb[i][1], &Comb[i][2]);
		scanf("%d ", &D); for(int i=0; i<D; i++) scanf("%c%c ", &Opos[i][0], &Opos[i][1]);
		int N; scanf("%d %s\n", &N, Str);
		int yes[26]; for(int i=0; i<26; i++) yes[i]=0;
		yes[Str[0]-'A']++;
		Vysl[pos++]=Str[0];
		for(int i=1; i<N; i++) {
			int k=0; Vysl[pos++]=Str[i]; yes[Str[i]-'A']++;
		if(pos>1)	for(k=0; k<C; k++) if( (Comb[k][0]==Vysl[pos-2] && Comb[k][1]==Vysl[pos-1]) || (Comb[k][1]==Vysl[pos-2] && Comb[k][0]==Vysl[pos-1]) ) {yes[Vysl[pos-2]-'A']--; yes[Vysl[pos-1]-'A']--; yes[Comb[k][2]-'A']++; Vysl[pos-2]=Comb[k][2]; pos--; break;}
			if(k==C && pos>1) {
				for(int l=0; l<D; l++) if(yes[Opos[l][0]-'A'] && yes[Opos[l][1]-'A']) {pos=0; for(int aaa=0; aaa<26; aaa++) yes[aaa]=0; break;}
}
		}
		Vysl[pos]=0;
		if(strlen(Vysl)==0) printf("Case #%d: []\n", test);
		else {printf("Case #%d: [", test); for(int i=0; i<strlen(Vysl)-1; i++) printf("%c, ", Vysl[i]); printf("%c]\n", Vysl[strlen(Vysl)-1]);}
	}

	return 0;
}
