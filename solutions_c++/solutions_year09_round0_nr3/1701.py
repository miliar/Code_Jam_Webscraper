#include <iostream>
#include <fstream>
#include <vector>
#include <map>

#define WLENGTH 19
#define MAX_LENGTH 500

char *welcome;
int wlen;

char buffer[1024];
int ilen;

unsigned int count = 0;

int f[19][500];

int get(char *wel, char *input)
{
	wel++;
//	std::cout<< "wel: "<< *wel<< ','<< wel-welcome<< std::endl;
	if(*wel == '\0'){
//		std::cout<< "count++"<< std::endl;
//		count++;
		return 1;
	}

	int sum = 0;
	input++;
	while(*input != '\0'){
		if(*input == *wel){
			// find next
			if(f[wel-welcome][input-buffer] == -1){
				f[wel-welcome][input-buffer] = get(wel, input);
			}
//			std::cout<< f[wel-welcome][input-buffer]<< std::endl;
			sum += f[wel-welcome][input-buffer];
		}
		input++;
	}
	return sum;
}

int main (int argc, char * const argv[]) {
//	std::ifstream ifile("input");
	std::ifstream ifile("C-small-attempt0(2).in");
	std::ofstream ofile("output");

	welcome = "welcome to code jam";
	wlen = strlen(welcome);
	char *w;

//	std::cout<< wlen<< std::endl;

	int caseCount;
	ifile >>caseCount;
	ifile.get();

	std::string input;
	for(int i=1;i<= caseCount;i++){
		ifile.getline(buffer, 1024);
//		std::cout<< buffer<< std::endl;

		for(int j=0;j< 19;j++){
			for(int k=0;k< 500;k++){
				f[j][k] = -1;
			}
		}
		
		w = welcome;
		count = 0;
		ilen = strlen(buffer);
		for(int j=0;j< ilen;j++){
//			std::cout<< *w<< ','<< buffer[j]<< std::endl;
			if(*w == buffer[j]){
				count += get(w, &buffer[j]);
			}
		}

		count %= 10000;
//		std::cout<< "Case #"<< i<< ": ";
//		if(count < 1000)
//			std::cout<< '0';
//		if(count < 100)
//			std::cout<< '0';
//		if(count < 10)
//			std::cout<< '0';
//		std::cout<< count<< std::endl;
		ofile<< "Case #"<< i<< ": ";
		if(count < 1000)
			ofile<< '0';
		if(count < 100)
			ofile<< '0';
		if(count < 10)
			ofile<< '0';
		ofile<< count<< std::endl;
	}

	ifile.close();
	ofile.close();
    return 0;
}
