#include <cstdio>
#include <cstdlib>
#include <cstring>

void projdi(int vrchol);
int graf[410][410];
int d[410];
int suma;
int P, W;
bool ohrozuje[410], naceste[410];

int main()
{
	int T; scanf("%d", &T);
	for(int test=1; test<=T; test++) {
		scanf("%d%d", &P, &W);
		for(int i=0; i<P; i++) graf[i][0]=0;
		for(int i=0; i<P; i++) d[i]=10000;
		d[0]=0;
		for(int i=0; i<W; i++) {
			int a, b; scanf("%d,%d", &a, &b);
			graf[a][++graf[a][0]]=b;
			graf[b][++graf[b][0]]=a;
		}
		int fronta[410]; fronta[0]=0; int zac=0, kon=0;
		while(zac<=kon) {
			int akt=fronta[zac++];
			for(int i=1; i<=graf[akt][0]; i++) if(d[graf[akt][i]]==10000) {
				d[graf[akt][i]]=d[akt]+1;
				fronta[++kon]=graf[akt][i];
			}
		}
	//for(int i=0; i<P; i++) printf("%d ", d[i]); printf("\n");
		for(int i=0; i<P; i++) naceste[i]=false;
		suma=0;
		for(int i=1; i<=graf[1][0]; i++) if(d[graf[1][i]]==d[1]-1) projdi(graf[1][i]);	
	
		printf("Case #%d: %d %d\n", test, d[1]-1, suma);
	}

	return 0;
}

void projdi(int vrchol)
{
	if(d[vrchol]==0) {
		int s=0;
		for(int i=0; i<P; i++) ohrozuje[i]=false;
		naceste[0]=true;
		for(int i=0; i<P; i++) {
			if(naceste[i]) {for(int j=1; j<=graf[i][0]; j++) if(!naceste[graf[i][j]]) ohrozuje[graf[i][j]]=true;}
		}
		for(int i=0; i<P; i++) if(ohrozuje[i]) s++;
	//for(int i=0; i<P; i++) printf("%d ", naceste[i]); printf("\n");
	//for(int i=0; i<P; i++) printf("%d ", ohrozuje[i]); printf("\n");
		naceste[0]=false;
		if(s>suma) suma=s;
		return;
	}
	naceste[vrchol]=true;
	for(int i=1; i<=graf[vrchol][0]; i++) {
		if(d[graf[vrchol][i]]==d[vrchol]-1) projdi(graf[vrchol][i]);
	}
	naceste[vrchol]=false;
}
