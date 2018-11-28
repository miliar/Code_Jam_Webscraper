#include <iostream>
#include <vector>
using namespace std;

typedef unsigned long long int ulli;

class viaje{
public:
	ulli tamanio, costo, siguiente, cantciclo, costociclo;//considerandome cabeza de serie, que resultados obtengo
	//cantciclo de viajes y su costociclo antes de hacer ciclo conmigo
	bool visto;
	viaje(): costo(0), siguiente(0), cantciclo(0), costociclo(0), visto(false){}
};

void actualizar(vector<viaje> &coaster, ulli capacidad){//calcula los otros campos de los objetos
	ulli K, tam, L, size;
	size = coaster.size();
	for(K=0; K<size; K++){
		for(L=K, tam=0; L < size+K; L++){
			tam += coaster[L%size].tamanio;
			if(tam > capacidad){
				tam -= coaster[L%size].tamanio;
				break;
			}
		}
		coaster[K].costo = tam;
		coaster[K].siguiente = (L+size)%size;
	}
}

void findciclo(vector<viaje> &coaster, ulli &inicio, ulli &costociclo, ulli &longciclo, ulli &costoant, ulli &longant){
	ulli K, cant, costo;
	for(K=0, cant = 0, costo = 0; !coaster[K].visto; K = coaster[K].siguiente, cant++){
		coaster[K].visto = true;
		coaster[K].cantciclo = cant;
		coaster[K].costociclo = costo;
		costo += coaster[K].costo;
	}
	
	inicio = K;
	costociclo = costo - coaster[K].costociclo;
	longciclo = cant - coaster[K].cantciclo;
	costoant = coaster[K].costociclo;
	longant = coaster[K].cantciclo;
}

ulli simular(vector<viaje> &coaster, ulli recorrido, ulli inicio){
	ulli K, total;
	for(K=inicio, total=0; recorrido>0; recorrido--, K=coaster[K].siguiente)
		total += coaster[K].costo;
	return total;
}

ulli magia(vector<viaje> &coaster, ulli recorrido){
	ulli total = 0, cantidad;
	ulli inicio, longciclo, costociclo, costoant, longant;
	inicio = longciclo = costociclo = costoant = longant = 0;
	findciclo(coaster, inicio, costociclo, longciclo, costoant, longant);
	
//	cout<<"inicio, costociclo, longciclo, costoant, longant"<<endl;
//	cout<<inicio<<' '<<costociclo<<' '<<longciclo<<' '<<costoant<<' '<<longant<<endl;
	
	//repeticion de la secuencia
	if(recorrido >= longciclo + longant){
		recorrido -= longant;
		cantidad = recorrido/longciclo;
		recorrido %= longciclo;
		total = costoant + costociclo * cantidad;
	}
	else
		inicio = 0;//solo habia que simular
	//simulacion del resto
	total += simular(coaster, recorrido, inicio);
	return total;
}

void print(vector<viaje> &coaster){
	cout<<"Tamanio costo siguiente"<<endl;
	for(int K=0; K<coaster.size(); K++){
		cout<<coaster[K].tamanio<<' '<<coaster[K].costo<<' '<<coaster[K].siguiente<<endl;
	}
}

int main(int argc, char *argv[]) {
	ulli recorrido, capacidad, K, casos, total, tam;
	vector<viaje> coaster;
	for(K=1, cin>>casos; K<=casos; K++){
		cin>>recorrido>>capacidad;
		cin>>tam;

		coaster.clear(); coaster.resize(tam);
		for(ulli L=0; L<tam; L++)
			cin>>coaster[L].tamanio;
		
		actualizar(coaster, capacidad);
//		print(coaster);
		total = magia(coaster, recorrido);
		
		cout<<"Case #"<<K<<": "<<total<<endl;
	}
	return 0;
}

