#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv){
	ifstream input(argv[1]);
	string line;
	int T,N,P;
	char R;
	vector<int> blue;
	vector<int> orange;
	vector<char> comb;
	input >> line;
	T = atoi(line.c_str());
	int posO,posB,nextO,nextB,nextComb;
	for (int i=0;i<T;i++){//cases
		posO = posB = 1;
		nextO=nextB =nextComb = 0;		
		input >> line;
		blue.clear();
		orange.clear();
		comb.clear();
		N=atoi(line.c_str());
		for (int j=0; j<N; j++)  //PARSE CASE
		{
			input >> line;
			R = line.c_str()[0];
			comb.push_back(R);
			input >> line;
			P = atoi(line.c_str());
			switch (R) {
				case 'O':
					orange.push_back(P);
					break;
				case 'B':
					blue.push_back(P);
					break;
			}
		} 
		bool done=false;
		int secs=0;
		while (!done){
		bool sigComb=false;
		secs++;
		//movimientos robot
		//AZUL
			if (nextB<blue.size()){	
				if (posB<blue.at(nextB))
					posB++;
				else if (posB>blue.at(nextB))
					posB--;
				else //IGUAL
					if (comb.at(nextComb)=='B')
						{sigComb=true;nextB++;}
				}
			//NARANJA
			if (nextO<orange.size()){
				if (posO<orange.at(nextO))
					posO++;
				else if (posO>orange.at(nextO))
					posO--;
				else //IGUAL
					if (comb.at(nextComb)=='O')
						{sigComb=true;nextO++;}

			}
			if (sigComb) nextComb++;
			if (nextComb>=comb.size()) done=true;
		}
		cout<< "Case #" << (i+1)<<": "<< secs << endl;
	}
}

