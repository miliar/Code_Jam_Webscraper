#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t;// test cases
	fin >> t;
	for (int i = 0 ; i < t; i++) {
		int c;//combine strings
		string cs;
		fin >> c;
		char comb[26][26];//combine map
		for (int i1 = 0; i1 < 26; i1++)
			for (int i2 = 0; i2 < 26; i2++) {
				comb[i1][i2] = ' ';//nothing 
			}
		//fout << c;
		for (int j = 0 ; j < c ; j++) {
			fin >> cs;
			char A = cs[0];
			char B = cs[1];
			char combAB = cs[2];
			comb[A - 'A'][B - 'A'] = combAB;
			comb[B - 'A'][A - 'A'] = combAB;
			//fout << cs[j];
		}
		int d;//dipose strings
		string ds;
		fin >> d;
		bool dps[26][26];//dispose map
		for (int i1 = 0; i1 < 26; i1++)
			for (int i2 = 0; i2 < 26; i2++) {
				dps[i1][i2] = false;//nothing 
			}
		//fout << d;
		for (int j = 0 ; j < d ; j++) {
			fin >> ds;
			char A = ds[0];
			char B = ds[1];
			dps[A - 'A'][B - 'A'] = true;
			dps[B - 'A'][A - 'A'] = true;
			//fout << ds[j];
		}
		int n;// n elements
		fin >> n;
		char ele;
		char list[101];// stack
		int top = -1;
		for (int j = 0; j < n; j++) {
			fin >> ele;
			//push
			if ( top == -1) {
				top++;
				list[top] = ele;
			}
			else {
				if ( comb[list[top] - 'A'][ele - 'A'] != ' ') {
					list[top] = comb[list[top] - 'A'][ele - 'A'];
				}
				else {
					top++;
					list[top] = ele;
				}
			}
			//pop
			for (int k = 0 ; k < top; k++) {
				if ( dps[list[top] - 'A'][list[k] - 'A'] ) {
					top = -1;
					break;
				}
			}
		}
		fout << "Case #" << i+1 << ": [";
		for (int k = 0 ; k < top; k++) {
			fout << list[k] << ", ";
		}
		if ( top >= 0) 
			fout << list[top]; 
		fout << "]" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

