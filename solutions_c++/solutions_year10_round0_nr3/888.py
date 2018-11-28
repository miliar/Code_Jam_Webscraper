#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

#define TRACE(x) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

long long rodadas[1010], pessoas[1010];
int grupo[1010];

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
#if TRACE(1)+0
		printf("\nCase #%d: \n", _42);
#else
		printf("Case #%d: ", _42);
#endif
		memset(rodadas, -1, sizeof(rodadas));
		memset(pessoas, -1, sizeof(pessoas));

		int R, K, N;
		scanf(" %d %d %d", &R, &K, &N);
		for (int i=0; i < N; i++) scanf(" %d", &grupo[i]);

		long long euros = 0;
		int state = 0;
		long long Pessoas = 0;
		long long Rodadas = 0;
		while (rodadas[state] == -1 && Rodadas < R) {
			pessoas[state] = Pessoas;
			rodadas[state] = Rodadas;

			long long sum = 0;
			for (int i=0; i < N; i++) {
				if (sum+grupo[state] <= K) {
					sum += grupo[state];
					state = (state+1)%N;
				}
				else break;
			}

			euros += sum;
			Pessoas += sum;
			Rodadas++;
			PRINT("viagem %lld: %lld pessoas\n", Rodadas, sum);
		}
		if (Rodadas < R && rodadas[state] != -1) {
			PRINT("encontrou loop apos %lld rodadas\n", Rodadas);
			PRINT("state: %d  rodadas[state] = %lld  pessoas[state] = %lld\n", state, rodadas[state], pessoas[state]);
			PRINT("Rodadas = %lld  Pessoas = %lld\n", Rodadas, Pessoas);

			long long pessoas_loop = Pessoas - pessoas[state];
			long long rodadas_loop = Rodadas - rodadas[state];
			WATCH(pessoas_loop);
			WATCH(rodadas_loop);

			long long rodadas_sobrando = R - Rodadas;
			long long loops_possiveis = rodadas_sobrando / rodadas_loop;
			WATCH(rodadas_sobrando);
			WATCH(loops_possiveis);

			euros += loops_possiveis * pessoas_loop;
			Rodadas += loops_possiveis * rodadas_loop;

			PRINT("depois de executar os loops, faltam %lld rodadas\n", R - Rodadas);
			while (Rodadas < R) {
				long long sum = 0;
				for (int i=0; i < N; i++) {
					if (sum+grupo[state] <= K) {
						sum += grupo[state];
						state = (state+1)%N;
					}
					else break;
				}

				euros += sum;
				Rodadas++;
			}
		}
		
		printf("%lld\n", euros);
	}

	return 0;
}
