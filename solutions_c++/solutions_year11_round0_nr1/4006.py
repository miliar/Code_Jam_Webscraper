#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
	int t, caso = 1;
	scanf("%d", &t);
	while(t--) {
		int n, o1 = 0, b1 = 0, butt = 0;
		scanf("%d", &n);
		int b[n], o[n], u;
		char indc[n];
		bool oe = false, be = false;
		for(int i = 0; i < n; ++i) {
			scanf(" %c", &indc[i]);
			scanf("%d", &u);
			if(indc[i] == 'B') {
				b[b1] = u;
				++b1;
			}
			if(indc[i] == 'O') {
				o[o1] = u;
				++o1;
			}
		}
		o1 = 0; b1 = 0;
		long long int postb = 1, posto = 1, acum = 0, secs = 0, aux2 = 0;
		char aux = indc[0];
		for(int i = 0; i < n; ++i) {
			if(aux == indc[i] && aux == 'B') {
				acum += abs(b[b1] - postb) +1;
				secs += abs(b[b1] - postb) +1;
				postb = b[b1];
				aux = 'B';
				++b1;
			}
			if(aux == indc[i] && aux == 'O') {
				acum += abs(o[o1] - posto) +1;
				secs += abs(o[o1] - posto) +1;
				posto = o[o1];
				aux = 'O';
				++o1;
			}
			if(aux != indc[i] && indc[i] == 'O') {
				if(acum > abs(o[o1] - posto)) {
					secs += 1;
					acum = 1;
					posto = o[o1];
					aux = 'O';
					++o1;
				}
				else {
				secs += abs(o[o1] - posto) +1 - acum;
				aux2 = abs(o[o1] - posto) +1 - acum;
				acum = aux2;
				posto = o[o1];
				aux = 'O';
				++o1;
				}
			}
			if(aux != indc[i] && indc[i] == 'B') {
				if(acum > abs(b[b1] - postb)) {
					secs += 1;
					acum = 1;
					postb = b[b1];
					aux = 'B';
					++b1;
				}
				else {
				secs += abs(b[b1] - postb) +1 - acum;
				aux2 = abs(b[b1] - postb) +1 - acum;
				acum = aux2;
				postb = b[b1];
				aux = 'B';
				++b1;
				}
			}
		}
		printf ("Case #%d: %lld\n", caso, secs);
		++caso;
	}
	return 0;
	}
