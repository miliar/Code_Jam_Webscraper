#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
using namespace std;

string to_str(int i){
	stringstream ss;
	ss.str("");
	ss.clear();
	ss << i;
	string str1 = ss.str();
	return str1;
}

int sol3(int a, int b) {
	int ret = 0;

	string str1,str2;
	bool flag;
	
	int n1,n2;

	int i,j,ii;
	
	string temp[8];

	for (i=a;i<b;i++){
		n1 = i;
		str1 = to_str(i);
		
		for (ii=0; ii<8;ii++){
			temp[ii] = "";
		}

		for (j=0; j<str1.length();j++){
			str2 = str1.substr(j) + str1.substr(0,j);
			flag = true;

			for (ii=0; ii<8;ii++){
				if (temp[ii] == str2){
					flag = false;
					continue;
				}
			}
			
			if (flag == false){
				continue;
			}

			temp[j] = str2;
	
			n2 = atoi(str2.c_str());
			if (n1 < n2 && n2 <= b){
				ret += 1;
			}
		}
	}
	return ret;
}



int main(){

	char buf[256];
	char num_[256];
	
	static const char filename[] = "C-large.in";
	FILE * fp = fopen(filename,"r");

	ofstream retfile;
	retfile.open("output.txt");


	string AB;
	string A,B;
	size_t pos1,pos2;

	int a,b;
	if (fp != NULL){
		fgets(num_, sizeof(buf), fp);		
		int num = atoi(num_);

		int i=0;
		for (i=0;i<num;i++){
			fgets(buf, sizeof(buf), fp);
			AB = buf;
			pos1 = AB.find(" ");
			pos2 = AB.find("\n");
			A = AB.substr(0,pos1);
			B = AB.substr(pos1+1,pos2);
			a = atoi(A.c_str());
			b = atoi(B.c_str());
 			retfile <<"Case #" << i+1 << ": "<< sol3(a,b) <<"\n";	
		}
	}
	fclose(fp);
	retfile.close();

 	return 0;
}
