#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main () {
	ifstream myfile;
	myfile.open("B-small-practice.in");
	ofstream outfile;
	outfile.open("B-practice.out");
	string cases;
	getline(myfile,cases);
	int n = atoi(cases.c_str());
	
	
	string words[1000] = {""};
	string t;

	for(int j = 0; j < n; j++) {
		cout << "Case #" << j+1 << ":";
		outfile << "Case #" << j+1 << ":";
		getline(myfile,t);
		size_t found;
		found = t.find_first_of(" ");
		int i = 0;
		
		while(found != string::npos){
			words[i] = t.substr(0, found);
			t = t.substr(found+1);
			i++;
			found = t.find_first_of(" ");
		}
		words[i] = t;
		i++;
		cout << " ";
		outfile << " ";
		for(int k = i-1; k > 0; k--){
			cout << words[k] << " ";
			outfile << words[k] << " ";
		}
		cout << words[0] << endl;
		outfile << words[0] << "\n";
		/*string hold = "";
		for(int k = 0; k < i/2; k++)
		{
			hold = words[i-k-1];
			words[i-k-1] = words[k];
			words[k] = hold;
		}
		cout << " ";
		for(int p = 0; p < i; p++)
		{
			cout << " "
		*/
		//memset(words, 0x00, 1000);
	}
	myfile.close();
	outfile.close();
	return 0;
}
