#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

#define MAX 2001
long long val[MAX][2]; //0 -> Termina, //1-> Soma
long long values[MAX];
long long cycle[MAX],resp[MAX][2];
int main() {
	long long T,i,j,sum,begin,R,k,N,cur;
	scanf("%lld",&T);
	for (i = 1 ; i<= T ; i++) {
		scanf("%lld %lld %lld",&R,&k,&N);
		for (j = 0 ; j < N ; j++) {
			scanf("%lld",&values[j]);
			cycle[j] = -1;
		}
		for (j = N ; j < 2*N ; j++)
			values[j] = values[j-N];
		for (j = 0 ; j < N ; j++) {
			val[j][1] = 0;
			val[j][0] = j-1;
			sum = values[j];
			begin = j;
			cur = j;
			while (sum <= k) {
				if (cur != begin && cur%N == begin)
					break;		
				val[j][0] = sum;
				val[j][1] = cur%N;
				cur += 1;
				sum += values[cur%N];
			}
		//	printf("Comecando de %lld consigo soma %lld e termino em %lld\n",begin,val[j][0],val[j][1]);
		}
		long long scur = 0,curcity=0,tot=0;
		cycle[N] = 0;
		resp[0][0] = N;
		while (R--) {
			if (cycle[curcity] == - 1) {
				scur += val[curcity][0];
				cycle[curcity] = scur;
		
				resp[curcity][1] = ++tot;	
				if (cycle[val[curcity][1]+1] != -1) { //Cycle
									
					long long elements = tot-resp[ ( val[curcity][1]+1)%N ][1] + 1;
					//printf("%lld %lld - %lld\n",elements,cycle[curcity],cycle[resp[val[curcity][1]+1][0]]);
					if (elements == 1) {
						scur += val[curcity][0]*R;
					}
					else scur += (cycle[curcity]-cycle[ resp[ (val[ curcity][1]+1)% N ][0] ])*(R/elements);
					long long restam = R%elements;
					curcity = (val[curcity][1]+1)%N;
					while (restam--) {
						scur += val[curcity][0];
						curcity = val[curcity][1]+1;
						curcity %= N;
					}
					break;
				}
					resp[val[curcity][1]+1][0] = curcity;	
				curcity = val[curcity][1]+1;	
			}
		}
		printf("Case #%lld: %lld\n",i,scur);
		
	}
	return 0;
}
