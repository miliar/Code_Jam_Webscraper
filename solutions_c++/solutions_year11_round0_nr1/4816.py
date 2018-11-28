#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

int main() {

	int t,n;
	char tempR; //robot
	int tempP; //position
	int WaitO, WaitB;
	int PosO,PosB;
	int dif; //dif = distance
	int total;
	//ofstream out;
	//ifstream in;


	//in.open("input.txt");
	//out.open("output.txt");
	cin >> t;

	for (int i=0;i<t;i++) {
		cin  >> n;
		PosO = 1;
		PosB = 1;
		WaitO = 0;
		WaitB = 0;
		total = 0;
		for (int j=0;j<n;j++) {
			cin >> tempR;
			cin >> tempP;

			if (tempR=='O') {
				dif = abs(PosO-tempP);
				dif = dif- WaitO;
				if (dif < 0) {
					dif=0;
				}
				dif++;
				total+= dif;
				WaitB+= dif;
				PosO=tempP;
				WaitO=0;
			}

			else {
				dif = abs(PosB-tempP);
				dif = dif- WaitB;
				if (dif < 0) {
					dif=0;
				}
				dif++;
				total+= dif;
				WaitO+= dif;
				PosB=tempP;
				WaitB=0;
			}
		}
		cout <<"Case #" << i+1 << ": " <<total <<endl;
	}


	return 0;
}
