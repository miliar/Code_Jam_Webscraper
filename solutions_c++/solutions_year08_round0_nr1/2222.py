#include <iostream>
#include <string>

using namespace std;

#define MAXS 128
#define MAXQ 1024
#define INF 999999999

int d[MAXQ][MAXS];

int main(){
	int N, Q, S;
	string searchEngines[MAXS];
	string query, tmp;
	int queries[MAXQ];
	cin >> N;
	for(int X = 1; X <= N; X++){
		cin >> S; getline(cin, tmp);

		for(int i = 0; i < S; i++){
			getline(cin, searchEngines[i]);
			//cout << searchEngines[i] << endl;
		}
		cin >> Q; getline(cin, tmp);
		for(int i = 0; i < Q; i++){
			getline(cin, query);
			for(int k = 0; k < S; k++)
				if(query == searchEngines[k]){
					queries[i] = k;
					break;
				}
		}

		for(int s = 0; s < S; s++)
			d[Q-1][s] = 0;
		d[Q-1][queries[Q-1]] = INF;

		for(int q = Q-2; q >= 0; q--)
			for(int s = 0; s < S; s++){
				if(queries[q] == s)
					d[q][s] = INF;
				else{
					//Cerco la prima occorrenza di s più avanti
					int j;
					for(j = q+1; j < Q; j++)
						if(queries[j] == s)
							break;
					if (j == Q){
						//non trovato
						d[q][s] = 0;
					} else {
						//restituisco 1 + min(d[j][i] per i = 0..s)
						int min = INF;
						for(int i = 0; i < S; i++)
							if(d[j][i] < min)
								min = d[j][i];
						d[q][s] = 1 + min;
					}
					
				}
			}
		
		int min = INF;
		for(int i = 0; i < S; i++)
			if(d[0][i] < min)
				min = d[0][i];
		
		cout << "Case #" << X << ": " << min << endl;
	}
	return 0;
}
