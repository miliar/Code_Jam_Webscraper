#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main(){

	int			T;
	string		G;

	ifstream	ifs("A-small-attempt0.in");
	ofstream	ofs("A.out");

	ifs >> T;
	getline(ifs, G);

	for(int i = 0; i < T; i++){
		getline(ifs, G);

		//abcdefghijklmnopqrstuvwxyz
		//yhesocvxduiglbkrztnwjpfmaq
		for(int j = 0; j < (int)G.size(); j++){
			if(G[j] == 'a'){
				G[j] = 'y';
			}
			else if(G[j] == 'b'){
				G[j] = 'h';
			}
			else if(G[j] == 'c'){
				G[j] = 'e';
			}
			else if(G[j] == 'd'){
				G[j] = 's';
			}
			else if(G[j] == 'e'){
				G[j] = 'o';
			}
			else if(G[j] == 'f'){
				G[j] = 'c';
			}
			else if(G[j] == 'g'){
				G[j] = 'v';
			}
			else if(G[j] == 'h'){
				G[j] = 'x';
			}
			else if(G[j] == 'i'){
				G[j] = 'd';
			}
			else if(G[j] == 'j'){
				G[j] = 'u';
			}
			else if(G[j] == 'k'){
				G[j] = 'i';
			}
			else if(G[j] == 'l'){
				G[j] = 'g';
			}
			else if(G[j] == 'm'){
				G[j] = 'l';
			}
			else if(G[j] == 'n'){
				G[j] = 'b';
			}
			else if(G[j] == 'o'){
				G[j] = 'k';
			}
			else if(G[j] == 'p'){
				G[j] = 'r';
			}
			else if(G[j] == 'q'){
				G[j] = 'z';
			}
			else if(G[j] == 'r'){
				G[j] = 't';
			}
			else if(G[j] == 's'){
				G[j] = 'n';
			}
			else if(G[j] == 't'){
				G[j] = 'w';
			}
			else if(G[j] == 'u'){
				G[j] = 'j';
			}
			else if(G[j] == 'v'){
				G[j] = 'p';
			}
			else if(G[j] == 'w'){
				G[j] = 'f';
			}
			else if(G[j] == 'x'){
				G[j] = 'm';
			}
			else if(G[j] == 'y'){
				G[j] = 'a';
			}
			else if(G[j] == 'z'){
				G[j] = 'q';
			}
		}

		ofs << "Case #" << i + 1 << ": " + G << endl;
	}
}