// C++ Code
// Cuneyt Mertayak
#include <iostream>
#include <fstream>
#include <string.h>
#include <string>

#define LINE_SIZE 501

using namespace std;

int calc_num(char *str){
	char pattern[] = "welcome to code jam";
	int **dp_table;

	int str_len = strlen(str);

	dp_table = new int *[str_len];
	for(int i=0; i<str_len; i++){
		dp_table[i] = new int[19];
	}

	dp_table[0][0] = 0;
	if(str[0]==pattern[0]){
		dp_table[0][0] = 1;
	}

	for(int i=1; i<str_len; i++){
		dp_table[i][0] = dp_table[i-1][0];
		if(str[i]==pattern[0]){
			dp_table[i][0] += 1;
		}
	}

	for(int i=0; i<str_len; i++){
		for(int j=1; j<19; j++){
			if(i<j){
				dp_table[i][j] = 0;
				continue;
			}
			if(str[i]==pattern[j]){
				dp_table[i][j] = (dp_table[i-1][j] + dp_table[i][j-1]) % 10000;
			}
			else{
				//dp_table[i][j] = (dp_table[i-1][j]<dp_table[i][j-1]) ? dp_table[i-1][j] : dp_table[i][j-1];
				dp_table[i][j] = dp_table[i-1][j]; //<dp_table[i][j-1]) ? dp_table[i-1][j] : dp_table[i][j-1];
			}
		}
	}

	return dp_table[str_len-1][18];
}


void clear_line(char *line){
	for(int i=0; i<LINE_SIZE; i++){
		line[i] = '\0';
	}
}

int main(){
	fstream fin, fout;
	int case_n;
	char line[LINE_SIZE];

	fin.open("./3.in", fstream::in);
	fout.open("./3.out", fstream::out);

	fin >> case_n;

	for(int i=0; i<case_n; i++){
		clear_line(line);

		// burada line OKU!
		string sline;

		do{
			getline(fin, sline);
		}while(sline.length() == 0);

		strcpy(line, sline.c_str());

		fout << "Case #" << i+1 << ": ";
		int result = calc_num(line);
		if(result < 10){
			fout << "000" << result << endl;
		}else if(result < 100){
			fout << "00" << result << endl;
		}else if(result < 1000){
			fout << "0" << result << endl;
		}else{
			fout << result << endl;
		}
	}

	fin.close();
	fout.close();
	
	return 0;
}

