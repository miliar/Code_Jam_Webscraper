#include "iostream"
#include "fstream"

using namespace std;

int main(int argc, char** argv){

	ifstream inFile(argv[1],ios::in);
	ofstream outFile(argv[2],ios::out);

	int T;
	inFile >> T;
	cout << T <<endl;
	for(int i = 0 ; i < T ; ++ i){
		cout << "Case #" << i+1 <<": ";
		outFile << "Case #" << i+1 <<": ";
		int Pd,Pg,N;
		inFile >> N >> Pd >> Pg;
		int a,b;
		b = 0;
		for(a = 1 ; a <= 100 && a <= N; ++a){
			if(float(a)*Pd/100 == a*Pd/100){
				b = a * Pd/100;
				break;
			}
		}
		cout << a << "  " << b << endl;
		cout << 100 - a << "  " << Pg - b << endl ;
		if(100-a >= Pg-b && Pg -b >= 0) {
			if( b != 0 || Pd == 0){
				outFile << "Possible" << endl;
			}else{
				outFile << "Broken" << endl;
			}
		}
		else outFile << "Broken" << endl;
	}
}
