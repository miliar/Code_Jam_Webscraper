#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <limits.h>
#include <deque>
#include <math.h>

using namespace std;

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[1] << " could not be opened" << endl;
		exit(-1);
	}
	long T;
	file >> T;
	for (long i = 0; i < T; i++){
		int R;
		file >> R;
		set < pair <int, int> > *oneElements = new set< pair <int, int > >();
		set <pair <int, int > > *newOneElements = new set < pair <int, int > >();
		for (long j = 0; j < R; j++){
			long X1, Y1, X2, Y2;
			file >> X1 >> Y1 >> X2 >> Y2;
			for (long k = X1; k <= X2; k++){
				for (long l = Y1; l <= Y2; l++){
					oneElements->insert(pair<int, int>(k, l));
				}
			}
		}


		//Simulamos
		//Pasamos los que mantienen vida
		int steps = 0;
		while(oneElements->size() != 0){
			newOneElements->clear();
			for (set< pair <int, int > >::iterator j = oneElements->begin(); j != oneElements->end(); j++){
				if (oneElements->count(pair<int, int>(j->first-1, j->second)) || oneElements->count(pair<int, int>(j->first, j->second - 1))){
					newOneElements->insert(*j);
				}
			}
			//Nuevos elementos vivos
			for (set< pair <int, int > >::iterator j = oneElements->begin(); j != oneElements->end(); j++){
				if (oneElements->count(pair<int, int> (j->first - 1, j->second + 1))){
					newOneElements->insert(pair<int, int>(j->first, j->second + 1));
				}
			}
			set < pair <int, int> > *tmp = oneElements;
			oneElements = newOneElements;
			newOneElements = tmp;
			steps++;
		}
		cout << "Case #" << (i+1) << ": " << steps << endl;

	}
	file.close();
}
