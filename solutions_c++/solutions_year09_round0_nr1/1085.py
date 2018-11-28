#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

char D[5000][16];
char q[512];

bool match(int k) {
	int i,p = 0;
	bool found;
	for (i=0;i<strlen(q);++i) {
		if (q[i] == '(') {
			found = false;
			while (q[i] != ')') {
				if (q[i] == D[k][p]) found = true;
				i++;
			}
			if (!found) return false;
		} else {
			if (q[i] != D[k][p]) return false;
		}
		++p;
	}
	return true;
}

int main() {
	
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int L,D1,N,i,j,res;
	
	scanf("%d%d%d\n",&L,&D1,&N);
	
	for (i=0;i<D1;++i)
		for (j=0;j<=L;++j) scanf("%c",&D[i][j]);
		
	for (i=0;i<N;++i) {
		res = 0;
		memset(q,0,sizeof(q));
		fgets(q,sizeof(q),stdin);
		
		for (j=0;j<D1;++j) {
				if (match(j)) res++;
		}
		
		printf("Case #%d: %d\n",i+1,res);		
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}