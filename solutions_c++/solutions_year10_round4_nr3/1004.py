#include <iostream>
#include <vector>
using namespace std;

vector<vector<char> > tablero, vacio;

int lim=101;

//typedef unsigned long long int ulli;

enum vida{nada=0, viva=1, nace=2, muere=3};

void iniciar(){
	tablero.resize(lim, vector<char> (lim, nada));
	vacio.resize(lim, vector<char> (lim, nada));
}

bool nacer(int x, int y){
	if(x==0 || y==0) return false;
	return (tablero[x-1][y]==viva && tablero[x][y-1]==viva);
}

bool morir(int x, int y){
	if(x==0 && y==0) return true;
	if(x==0) return tablero[x][y-1]==nada;
	if(y==0) return tablero[x-1][y]==nada;
	return (tablero[x-1][y]==nada && tablero[x][y-1]==nada);
}

void actualizar(){
	
}

void print(){
	int K,L;
	for(K=0; K<tablero.size(); K++){
		for(L=0; L<tablero.size(); L++){
			if(tablero[K][L]==viva)
				cout<<1;
			else
				cout<<0;
		}
		cout<<endl;
	}
}

void llenar(int x1, int y1, int x2, int y2){
	int K, L;
	for(K=x1; K<=x2; K++){
		for(L=y1; L<=y2; L++){
			tablero[K][L]=1;
		}
	}
}

void lectura(){
//	cout<<endl<<endl;
//	print();cout<<endl;
	int K;
	int x1, y1, x2, y2;
	for(cin>>K; K>0; K--){
		cin>>x1>>y1>>x2>>y2;
		llenar(x1,y1,x2,y2);
	}
//	cout<<"Inicio"<<endl;
//	print();
//	cout<<endl;
}

void simular(){
	int K, L;
	for(K = tablero.size()-1; K >= 0; K--){
		for(L = tablero.size()-1; L >= 0; L--){
			if(tablero[K][L] == nada && nacer(K, L))
				tablero[K][L] = viva;
			else if(tablero[K][L] == viva && morir(K, L))
				tablero[K][L] = nada;
		}
	}
//	cout<<endl;
//	actualizar();
//	print();
//	cout<<endl;
}

int magia(){
	int tiempo;
	for(tiempo = 0; tablero != vacio; tiempo ++)
		simular();
	return tiempo;
}

int main(int argc, char *argv[]) {
	int casos, K=0;
	for(cin>>casos; K<casos; K++){
		tablero.clear();
		iniciar();
		lectura();
		cout<<"Case #"<<K+1<<": ";
		cout<<magia();
		cout<<endl;
	}
	return 0;

}

