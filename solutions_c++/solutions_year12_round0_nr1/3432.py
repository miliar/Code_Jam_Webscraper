#include <iostream>
#include <sstream>

using namespace std;

string map = "yhesocvxduiglbkrztnwjpfmaq";

int main(void){
	int T;
	cin >> T;

	string line;
	getline(cin, line);

	for(int t=1; t<=T; t++){
		getline(cin, line);
		
		for(int i=0; i<line.length(); i++)
			if(line[i] != ' ')
				line[i] = map[line[i]-'a'];
		
		cout << "Case #" << t << ": " << line << endl;
	}

	return 0;
}
