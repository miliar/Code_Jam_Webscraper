#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
    //ifstream in("..//..//sample.in.txt");
	ifstream in("..//..//A-small-attempt0.in.txt");
	if (!in)
	{
		cout << "Input file cannot be opened";
		return 1;
	}
	
	ofstream out("output.txt");
	if (!out) {
		cout << "Output file cannot be opened";
		in.close();
		return 1;
	}
	
	int T;
	in >> T;
	
	for (int t = 0; t < T; t++) {
		bool isPossible = false;
		int N, PD, PG;		
		in >> N >> PD >> PG;
		
		int D;
		for (int n = 1; n <= N; n++) {
			if (PG == 100 && PD != 100)
				break;
			else if(PG == 0 && PD != 0) {
				break;
			}
			
			D = n;
			
			if ((D * PD) % 100 != 0)
				continue;
			
			// D is found
			cout << "D = "<< D << endl;
			int DW = D * PD / 100;
			cout << "DW = " << DW << endl;			
			
			int GW = DW;
			int PGN = PG;
			int PGD = 100;
			
			// reduced
			if (PGN % 4 == 0) {
				PGN = PGN / 4;
				PGD = PGD / 4;				
			}
			else if (PGN % 2 == 0) {
				PGN = PGN / 2;
				PGD = PGD / 2;				
			}
			
			if (PGN % 25 == 0) {
				PGN = PGN / 25;
				PGD = PGD / 25;				
			}
			else if (PGN % 5 == 0) {
				PGN = PGN / 5;
				PGD = PGD / 5;				
			}
			cout << "PGN = " << PGN << endl;
			cout << "PGD = " << PGD << endl;
			
			//int G = PGN * GW * PGD;
			int G = PGD;
			
			cout << "G = " << G << endl;			
			if (G >= D) 
			{
				isPossible = true;	
				break;
			}
		}		
		
		cout << "Case #" << (t + 1) << ": " << (isPossible ? "Possible" : "Broken") << endl;
		out << "Case #" << (t + 1) << ": " << (isPossible ? "Possible" : "Broken") << endl;
	}
	
	in.close();
	out.close();
	
    return 0;
}
