#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<memory.h>
#include<algorithm>
using namespace std;

struct trip_t {
	int dep,arr;
};
bool operator < (trip_t x, trip_t y) {
	if ( x.dep == y.dep ) return x.arr < y.arr;
	else return x.dep < y.dep;
}

int gettime(char* s) {
	int ho,se;
	char *p;
	ho = se = 0;
	p = s;
	while ( *p != ':' ) {
		ho = ho * 10 + (*p-'0');
		++p;
	}
	++p;
	while ( *p != 0 ) {
		se = se * 10 + (*p-'0');
		++p;
	}
	return ho*60+se;
}


int T, NA, NB;
trip_t trA[1280], trB[1280];
int pA,pB;
int ra, rb;
int stA[1280],nsA, stB[1280],nsB;

bool cmp(int a , int b) {
	return a>b;
}

int main(int argc, char* argv[]) {
	int N;
	int nc;
	char tdep[16], tarr[16];
	nc = 0;
	scanf("%d", &N);
	while (N--) {
		scanf("%d", &T);
		scanf("%d%d", &NA, &NB);
		for ( int i = 0 ; i < NA ; ++i ) {
			scanf("%s%s", tdep, tarr);
			trA[i].dep = gettime(tdep);
			trA[i].arr = gettime(tarr);
		}
		for ( int i = 0 ; i < NB ; ++i ) {
			scanf("%s%s", tdep, tarr);
			trB[i].dep = gettime(tdep);
			trB[i].arr = gettime(tarr);
		}

		sort(trA, trA+NA);
		sort(trB, trB+NB);


		nsA = nsB = 0;
		pA = pB = 0;
		ra = rb = 0;

		for ( int i = 0 ; i < 24*3600 ; ++i ) {
			while ( pA < NA && trA[pA].dep == i ) {
				if ( nsA > 0 && stA[0] <= i ) {
					pop_heap(stA, stA+nsA, cmp);
					--nsA;
					stB[nsB++] = trA[pA].arr + T;
					push_heap(stB, stB+nsB, cmp);
				} else {
					++ra;
					stB[nsB++] = trA[pA].arr + T;
					push_heap(stB, stB+nsB, cmp);
				}
				++pA;
			}
			
			while ( pB < NB && trB[pB].dep == i ) {
				if ( nsB > 0 && stB[0] <= i ) {
				//	printf("nsB = %d, stB[0] = %d\n",nsB, stB[0], i);
					pop_heap(stB, stB+nsB, cmp);
					--nsB;
					stA[nsA++] = trB[pB].arr + T;
					push_heap(stA, stA+nsA, cmp);
				} else {
				//	printf("nsB = %d, stB[0] = %d\n",nsB, stB[0], i);
					++rb;
					stA[nsA++] = trB[pB].arr + T;
					push_heap(stA, stA+nsA, cmp);
				}
				++pB;
			}
		}

		++nc;
		printf("Case #%d: %d %d\n", nc, ra, rb);
	}
	return 0;
}
