#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

char comb[1000][5], oppo[1000][5], s[1000];
int T,C,D,N;

char combine(char A, char B){
	if (A > B) swap(A,B);
	REP(i,C) if (comb[i][0]==A && comb[i][1]==B) return comb[i][2];
	return 0;
}

bool oppose(int S){
	REP(i,S-1){
		char A = s[i], B = s[S-1];
		if (A > B) swap(A,B);
		REP(j,D) if (oppo[j][0]==A && oppo[j][1]==B) return true;
	}
	return false;
}

int main(){
	scanf("%d",&T);
	REP(tc,T){
		scanf("%d",&C); REP(i,C) scanf("%s",comb[i]);
		scanf("%d",&D); REP(i,D) scanf("%s",oppo[i]);
		scanf("%d %s",&N,s);

		REP(i,C) if (comb[i][0] > comb[i][1]) swap(comb[i][0], comb[i][1]);
		REP(i,D) if (oppo[i][0] > oppo[i][1]) swap(oppo[i][0], oppo[i][1]);

		int S = 0;
		REP(i,N){
			s[S++] = s[i];
			while (S>1){
				char c = combine(s[S-2],s[S-1]);
				if (c) s[S-2] = c, S--; else break;
			}
			if (oppose(S)) S = 0;
		}

		printf("Case #%d: [",tc+1);
		REP(i,S){
			if (i>0) printf(", ");
			printf("%c",s[i]);
		}
		puts("]");
		fflush(stdout);
	}
}
