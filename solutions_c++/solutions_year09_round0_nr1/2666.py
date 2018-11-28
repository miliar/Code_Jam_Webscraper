#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;

void QSort(long x[ ], int left, int right);

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int L, D, N;
	fin >> L >> D >> N; 
//	cout << L << " " << D << " " << N << endl;

	string tkn[5000];

	for(int i=0;i<D;i++)
		fin >> tkn[i];
	
	for(int i=0;i<N;i++){
		string cs;
		fin >> cs;

		int counter;

		counter = 0;
		for(int j=0;j<D;j++){
			bool flgLts; // if there is "(abc..)"
			bool flgOK;
			int numMtc;	
//			string str;
			int m;

			m=0;
			numMtc = 0;
//			tkn[D].copy(str,tkn[D].size(),0);
			flgLts = false; 
			flgOK = false;

			for(int k=0;k<L;k++){ 
				while(m<(int)cs.size() && numMtc<=k){
//					cout <<"  " << m << " : " << cs[m] << " | " << k << ": " << tkn[j][k] << endl;
					
					if(cs[m]=='(') {
						flgLts=true;
						m++;
					}else if(cs[m]==')'){ 
						k=L+1;		//exit for loop
						m=cs.size()+1;
					}else if(cs[m]!=tkn[j][k] && flgLts==false){
						k=L+1;		//exit for loop
						m=cs.size()+1;
					}else if(cs[m]!=tkn[j][k] && flgLts==true){
						m++;
					}else{// if cs[m]== tkn[D][k]
						numMtc++;
						if(flgLts==true){
							for(;cs[m]!=')';m++);
							flgLts=false;
							m++;
						}else{
							m++;
						}
					}
				}
				if(numMtc==L) flgOK=true;
			}

			if(flgOK == true) counter++;

		}


//		cout << "Case #" <<i+1 << ": " << counter << endl;
		fout << "Case #" <<i+1 << ": " << counter << endl;
	}

	fin.close();
	fout.close();
}



