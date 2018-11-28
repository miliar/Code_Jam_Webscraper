#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned int uint;

uint gcd(uint a, uint b){
	if(b==0) return a;
	return gcd(b, a%b);
}

uint magia(vector<uint> &suceso){
	uint result, resta;
	sort(suceso.rbegin(), suceso.rend());
	//el gcd de todas las restas
	result = suceso[0] - suceso[1];
	for(uint K=0; K+1 < suceso.size(); K++){
		for(uint L= K+1; L < suceso.size(); L++){
			resta = suceso[K] - suceso[L];
			
//			cout<<"Dep "<<result<<' '<<resta<<endl;
			result = gcd(max(result, resta), min(result, resta));
		}
	}
	return result;
}

int main(int argc, char *argv[]) {
	uint K, casos, resultado, tam, armag;
	vector<uint> suceso;
	
	for(K=1, cin>>casos; K<=casos; K++){
		cin>>tam;
		suceso.clear(); suceso.resize(tam);
		for(uint L=0; L<suceso.size(); L++)
			cin>>suceso[L];
		resultado = magia(suceso);
		
//		cout<<resultado<<endl;
		//resultado tiene el maximo divisor
		
		armag = (resultado - (suceso[tam-1] % resultado) )%resultado ;
		
//		cout<<"Case #"<<K<<": "<<armag<<endl;
		cout<<"Case #"<<K<<": "<<armag<<endl;
	}
	return 0;
}

