#include <iostream>

using namespace std;

int main (int argc, char * const argv[]) {
    long T, N, i, j, P1, P2, Step1, Step2, M1, M2;
	char R;
	
	cin >> T;
	for (i=0; i < T; i++) {
		P1 = 1;
		P2 = 1;
		Step1 = 0;
		Step2 = 0;
		j = 0;
		
		cin >> N;
		do {
			j++;
			cin >> R;
			switch (R) {
				case 'O':
					cin >> M1;
					if (int(abs(M1 - P1)) + Step1 > Step2) 
						Step1 += int(abs(M1 - P1)) + 1;
					else Step1 = Step2 + 1;
					P1 = M1;
					break;
				case 'B':
					cin >> M2;
					if (int(abs(M2 - P2)) + Step2 > Step1) 
						Step2 += int(abs(M2 - P2)) + 1;
					else Step2 = Step1 + 1;
					P2 = M2;
					break;
			}
		} while (j < N);
		printf("Case #%ld: %ld\n", i+1, Step1 > Step2 ? Step1 : Step2 );
	}
	
    return 0;
}
