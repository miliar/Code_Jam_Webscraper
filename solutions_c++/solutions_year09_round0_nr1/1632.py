#include <iostream>
#include <fstream>

#define MAX_CHAR 256

int main (int argc, char * const argv[]) {
//	std::ifstream ifile("input");
//	std::ifstream ifile("A-small-attempt0.in");
	std::ifstream ifile("A-large.in");
	std::ofstream ofile("output2");
	int wLen, wCount, patternCount;
	ifile>> wLen >>wCount >>patternCount;
	ifile.get();

	wLen++;
	char *words = (char*)malloc(sizeof(char)*wCount*wLen);
	int p[wLen*MAX_CHAR];
	
	
	for(int i=0;i< wCount;i++){
		ifile.getline(&words[i*wLen], wLen);
	}
	for(int i=0;i< wCount;i++){
//		std::cout<< &words[i*wLen]<< std::endl;
	}
	std::string pattern;
	bool in;
	int pos;

	char *word;
	bool match;
	int matchCount;
	for(int i=1;i<= patternCount;i++){
		memset(p, 0, sizeof(int)*wLen*MAX_CHAR);
		in = false;
		pos = 0;
		// set pattern
		ifile >> pattern;
//		std::cout<< pattern<< std::endl;
		for(int j=0;j< pattern.length();j++){
			if(pattern[j] == '('){
				in = true;
			}else if(pattern[j] == ')'){
				in = false;
				pos++;
			}else{
				p[(pos*MAX_CHAR)+pattern[j]]++;
				if(!in){
					pos++;
				}
			}
		}

		matchCount = 0;
		for(int k=0;k< wCount;k++){
			word = &words[k*wLen];
//			std::cout<< word<< std::endl;
			match = false;
			for(int j=0;j< 16;j++){
//				std::cout<< word[j]<< std::endl;
				if(word[j] == '\0'){
					match = true;
					break;
				}
				if(p[(j*MAX_CHAR)+word[j]] == '\0'){
					// not match
					break;
				}
			}
			if(match){
				matchCount++;
			}
		}
		std::cout<< "Case #"<< i<< ": "<< matchCount<< std::endl;
		ofile<< "Case #"<< i<< ": "<< matchCount<< std::endl;
	}

	ifile.close();
	ofile.close();
    return 0;
}
