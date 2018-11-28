#include <iostream>
#include <string.h>

using namespace std;

int main(){
	int T;
	int caso = 1;
	cin >> T;
	for (int caso=1; caso <= T; caso++){
		int R, k, N;

		cin >> R >> k >> N;

		int q[1000];
		long long int cuantos[1000];
		long long int hasta_donde[1000];

		for (int i=0;i<N;i++){
			int g;
			cin >> g;
			q[i] = g;
		}

		memset(cuantos,0,sizeof cuantos);

		for (int i=0;i<N;i++){
			int j=i;
			while(j<N && cuantos[i] + q[j] <= k){
				cuantos[i] += q[j];
				j++;
			}

			if (j<N){
				hasta_donde[i] = j;
			} else {
				j=0;
				while(j<i && cuantos[i] + q[j] <= k){
					cuantos[i] += q[j];
					j++;
				}
				hasta_donde[i] = j;
			}
		}

		long long int sol = 0;
		int esta = 0;
		for (int i=0;i<R;i++){
			sol += cuantos[esta];
			esta = hasta_donde[esta];
		}

		cout << "Case #" << caso << ": " << sol << endl;
	}

	return 0;
}