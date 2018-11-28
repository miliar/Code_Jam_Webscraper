#include <iostream>
#include <string>
#include <vector>
using namespace std;

enum contestant {Red, Blue, Both, Neither};

vector<string> tablero;

void salida(contestant win){
	switch(win){
	case Red:
		cout<<"Red"; break;
	case Blue:
		cout<<"Blue"; break;
	case Both:
		cout<<"Both"; break;
	case Neither:
		cout<<"Neither"; break;
	}
	cout<<endl;
}

void input(int tam){
	tablero.clear();
	tablero.resize(tam);
	for(int K=0; K<tam; K++)
		cin>>tablero[K];
}
void rotar(){
	int tam = tablero.size();
	string s;
	for(int K=0; K<tam; K++){
		for(int L=tam-1; L>=0; L--){
			if(tablero[K][L] == '.'){
				tablero[K].erase(tablero[K].begin()+L);
			}
		}
		//volver al tamanio original
		tablero[K].insert(0, tam-tablero[K].size(), '.');
	}
}

bool buscarlinea(int x, int y, int cant, int dx, int dy){
	char caracter = tablero[x][y];
	int tam = tablero.size();
	for(int K=x, L=y; cant>0; cant--, K+=dx, L+=dy){
		if(K<0 || L<0 || K==tam||L==tam) return false;
		if(tablero[K][L] != caracter) return false;
	}
	return true;
}

contestant ganador(int linea){
	//buscar una linea con la longitud deseada
	bool rojo=false, negro=false;
	int tam=tablero.size();
	for(int K=0; K<tam; K++){
		for(int L=0; L<tam; L++){
			if(tablero[K][L]!='.')
				if(buscarlinea(K, L, linea, 1, 0)||buscarlinea(K, L, linea, 0, -1)||buscarlinea(K, L, linea, -1, -1)||buscarlinea(K, L, linea, 1, -1)){
					if(tablero[K][L]=='R') rojo = true;
					else negro = true;
				}
		}
	}
	
	if(rojo && negro) return Both;
	if(rojo) return Red;
	if(negro) return Blue;
	return Neither;
}

void print(){
	int tam = tablero.size();
	cout<<"Debug"<<endl;
	for(int K=0; K<tam; K++)
		cout<<tablero[K]<<endl;
	cout<<endl;
}

int main(int argc, char *argv[]) {
	int casos, K, tam, linea;
	contestant win;
	for(K=0, cin>>casos; K<casos; K++){
		cin>>tam>>linea;
		input(tam);
//		print();
		rotar();
		
		win = ganador(linea);
		cout<<"Case #"<<K+1<<": ";
		salida(win);
		
//		print();
	}
	return 0;
}

