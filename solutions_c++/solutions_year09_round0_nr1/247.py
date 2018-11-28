#include <cstdio>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstring>
using namespace std;

string palavras[5000];

char palavra[16][32];
char npalavra[16];

char atual[16];
int L,D,N;

int procura(int p) {
	if(p==L) {
		if(binary_search(palavras,palavras+D,atual))
			return 1;
		return 0;
	}
	int ans=0;
	for(int i=0;i<npalavra[p];i++) {
		atual[p]=palavra[p][i];
		atual[p+1]=0;
		if((lower_bound(palavras,palavras+D,atual)!= palavras+D) and (lower_bound(palavras,palavras+D,atual)->substr(0,p+1) == atual))
			ans+=procura(p+1);
	}
	return ans;
}

int main(void) {
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;i++)
		cin >> palavras[i];

	sort(palavras,palavras+D);

	for(int T=1;T<=N;T++) {
		memset(npalavra,0,sizeof(npalavra));
		for(int k=0;k<L;k++) {
			char c;
			cin >> c;
			if(c=='(') {
				while( (cin >> c) and c!=')' ) {
					palavra[k][npalavra[k]++]=c;
				}
			}
			else {
				palavra[k][0]=c;
				npalavra[k]=1;
			}
		}
		printf("Case #%d: %d\n",T,procura(0));
	}
	return 0;
}
