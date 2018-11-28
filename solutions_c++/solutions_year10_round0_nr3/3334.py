#include <iostream>
#include <fstream>

using namespace std;

int main () {
	
	ifstream arq( "teste.txt", ifstream::in );
	ofstream arq2("resultado.txt", ofstream::out);
	long int T, R, k, N, usuarios =0, pos, qtd;
	arq >> T;
	for(long int caso = 1; caso <= T; caso++){ //volta
		pos =0;
		arq >> R;//qtd de voltas da montanha russa
		arq >> k;// capacidade da MR
		arq >> N;//qtd de grupos
		long int grupo[10000];
		for(long int i = 0; i < N; i++) //pega os grupos
			arq >> grupo[i];
		for(long int v=0;v<R;v++){ //para cada volta da montanha russa
			qtd=0;
			long int repete = pos;
			while(qtd+grupo[pos] <= k){ //enquanto puder botar + gente na MR
				qtd += grupo[pos];
				pos++;
				if (pos == N)
					pos = 0;
				if (pos == repete)
					break;
			}
			usuarios += qtd;
		}
		arq2 << "Case #" << caso <<": "<< usuarios;
		if(caso < T)
			arq2 << endl;
		usuarios = 0;
	}
	
	return 0;
}
