#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cstdlib>

using namespace std;

char engine[200][201];
char query[2001][201];
char buff[1000];

int next[2001][201];

int getInt(void){
	gets(buff);
	return atoi(buff);
}

int main (void){
	int N, S, Q, i, j, k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	N = getInt();
	for(int n=1;n<=N;++n){
		S = getInt();
		for( i = 0; i < S; ++i ){
			gets(engine[i]);
		}
		Q = getInt();
		for( i = 0; i < Q; ++i){
			gets(query[i]);
		}
		
		for(i = 0; i<S; ++i){
			next[Q][i] = Q;
		}

		for(i = Q-1; i>=0; --i){
			for(j=0; j<S; ++j){
				if(strcmp(query[i], engine[j])==0){
					next[i][j] = i;
				}
				else next[i][j]=next[i+1][j];
			}
		}

		int pos = 0;
		int res = 0;
		while(pos<Q){
			res++;

			int m = 0;
			for(i=1;i<S;++i){
				if(next[pos][i]>next[pos][m])m=i;
			}
			pos = next[pos][m];
		}
		if(res)res--;
		printf("Case #%d: %d\n",n,res);
	}

	return 0;
}