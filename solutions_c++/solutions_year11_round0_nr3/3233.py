#include<stdio.h>

int soma (int a, int b) { return (a+b - ((a&b)<<1)); }
int n, best, proibido;
int v[10000];

void bt ( int index, int sean, int patrick, int verdade ) {
	if ( index == n ) {
		if ( sean == patrick && verdade < proibido ) best = ( verdade > best ? verdade : best );
		return;
	}
	
	bt(index+1, soma(sean,v[index]), patrick, verdade);
	bt(index+1, sean, soma(patrick,v[index]), verdade+v[index]);
}

int main (void) {
	int t,cont = 1;
	scanf("%d",&t);
	while (t--) {
		best = proibido = 0;
		scanf("%d",&n);
		for ( int i = 0; i < n; i++ ) { scanf("%d",&(v[i])); proibido += v[i]; }
		bt (0,0,0,0);
		if ( best == 0 ) printf("Case #%d: NO\n",cont++);
		else printf("Case #%d: %d\n",cont++,best);
	}
	
	return 0;
}
