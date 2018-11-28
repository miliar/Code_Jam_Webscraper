#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream arq("teste.txt", ifstream::in);
	ofstream arq2("resultado.txt", ofstream::out);
	int status;
	long long int T, N, K, potN;
	arq >> T;
	for(int casos=1;casos<=T;casos++){
		status = 1;
		potN = 1;
		arq >> N;//numero de lampadas
		arq >> K;//numero de estalos
		for(int i=1;i <= N ; i++){
			//cout << potN << " "<< K << endl;
			//cout << 1*(potN & K)  << endl;
			if ((potN & K) == 0){
				//cout << potN << " "<< K << endl;
				status =0;
				break;
			}
			potN *=2;
		}
		arq2 << "Case #" << casos << ": ";
		if (status)
			arq2 << "ON";
		else
			arq2 << "OFF";
		if(casos < T)
			arq2 << endl;
	}
	return 0;
}
