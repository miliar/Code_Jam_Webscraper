#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ofstream fout("A.out");
	ifstream fin("A.in");

	string check = "yhesocvxduiglbkrztnwjpfmaq";

	int T, cc = 1;
	char a;

	fin >> T;
	fin.get(a);
	
	while(T--){	
		string befTran;		
		getline(fin, befTran);

		string afTran = befTran;
		for(int i = 0; i < befTran.length(); i++){
			if( afTran[i] == ' ')	continue;
			afTran[i] = check[befTran[i] - 'a'];
		}

		fout << "Case #" << cc++ << ": " << afTran << endl;
	}

	return 0;
}