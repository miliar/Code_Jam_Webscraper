#include <iostream>
#include <fstream>
#include <string>
#include <Vector>
#include <cmath>

using namespace std;

int main(){
string line;
int T=0;
int N=0;
double k=0;

ifstream fin ("c:\\googleCode\\A-small-attempt0.in");
ofstream fout ("c:\\googleCode\\A.txt");

fin >> T;

for (int i=0; i<T; i++){
			string status = "OFF";
			fin >> N;
			fin >> k;

			int on =0;
			for (int j =0; j<N; j++) on += pow(2.0,j);
				
			int P = ((int) k)&on;
			if (P==on) status="ON";
			
			fout << "Case #"<< i+1<<": "<<status <<endl;
			cout << "Case #"<< i+1<<": "<<status <<endl;
		}

fin.close();
fout.close();

}
