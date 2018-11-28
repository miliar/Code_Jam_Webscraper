#include <iostream>
#include <fstream>
#include <string>
#include <math>
using namespace std;


int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	if(!fin){
		cout << "Cannot open the file.\n";
		return 1;
	}

	int N;		
	string str;
	fin >> N; 
	getline(fin, str);
	
	string w2cj = "welcome to code jam";

	for(int i=0;i<N;i++){
		getline(fin, str);

//		cout << str << endl;

		int pibot[19]; // w2cj has 19chrs.
		int keyChr = 0;
		int counter = 0;
		for(int j=0;j<19;j++) pibot[j] = j;

		while(pibot[0]<=(int)str.size()-19 && keyChr>=0 ){
			unsigned int loc = str.find(w2cj[keyChr],pibot[keyChr]);
			//cout << " loc= " << loc << endl;
			if( loc != string::npos ){
				if(keyChr==18){
					counter++;
					pibot[keyChr]=loc+1;
					if(pibot[keyChr]>=(int)str.size()){
						keyChr--;
						pibot[keyChr]++;
					}
				}else{
					pibot[keyChr]=loc;
					keyChr++;
					pibot[keyChr]=loc+1;
				}
			}else{
				keyChr--;
				pibot[keyChr]++;
			}
		}


		fout << "Case #" <<i+1 << ": " ;
		fout << counter / 1000 ;
		fout << (counter % 1000) / 100 ;
		fout << (counter % 100) / 10 ;
		fout << (counter % 10)  << endl;



	}

	fin.close();
	fout.close();
}



