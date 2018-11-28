#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <utility>
#include<map>
#include<cmath>
#include<string.h>

using namespace std;

int rep(int j, int rept){
	stringstream st;
	string stt;
	st<<j;
	stt=st.str();
	string num="";

	for(int i=0; i<rept; i++){
		num+=stt[stt.length()-rept+i];
	}
	for(int i=0; i<stt.length()-rept; i++){
		num+=stt[i];
	}

	return atoi(num.c_str());
}

int main(int argc, char **argv) {
	ifstream input(argv[argc-1]);
	string tmp;
	int result;
	int input_size;

	if(argc!=2){
		cout << "There is no input file!" << endl;
		return -1;
	}

	input>>tmp;
	input_size=atoi(tmp.c_str());

	for(int i=1; i<=input_size; i++){
		input>>tmp;
		int min=atoi(tmp.c_str());
		input>>tmp;
		int max=atoi(tmp.c_str());

		result=0;

		// cout << rep(12345, 1) << endl;
		// cout << rep(12345, 2) << endl;
		// cout << rep(12345, 3) << endl;
		vector<int> a;

		for(int j=min; j<=max; j++){
			for(int r=1; r<log10(j); r++){
				int tmp=rep(j,r);
				if(j<tmp && tmp<=max && find(a.begin(), a.end(),tmp)==a.end()){
					result++;
					//cout << j<< ", "<<tmp<<endl;
				}
				a.push_back(tmp);
			}
			a.clear();
		}


		cout << "Case #" << i << ": " << result << endl;

	}

	return 0;
}