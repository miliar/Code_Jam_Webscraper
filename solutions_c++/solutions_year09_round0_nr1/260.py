#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ofstream fout ("googleqr1.out");
	ifstream fin ("googleqr1.in");
	int numLetters, numWords, numCases;
	char words[5000][16];
	fin>>numLetters>>numWords>>numCases;
	fin.get();
	for(int n=0; n<numWords; n++)
		fin.getline(words[n], 16);
	for(int j=0; j<numCases; j++){
		char input[1000];
		fin.getline(input, 1000);
		int numMatches=0;
		for(int word=0; word<numWords; word++){
			bool works=true;
			int i=0;
			for(int n=0; n<numLetters; n++){
				if(input[i]=='('){
					bool match=false;
					while(input[i]!=')'){
						if(input[i]==words[word][n])
							match=true;
						i++;
					}
					if(!match){
						works=false;
						break;
					}
					i++;
				}
				else if(input[i]==words[word][n])
					i++;
				else{
					works=false;
					break;
				}
			}
			if(input[i])
				works=false;
			if(works)
				numMatches++;
		}
		fout<<"Case #"<<j+1<<": "<<numMatches<<endl;
	}
	return 0;
}
