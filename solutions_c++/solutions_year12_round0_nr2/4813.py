#include <iostream>
#include <string>
#include <fstream>
#include <map>
using namespace std;


int main() {
	
	ifstream fin;
	
	fin.open("input.txt");
	
	int numcases;
	fin >> dec >> numcases;
	fin >> ws;
//	fscanf(&fin,"%d\n", &numcases);
	
//	cout << numcases << endl;
	
	int readcases = numcases;
	while(readcases > 0) {
		int numpeople;
		int numsurprise;
		int bestresult;
		int countabove = 0;
//		vector<int, vector<int>, int> totalArray;
		fin >> dec >> numpeople;
		fin >> dec >> numsurprise;
		fin >> dec >> bestresult;
		
		int whocansurprise = 0;
		for(int i=0; i < numpeople; i++) {
			int temp;
			int tempsurprise;
			int countsurprise = numsurprise;
			int countpass = 0;
			int nosurprise = 0;
			int cansurprise = 0;
			fin >> dec >> temp;
//			cout << temp << " :";
			for (int a=0; a<=temp; a++) {
				if(nosurprise == 1) { break; }
				for (int b=0; b<=temp-a; b++) {
					if(nosurprise == 1) { break; }
					for(int c=0; c<=temp-(a+b);c++) {
						if(nosurprise == 1) { break; }
						int d = temp-(a+b+c);
						
						if(((abs(a-b) < 3) && (abs(a-c) < 3) && (abs(b-c) < 3)) && d == 0) {
							if ( (a >= bestresult || b >= bestresult || c >= bestresult) && ((abs(a-b) < 2) && (abs(a-c) < 2) && (abs(b-c) < 2 )) ){
								//Unsurprising match
								countpass++;
//								cout << " Match without surprise for " << temp << " " << a << " " << b << " " << c;
								nosurprise = 1;
							} else if(((abs(a-b) == 2) || (abs(a-c) == 2) || (abs(b-c) == 2)) && (a >= bestresult || b >= bestresult || c >= bestresult)) {
								//Surprising Match
								//cout << " Match with surprise for " << temp << " " << a << " " << b << " " << c;
								if(countsurprise > 0) {
									//cout << " This one can surprise and be above our bestresult...";
									//countsurprise--;
									//countpass++;
									cansurprise = 1;
								}
							}
							
						}
					}
				}
			}
			
			if(cansurprise == 1 && nosurprise == 0 && numsurprise > 0) { whocansurprise++; numsurprise--; countabove++; }
			if(nosurprise == 1) {countabove++; }
//			cout << endl;
		}
	
		
		cout << "Case #" << numcases - readcases + 1 << ": ";
		cout << countabove;
		
		cout << endl;
		readcases--;
	}

	return 0;
}
