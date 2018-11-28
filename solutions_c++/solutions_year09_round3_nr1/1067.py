#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <cmath>

using namespace std;

int main(){
	string S;
	size_t found;
	int used = 0;
	int T;
	ifstream input;
	input.open ("A-small-attempt0.in");
	
	input >> T;

	for (int i = 0; i < T; i++){
		input >> S;
		int A[S.length()];
		for (int j = 0; j < S.length(); j++){
			A[j] = -1;
		}
		for (int k = 0; k < S.length(); k++){
			if (k == 0){
				A[k] = 1;
				used = 1;
				found = S.find(S[k],k+1);
				while(found != string::npos){
					A[found] = 1;
					found = S.find(S[k],found+1);
				}
			}
			else if (A[k] == -1){
				if (used == 1){
					A[k] = 0;
					used = 2;
					found = S.find(S[k],k+1);
					while(found != string::npos){
						A[found] = 0;
						found = S.find(S[k],found+1);
					}
				}
				else{
					A[k] = used;
					found = S.find(S[k],k+1);
					while(found != string::npos){
						A[found] = used;
						found = S.find(S[k],found+1);
					}
					used++;
				}
			}
		}

		string s;
		stringstream out;
		int max = 0;
		for (int l = 0; l < S.length(); l++){
			if (A[l] > max){
				max = A[l];
			}
			out << A[l];
		}
		s = out.str();

		cout << "Case #" << i+1 << ": ";

		if (max == 9){
			cout << s << endl;
		}
		else{
			double sum = 0;
			int loc = 0;
			int len = S.length();
			for (int j = len-1; j >= 0; j--){
				sum += A[j] * pow(max+1,loc);
				loc++;
			}
			printf("%.0f\n", sum);
		}
	}

	return 0;
}
