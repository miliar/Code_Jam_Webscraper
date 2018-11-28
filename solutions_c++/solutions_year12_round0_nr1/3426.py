#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream ifs(argv[1]);
	ofstream ofs("output");

	int T;
	ifs >> T;
	ifs.clear();
	ifs.ignore(std::numeric_limits<streamsize>::max(),'\n');

	if ( T < 1 || T > 30) return 1;

	string G, S;
	char *al = "yhesocvxduiglbkrztnwjpfmaq";
	
	for (int i = 1; i <= T; ++i) {
		int j = 0;
		S.erase();

		getline(ifs, G);
		 
		while (G[j]) 
			if (G[j] !=' ')	S.push_back(al[G[j++]-'a']);
			else { S.push_back(' '); j++; }
            
		ofs << "Case #" << i << ": " << S << endl;
		}
	ifs.close();
	ofs.close();
	return 0;
}
