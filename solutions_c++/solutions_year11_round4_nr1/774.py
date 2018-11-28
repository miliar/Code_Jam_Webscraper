#include <cstdio>
#include <cstdlib>
#include <cstring>

long double chodnik[2100][3];

int comp(const void *a, const void *b)
{
	return chodnik[(*(int *)b)][2]>chodnik[(*(int *)a)][2] ? 1 : -1;
}

int main()
{
	int T; scanf("%d", &T);
	for(int test=1; test<=T; test++) {
		int X, S, R, t, N; scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
		int udaje[1000][3];
		
		int id=0;
		int konec=0;
		for(int i=0; i<N; i++) scanf("%d%d%d", &udaje[i][0], &udaje[i][1], &udaje[i][2]);
		for(int i=0; i<N; i++) {
			if(udaje[i][0]==konec) {
				chodnik[id][0]=udaje[i][1]-udaje[i][0];
				chodnik[id][1]=udaje[i][2];
				id++;
				konec=udaje[i][1];
			}
			else {
				chodnik[id][0]=udaje[i][0]-konec;
				chodnik[id][1]=0;
				id++;
				chodnik[id][0]=udaje[i][1]-udaje[i][0];
				chodnik[id][1]=udaje[i][2];
				id++;
				konec=udaje[i][1];
			}
		}
		if(konec!=X) {
			chodnik[id][0]=X-konec;
			chodnik[id][1]=0;
			id++;
		}
	//for(int i=0; i<id; i++) printf("%.1Lf %.1Lf\t", chodnik[i][0], chodnik[i][1]); printf("\n");
		for(int i=0; i<id; i++) {
			chodnik[i][2]=1/(chodnik[i][1]+S)-1/(chodnik[i][1]+R);
		}
		int cisla[2100]; for(int i=0; i<id; i++) cisla[i]=i;
		qsort(cisla, id, sizeof(int), comp);
	//for(int i=0; i<id; i++) printf("%Lf ", chodnik[i][2]); printf("\n");
	//for(int i=0; i<id; i++) printf("%d ", cisla[i]); printf("\n");
		long double cas=t;
		long double vysledek=0;
		int idx=0;
		for(int i=0; i<id; i++) vysledek+=((long double)chodnik[i][0])/(chodnik[i][1]+S);
		//printf("%Lf\n", vysledek);
		while(cas>0 && idx<id) {
			if(cas>=chodnik[cisla[idx]][0]/(chodnik[cisla[idx]][1]+R)) {
				cas-=chodnik[cisla[idx]][0]/(chodnik[cisla[idx]][1]+R);
				vysledek-=chodnik[cisla[idx]][0]/(chodnik[cisla[idx]][1]+S);
				vysledek+=chodnik[cisla[idx]][0]/(chodnik[cisla[idx]][1]+R);
				//printf("%d ", cisla[idx]);
			}
			else {
				vysledek-=(cas*(chodnik[cisla[idx]][1]+R))/(chodnik[cisla[idx]][1]+S);
				vysledek+=(cas*(chodnik[cisla[idx]][1]+R))/(chodnik[cisla[idx]][1]+R);
				cas=0;
			}
			idx++;
		}
	
		printf("Case #%d: %Lf\n", test, vysledek);
	}

	return 0;
}
