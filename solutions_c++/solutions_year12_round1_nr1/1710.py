#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>

using namespace std;



int main() {

	ifstream fin;
	
	fin.open("input.txt");
	
	int numcases;
	fin >> dec >> numcases;
	fin >> ws;
	
	int readcases = numcases;
	while(readcases > 0) {
		int numtyped;
		int numcharstotal;
		vector< float > probarray;
		
		fin >> dec >> numtyped;
		fin >> dec >> numcharstotal;
		
		for(int i=0; i<numtyped; i++) {
			float tempProb;
			fin >> tempProb;
			probarray.push_back(tempProb);
		}
	
		//keep typing avg number of chars
		float cumprob = probarray[0];
		for (int i=1; i<numtyped; i++) {
			cumprob = cumprob * probarray[i];
		}
		float avgkeys1 = cumprob * (numcharstotal-numtyped+1) + (1-cumprob) * ((numcharstotal-numtyped)+1+(numcharstotal)+1);
		//Probability of only needing to type remaining characters + enter, + probability of needing to type remaining, enter, and then type it all again, and enter.
		
		
		//backspace avg number of chars
		float curleast = 999999999;
		for (int i=numtyped; i>0; i--) {
			
			float tempcumprob = probarray[0];
			for (int j=1; j<i; j++) {
				tempcumprob = tempcumprob * probarray[j];
			}
			float avgkeys2 = tempcumprob * ((numcharstotal-i)+(numtyped-i)+1) + (1-tempcumprob) * ((numcharstotal-i)+(numtyped-i)+1+(numcharstotal)+1);
			//Probability of only needing to type remaining characters+enter+number of backspaces, + probability of needing to  retype it all again after previous.
			
			if(avgkeys2 < curleast) { curleast = avgkeys2; }
		}
		
		
		//enter right away avg number of chars
		float avgkeys3 = 1  + (numcharstotal+1);
		
		float output = 0;
//		cout << "AK1: " << avgkeys1 << " CURLEAST: " << curleast << " AK3: " << avgkeys3 << endl;
		if ((avgkeys3 < curleast) && (avgkeys3 < avgkeys1)) {
			output = avgkeys3;
		} else if ((curleast < avgkeys3) && (curleast < avgkeys1)) {
			output = curleast;
		} else if ((avgkeys1 < avgkeys3) && (avgkeys1 < curleast)) {
			output = avgkeys1;
		}
		
		if((output == 0) && (avgkeys1 == curleast)) {
			output = avgkeys1;
		}
		
		cout << "Case #" << setiosflags(ios::fixed) << setprecision(6) << numcases - readcases + 1 << ": ";
		cout << output;
		
		cout << endl;
		readcases--;
		
	}
	
	return 0;
}
