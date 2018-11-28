#include<stdio.h>
#include<algorithm>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))

struct trip {
	int st,en;
	int flag;
}ta[105],tb[105];

bool comp1(trip a,trip b) {
	return a.st < b.st ;
}

int main() {
	int i,T,kase=1,na,nb,turn;
	int h1,h2,m1,m2;
	int sa,sb;
	int mina,minb;
	int pos,tim;
	int posa,posb;
	scanf("%d",&T);
	while(T--) {
		scanf("%d",&turn);
		scanf("%d%d",&na,&nb);
		for(i=0;i<na;i++) {
			scanf("%02d:%02d %02d:%02d",&h1,&m1,&h2,&m2);
			ta[i].st = h1 * 60 + m1;
			ta[i].en = h2 * 60 + m2;
			ta[i].flag = 0;
		}

		for(i=0;i<nb;i++) {
			scanf("%02d:%02d %02d:%02d",&h1,&m1,&h2,&m2);
			tb[i].st = h1 * 60 + m1;
			tb[i].en = h2 * 60 + m2;
			tb[i].flag = 0;
		}

		sa = sb = 0;
		while(1) {
			//sort(ta,ta+na,comp1); sort(tb,tb+nb,comp1);
			mina = minb = 15000;
			for(i=0;i<na;i++) if(ta[i].flag == 0) mina = min(mina,ta[i].st);
			for(i=0;i<nb;i++) if(tb[i].flag == 0) minb = min(minb,tb[i].st);
			if(mina == 15000 &&  minb == 15000) break;
			if(mina <= minb) {
				sa++;
				pos = 1;
			}
			else {
				sb++;
				pos = 2;
			}
			tim = -1;
			while(1) {
				if(pos == 1) {
					mina = 15000;
					for(i=0;i<na;i++) if(ta[i].flag == 0) {
						if(ta[i].st >= tim) {
							if(ta[i].st < mina) {
								mina = ta[i].st;
								posa = i;
							}
						}
					}
					if(mina == 15000) break;
					tim = ta[posa].en + turn;
					ta[posa].flag = 1;
					pos = 2;
				}
				else {
					minb = 15000;
					for(i=0;i<nb;i++) if(tb[i].flag == 0) {
						if(tb[i].st >= tim) {
							if(tb[i].st < minb) {
								minb = tb[i].st;
								posb = i;
							}
						}
					}
					if(minb == 15000) break;
					tim = tb[posb].en + turn;
					pos = 1;
					tb[posb].flag = 1;
				}
			}//while 1
		}//while 1
		printf("Case #%d: %d %d\n",kase++,sa,sb);
	}
	return 0;
}