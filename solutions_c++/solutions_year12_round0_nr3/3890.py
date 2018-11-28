//recycled numbers solution by Aaron Dimet

#include <vector>
#include <iostream>
#include <string>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>

using namespace std;

int M;
int n;

bool find(int offset, string & N, string & B, int numA, int numB){
	char temp[N.length()];
	for(int i = 0; i < N.length(); i++){
		if(i + offset < N.length()) temp[i] = N[i+offset];
		else{
			temp[i] = N[i + (offset-N.length())];
			}

		}
		M = atoi(temp);
		if(M <= numB and M >= numA and M > atoi(N.c_str())){
			n =  atoi(N.c_str());
			return true;
			}
		else return false;	
		}


int main(){
	
	string line;
    getline(cin, line);
    int tests = atoi(line.c_str());
   //cerr << "Tests = " << tests << endl;
	int poss;

	for(int cases = 0; cases < tests; cases++){
		poss = 0;
		string A,B;
		getline(cin, A, ' ');
		getline(cin, B);
		int numA = atoi(A.c_str());
		int numB = atoi(B.c_str());
	
		if(numA < 10 and numB < 10) poss = 0;
		else{
			for(int i = numA; i <= numB; i++){
				stringstream convert;
				convert << i;
				A = convert.str();
				vector<int> matched;
				for( int offset = 1; offset < A.length(); offset++){
					if(find(offset, A, B, numA, numB)){
						int k;
						for(k=0; k < matched.size(); k++){
							if(matched[k] == M) break;	
							}
						if(k == matched.size()) {
							matched.push_back(M);
							poss++;
							}
						//cerr << "N = " << n << ", ";
						//cerr << "M = " << M;
						//cerr << "      match # " << poss << endl;
						}
					}
				matched.clear();
				}
			}
		cout << "Case #" << cases+1 << ": " << poss << endl;
		}
	return 0;
	}
	

						
