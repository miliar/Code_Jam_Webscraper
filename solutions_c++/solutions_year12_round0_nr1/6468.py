#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
	string alph = "yhesocvxduiglbkrztnwjpfmaq";
	int T;
	vector<string> trans;
	string G;

	ifstream input("input.txt");
	ofstream output;
	output.open("output.txt");

	if(! input ){
		cout << "Unable to open file: input.txt"<< endl;
		return EXIT_FAILURE;
	}else{
		input>>T;
		getline(input,G);
		for(int i=0; i < T; i++){
			getline(input,G);
			output << "Case #"<< i+1 <<": ";
			for(int j=0; j< G.size() && G.size()<101 ;j++){
				if(G[j] >= 'a' && G[j] <= 'z')
					output << alph[G[j] - 97];
				else output << G[j];
			}
			output<<"\n";
		}	
	}
	output.close();
}