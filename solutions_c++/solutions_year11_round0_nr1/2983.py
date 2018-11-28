#include <cstdio>
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MINIM(a, b) ((a)<(b) ? (a) : (b))

int main()
{
	int T; scanf("%d\n", &T);
	for(int test=1; test<=T; test++) {
		int N; scanf("%d ", &N);
		int blue=1, orange=1;
		int secs=0;
		int orcom[100], blcom[100];
		int orpos=0, blpos=0;
		bool oran[100];
		for(int i=0; i<N; i++) {
			char c; int pos; scanf("%c", &c); scanf(" %d ", &pos);
			if(c=='O') {orcom[orpos++]=pos; oran[i]=true;}
			else {blcom[blpos++]=pos; oran[i]=false;}
		}
		int op=0, bp=0;
		for(int i=0; i<N; i++) {
			secs+=(oran[i] ? ABS(orcom[op]-orange)+1 : ABS(blcom[bp]-blue)+1);
				if(oran[i]) {if(bp!=blpos) {if(blcom[bp]<blue) {blue-=MINIM(ABS(blue-blcom[bp]), ABS(orcom[op]-orange)+1);} else {blue+=MINIM(ABS(blue-blcom[bp]), ABS(orcom[op]-orange)+1);}}}
				else {if(op!=orpos) {if(orcom[op]<orange) {orange-=MINIM(ABS(orange-orcom[op]), ABS(blcom[bp]-blue)+1);} else {orange+=MINIM(ABS(orange-orcom[op]), ABS(blcom[bp]-blue)+1);}}}
				if(oran[i]) orange=orcom[op++]; else blue=blcom[bp++];
		}
		printf("Case #%d: %d\n", test, secs);
		scanf("\n");
	}

	return 0;
}
