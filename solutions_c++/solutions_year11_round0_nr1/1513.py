#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


int pos[2], n, at, t, target[110], type[110], last, custo, num, tempo, cn;
char color[10];

int main() {
	int cases;
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d",&n);
		pos[0]=pos[1]=1;
		for (t=0; t < n; ++t) {
			scanf("%s %d",color,&num);
			target[t] = num;
			if (color[0]=='O') type[t] = 0;
			else type[t] = 1;
		}
		
		t=0;
		tempo=0;
		at=0;
		last=2;
		
		while (t < n) {
			custo = abs( pos[ type[t] ] - target[t] );
			if ( last != type[t] ) {
				custo -= at;
				if ( custo < 0 ) custo=0;
				at=0;
			}
			pos[ type[t] ] = target[t];
			tempo += ++custo;
			at += custo;
			last = type[t++];
		}
		
		printf("Case #%d: %d\n", ++cn, tempo);
		
		
	}
	return 0;
}
