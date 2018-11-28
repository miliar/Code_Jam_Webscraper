#include <iostream>

#include <vector>
#include <fstream>

typedef std::vector<std::string> COMBINATION_CONT;

typedef struct {
	char ele1;
	char ele2;
} OPPOSE;

typedef std::vector<OPPOSE> OPPOSITION_CONT;

COMBINATION_CONT combines;
OPPOSITION_CONT opposes;

using namespace std;
std::string sequence;

bool doReplace(char inChar, size_t pos) {
	bool replaced = false;
	for(size_t k=0; k<combines.size(); ++k) {
		int fpos = -1;
		if(combines[k][0] == inChar)
			fpos = 1;
		else if(combines[k][1] == inChar)
			fpos = 0;
		if(fpos != -1) {
			if(sequence[pos] == combines[k][fpos]) {
				sequence[pos] = combines[k][2];
				
				sequence.erase(pos+1, 2);
				doReplace(combines[k][2], pos-1);

				replaced = true;
			}
		}
	}
	return replaced;
}


void doDelete(char inChar) {
	for(size_t i=0; i<opposes.size(); ++i) {
		size_t start = string::npos;
		if(inChar == opposes[i].ele1)
			start = sequence.find(opposes[i].ele2);
		else if(inChar == opposes[i].ele2)
			start = sequence.find(opposes[i].ele1);
		if(start != string::npos) {
			sequence.clear();
		}
	}
}

ifstream input("B-large.in");
ofstream output("output.out");

int main (int argc, char * const argv[]) {
	int caseNum;
	input>>caseNum;
	for(int i=0; i<caseNum; ++i) {
		combines.clear();
		opposes.clear();
		sequence.clear();
		
		int tmpNum;
		input>>tmpNum;
		for(int j=0; j<tmpNum; ++j) {
			std::string tmp;
			input>>tmp;
			combines.push_back(tmp);
		}
		input>>tmpNum;
		for(int j=0; j<tmpNum; ++j) {
			OPPOSE tmp;
			input>>tmp.ele1;
			input>>tmp.ele2;
			opposes.push_back(tmp);
		}
		input>>tmpNum;
		for(int j=0; j<tmpNum; ++j) {
			char tmpChar;
			input>>tmpChar;
			
			if(sequence.size() == 0) {
				sequence += tmpChar;
				continue;
			}
			
			if(!doReplace(tmpChar, sequence.size()-1)) {
				sequence += tmpChar;
			}
			doDelete(sequence[sequence.size()-1]);
		}
		
		
		output<<"Case #"<<i+1<<": [";		
		for(size_t j=0; j<sequence.size(); ++j) {
			output<<sequence[j];
			if(j != sequence.size()-1)
				output<<", ";
		}

		output<<"]\n";
	}
	
    return 0;
}
