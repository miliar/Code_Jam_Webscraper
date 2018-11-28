#include <iostream>
#include <fstream>
#include <list>
#include <string>

using namespace std;
long T,N,k,R; //k -> capacidad; R-> corridas; N->can grupos

list <long> grupos; //cada elemento tiene la capacidad de los grupos
list <long> rc;

int main (int argc, char** argv) {
	ifstream input(argv[1]);
	input >> T;
	long i=0;
	long g=0;
	long util=0;
	long recaud=0;
	while (i<T){
		input >> R;
		input >> k;
		input >> N;
		for (long n=0; n<N; n++){  //cargo los grupos
			input >> g;
			grupos.push_back(g);
		}
		recaud=0;
		for (long a=0; a<R; a++){ //para cada corrida
			util=0;
			while (util<=k) { //suben
				if (grupos.front()+util>k) break;
				util+=grupos.front();
				rc.push_back(grupos.front());
				grupos.pop_front();
			}
			recaud+=util;
			while (!rc.empty()){
				grupos.push_back(rc.front());
				rc.pop_front();
			}
			rc.clear();
		}
		cout << "Case #"<< i+1 << ": " << recaud << endl;
		grupos.clear();
		i++;
	}


	return 0;
}
