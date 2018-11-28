#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;

#define MAX_N 100
#define MAX_C 36
#define MAX_D 28


int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int T;
	fin >> T; 
//	cout << "T:" << T << endl;
	
	
	for(int i=0;i<T;i++){
		// input data
		long C;
		fin >> C;
//		cout << "C:" << C << endl;
		string cmb[MAX_C*2]; //combine forms
		for( int j=0;j<C;j++ ){
			fin >> cmb[j*2];
			cmb[j*2+1] = cmb[j*2].substr(1,1) + cmb[j*2].substr(0,1) + cmb[j*2].substr(2,1) ;
		}

		long D;
		fin >> D;
//		cout << "D:" << D << endl;
		string ops[MAX_D*2]; //oppose forms
		for( int j=0;j<D;j++ ){
			fin >> ops[j*2];
			ops[j*2+1] = ops[j*2].substr(1,1) + ops[j*2].substr(0,1) + ops[j*2].substr(2,1);
		}

		long N;
		fin >> N;
//		cout << "N:" << N << endl;
		string inv; //invoked strings
		fin >> inv;
//		cout << inv << endl;

	
		// main
		string elt; // element list
		long j;
		int caseno; // for debugging
		j=0;
		while(j<N){
			// invoking
			elt += inv.substr(j,1);
			
			// if there is only one element in the element list 
			if(elt.length()==1){
				caseno = 1;
				goto ENDD;
			}

			// to search a combinable pair
			for(int k=0;k<C*2;k++){
				if(cmb[k].substr(0,2) == elt.substr(elt.length()-2,2)){
					elt.replace(elt.length()-2,2,cmb[k].substr(2,1));
					caseno = 2;
					goto ENDD;
				}
			}

			// to search a oppsit pair
			for(unsigned int k=0;k<elt.length()-1;k++){
				for(int m=0;m<D*2;m++){
					if(ops[m].substr(0,2) == elt.substr(k,1)+elt.substr(elt.length()-1,1)){
						elt.erase();
						caseno=3;
						goto ENDD;
					}
				}
			}

			caseno=0;
ENDD:
			j++;
//			cout << "j:" << j << ", Case:" << caseno <<  ", elist:" << elt << endl;
		}

		fout << "Case #" << i+1 << ": [" ;
		for(unsigned int k=0; k<elt.size(); k++){
			fout << elt[k];
			if(k<elt.size()-1){
				fout << ", ";
			}
		}
		fout << "]" << endl;

	}

	fin.close();
	fout.close();
}



