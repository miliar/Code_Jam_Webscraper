#include <iostream>
#include <map>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	map<char, char> remplazos;
	unsigned int casos;
	string entrada, salida;
	
	remplazos['y'] = 'a';
	remplazos['n'] = 'b';
	remplazos['f'] = 'c';
	remplazos['i'] = 'd';
	remplazos['c'] = 'e';
	remplazos['w'] = 'f';
	remplazos['l'] = 'g';
	remplazos['b'] = 'h';
	remplazos['k'] = 'i';
	remplazos['u'] = 'j';
	remplazos['o'] = 'k';
	remplazos['m'] = 'l';
	remplazos['x'] = 'm';
	remplazos['s'] = 'n';
	remplazos['e'] = 'o';
	remplazos['v'] = 'p';
	remplazos['z'] = 'q';
	remplazos['p'] = 'r';
	remplazos['d'] = 's';
	remplazos['r'] = 't';
	remplazos['j'] = 'u';
	remplazos['g'] = 'v';
	remplazos['t'] = 'w';
	remplazos['h'] = 'x';
	remplazos['a'] = 'y';
	remplazos['q'] = 'z';
	
	
	
	//freopen("SpeakinginTongues.txt", "rb", stdin);
	cin >> casos;
	cin.ignore();
	for(unsigned int i=0; i<casos;){
		getline(cin, entrada);
		
		if(!entrada.empty() && entrada[0] != '\r'){
			for(unsigned int j=0; j<entrada.size();j++){
				if(isalpha(entrada[j]))
					salida.push_back(remplazos[entrada[j]]);
				else
					salida.push_back(' ');
			}
			cout << "Case #" << i+1 << ": ";
			cout << salida << endl;
			i++;
		}
		salida.clear();
	}
	
	return 0;
}

