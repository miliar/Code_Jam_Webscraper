#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef vector<string> VS;

VS words;

int Solve(string pattern, int numtokens, int numwords){
	int count = numwords;

	VS mpattern;

	while (pattern != ""){
		if (pattern[0] == '('){
           mpattern.push_back(pattern.substr(1, pattern.find(')') - 1));
		   pattern = pattern.substr(pattern.find(')') + 1);
		} else {
           mpattern.push_back(pattern.substr(0,1));
		   pattern = pattern.substr(1);
		}    
		//cout << mpattern[mpattern.size()-1] << " ";
	}
    cout << "\n";
	VS::iterator it;
	for (it = words.begin(); it < words.end(); it++){
		string oneword = *it;
		for (int pos = 0; pos < numtokens; pos++){
			if (mpattern[pos].find(oneword[pos]) == -1){
                count--; 
                break;
			}
		}
	}

	return count;

}

int main(){

	int L, D, N;
	
	ifstream file;
	ofstream outfile;
	outfile.open("A-large-1.out");
	file.open("../A-large.in");

	file >> L;
	file >> D;
	file >> N;

	if (N == 0) return 0;
	
	words.resize(D);
	
	for (int j = 0; j < D; j++){
		file >> words[j];
	}

	int m = 1;
	while (m <= N){
		string pattern;
		file >> pattern;
        //cout << pattern << "\n";
		outfile << "Case #" << m << ": " << Solve(pattern, L, D) << endl;
		m++;
	}

	file.close();
	outfile.close();

	return 0;
}