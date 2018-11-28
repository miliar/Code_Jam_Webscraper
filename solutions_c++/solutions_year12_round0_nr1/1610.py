//============================================================================
// Name        : fff.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <map>
using namespace std;

// y-->a
// e-->o
// q-->z
// 97 --- 122
int incode[26];
int outcode[26]={

};


map<int, int> charMap;

int main() {


	ifstream in;
	ofstream out;
	in.open("input");

	ifstream in2;
	in2.open("input2");

	out.open("output");
	int casecount;
	in >> casecount;
	in2 >> casecount;
//	char charactor = 'a';
//	for (int i=0; i<26; ++i){
//		incode[i]= charactor;
//		charactor++;
//	}

	//casecount++;
	for(int i=0; i<casecount;++i){


		for (int j = 0; j <100; j++){
			char c = 0;
			char c2 = 0;
			in>>c;
			in2>>c2;
			if(c>=97 && c<=122){
				charMap[c] = c2;
				//cout << int(c2) <<endl;
			}

		}
//		while(c!='\n'){
//			cout << c2;
//			charMap[c] = c2;
//		}



	}

	charMap['y'] = 'a';
	charMap['e'] = 'o';
	charMap['q'] = 'z';
	charMap['s'] = 'n';
	charMap['z'] = 'q';

	map<int, int>::iterator cS = charMap.begin(),
			cE = charMap.end();
	for(;cS!= cE;++cS){
		cout << char(cS->first) << "--->" << char (cS->second)<<endl;
	}

	ifstream inputdata;
	inputdata.open("input3");
	out;

	inputdata >> casecount;
	casecount++;
	for(int i=0; i < casecount; ++i){
		string cc;
		getline(inputdata, cc);
		cout <<cc<<endl;
		const char* c = cc.c_str();

		out << "Case #"<<i<<": ";
		for (int j = 0; j <cc.length(); j++){


			if(c[j]>=97 && c[j]<=122){
				out << char(charMap[c[j]]);

			}else{
				out<<c[j];
			}

		}
		out << '\n';

	}



	cout << "!!!Hello World!!!" << casecount << endl; // prints !!!Hello World!!!
	return 0;
}
