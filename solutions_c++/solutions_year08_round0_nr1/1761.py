#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(){
	int casos;
	cin >> casos;
	for (int caso=0 ; caso<casos ;caso++){
		int buscadores;
		cin >> buscadores;
		map <string , long> mapa;
		int id=0;
		long todos[buscadores];
		memset(todos, 0 , sizeof(todos));
		
		string temp;
		getline(cin,temp);
		for (int i=0 ; i<buscadores ; i++){
			getline(cin,temp);
		//	cout << temp << " " << id << endl;
			mapa[temp]=id;
			id++;
		}
		int consultas;
		cin >> consultas;
		getline(cin,temp);
		
		int maximo=1<<buscadores;
		--maximo;
		//cout << consultas << "consultas " << maximo<< endl;
		int imp=0;
		int respuesta=0;
		for (int con=0 ; con<consultas ; con++){
			getline(cin,temp);
			//cout << "Temp " << temp << endl;
			if (mapa.count(temp)>0){
				int ide=mapa[temp];
				imp=imp|1<<ide;
				//cout << imp << " Imp " << maximo << endl;
				if (imp==maximo){
					++respuesta;
					imp=0;
					imp=1<<ide;
				}
				//todos[ide]++;
				/*for (int i=0 ; i<buscadores ; i++)
					cout << todos[i] << " ";
				cout << endl;*/
			}
						
		}/*
		int menor=9999999;
		for (int i=0 ; i<buscadores ; i++)
			if (todos[i]<menor)
				menor=todos[i];*/
		cout << "Case #" << (caso+1) << ": " << respuesta << endl;
	}
	return 0;
}
