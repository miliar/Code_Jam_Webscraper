#include <iostream>
#include <cmath>
using namespace std;

bool magia(unsigned int cant, unsigned int pruebas){
	unsigned int limite = exp2(cant);
	pruebas %= limite;
	return (limite-1) == pruebas;
}

int main(int argc, char *argv[]) {
	int casos, K;
	unsigned int cant, pruebas;
	for(K=1, cin>>casos; K<=casos; K++){
		cin>>cant>>pruebas;
		cout<<"Case #"<<K<<": ";
		if(magia(cant, pruebas))
			cout<<"ON";
		else
			cout<<"OFF";
		cout<<endl;
	}
	return 0;
}

