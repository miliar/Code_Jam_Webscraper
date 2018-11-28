/*
 * themepark.cpp
 *
 *  Created on: 08/05/2010
 *      Author: eduardoespinoza
 */

#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int main(int argc, char **argv) {

	int nrocasos;
	int r,k,n;
	cin>>nrocasos;
	for (int i = 0; i < nrocasos; ++i) {
		cin>>r>>k>>n;
		queue<int> cola;
		queue<int> tren;int pasajerostren=0;
		int totaldinero=0;
		int nro;
		for (int j = 0; j < n; ++j) {
			cin>>nro;
			cola.push(nro);
		}
		int nropaseos=0;
		while(nropaseos<r){
			while(!cola.empty()&&pasajerostren+cola.front()<=k)//comprueba capacidad
			{
//				cout<<"anadiendo "<<cola.front()<<endl;
				pasajerostren+=cola.front();
				tren.push(cola.front());
				cola.pop();

			}
//			cout<<"_______\n";
//			sleep(1);
			totaldinero+=pasajerostren;
			pasajerostren=0;
			nropaseos++;
			while(!tren.empty())
			{
				cola.push(tren.front());
				tren.pop();
			}
		}
		printf("Case #%d: %d\n",i+1,totaldinero);


	}

	return 0;
}
