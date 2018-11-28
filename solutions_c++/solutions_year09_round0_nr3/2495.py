#include <string>
#include <vector>
#include <fstream>
#include <iostream>
#include <stdio.h>

using namespace std;

void help(char *program) {
  std::cout << program; 
  std::cout << ": Need a filename for a parameter.\n";
}



int main(int argc, char* argv[]) {
	string line;
	int caseno=0,i,N;
	char tc;
	unsigned int c[20] = {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
	if (argc < 2) { help(argv[0]); return 1; }
	ifstream infile (argv[1], ios_base::in);
	infile >> N;
	getline(infile, line);
	for (caseno=0;caseno<N;caseno++) {
		getline(infile, line);
		//transform(line.begin(), line.end(), line.begin(), toupper);
		for (i=0;i<20;i++) c[i]=0;
		c[0]=1;
		for (i=0;i<line.length();i++) {
			tc = toupper(line[i]);
			switch ( tc ) {
				case 'W' : {c[1]=(c[0]+c[1]) % 10000;
					   break;}
				case 'E' : {c[2]=(c[1]+c[2]) % 1000;
					    c[7]=(c[6]+c[7]) % 10000;
					    c[15]=(c[14]+c[15]) % 10000; break;}
				case 'L' : {c[3]=(c[2]+c[3]) % 10000; break;}
				case 'C' : {c[4]=(c[3]+c[4]) % 10000;
					    c[12]=(c[11]+c[12]) % 10000;break;}
				case 'O' : {c[5]=(c[4]+c[5]) % 10000;
					    c[10]=(c[9]+c[10]) % 10000;
					    c[13]=(c[12]+c[13]) % 10000;break;}
				case 'M' : {c[6]=(c[5]+c[6]) % 10000;
					    c[19]=(c[18]+c[19]) % 10000;break;}
				case 'T' : {c[9]=(c[8]+c[9]) % 10000;}
				case 'D' : {c[14]=(c[14]+c[13]) % 10000;break;}
				case 'J' : {c[17]=(c[16]+c[17]) % 10000;break;}
				case 'A' : {c[18]=(c[17]+c[18]) % 10000;break;}
				case ' ' : {c[8]=(c[7]+c[8]) % 10000;
					    c[11]=(c[10]+c[11]) % 10000;
					    c[16]=(c[15]+c[16]) % 10000;break;}
			}
		}
		printf("Case #%u: %4.4u\n",caseno+1,c[19]);
		//cout << "Case #"<<caseno+1<<": "<<c[19]<<endl;
	}	
}

