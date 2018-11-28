/*
 * main.cpp
 *
 *  Created on: 14.4.2012.
 *      Author: Adnan
 */

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {
	string inLine,outLine;
	string example,exampleGoogle;
	string alphabet,alphaGoogle;
	int t;

	//Setup alphabet
	for (char i='a';i<='z';i++) {
		alphabet.push_back(i);
	}

	example = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq";
	exampleGoogle = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz";

	//Translate
	for (char i='a';i<='z';i++) {
		for (int j=0;j<example.size();j++) {
			if (example[j]==i) {
				alphaGoogle.push_back(exampleGoogle[j]);
				break;
			}
		}
	}

	cout << alphabet.size() << endl;
	cout << alphaGoogle.size() << endl;

	cout << alphabet << endl;
	cout << alphaGoogle << endl;

	ifstream in("input");
	ofstream out("output");

	if (!in){
		cout << "Cannot open input file.\n";
		return 1;
	}

	if (!out){
		cout << "Cannot open output file.\n";
		return 1;
	}

	in >> t;

	getline(in,inLine);

	for (int i=0;i<t;i++) {
		outLine.clear();
		inLine.clear();

		getline(in,inLine);

		cout << inLine.size() << endl;
		cout << inLine << endl;
		for (int j=0;j<inLine.size();j++) {
			//cout << inLine[j] << endl;
			cout << j << endl;
			if (inLine[j]==' ') {
				outLine.push_back(' ');
			} else {
				for (int k=0;k<alphaGoogle.size();k++) {
					if (alphaGoogle[k]==inLine[j]) {
						outLine.push_back(alphabet[k]);
						break;
					}
				}
			}
		}
		out << "Case #" << i+1 << ": " << outLine << endl;
	}

	in.close();
	out.close();

	return 0;
}
