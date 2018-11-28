#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdio.h>
using namespace std;


void main(){


    ifstream fin("input.txt");
    ofstream fout("output.txt");
	
	string a = "abcdefghijklmnopqrstuvwxyz";
	string b = "ynficwlbkuomxsevzpdrjgthaq";
	
	
	int n;
	fin >> n;

	char st[500];
	fin.getline(st, 5000);

	for(int i = 1; i<=n; i++){
		string instr = "";
		

		
		fin.getline(st, 5000);


		



 
		instr = st;

		string res = "";
		for(int k = 0; k<instr.length(); k++){
			int t = 0;
			
			if(instr[k] == ' ') res += ' ';
			else{
				while(b[t] != instr[k]) t++;
				res += a[t];
			}

			
			
		}



		fout << "Case #" << i << ": " << res << endl;
	
	}
    
}