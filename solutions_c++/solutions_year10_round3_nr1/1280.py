#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int A[1000], B[1000];

int main(){
	ifstream arq("teste.txt", ifstream::in);
	ofstream arq2("resultado.txt", ofstream::out);

	int T, N, K,i,j,count;
	
	arq >> T;//numero de testes
	
	for(int t=1; t!=T+1;t++){// para todos os casos:
		arq >> N;
		for(i=0;i<N;i++){
		arq >> A[i];//
		arq >> B[i];//
		}
		count=0;
		for(i=0;i<N;i++){ //
			 for(j=i+1;j<N;j++){
				 if((A[i]-A[j])*(B[i]-B[j]) < 0){
					 count++;
				 }
			 }
		}
		arq2 << "Case #" << t << ": " << count;
		if (t<T)
			arq2 << endl;
	}
	return 0;
}
