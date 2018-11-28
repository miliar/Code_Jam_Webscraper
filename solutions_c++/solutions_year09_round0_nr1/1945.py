#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int L, D, N;
	int d, wordinc, l, n, testinc, x, count, match, lettermatch;
	char a;
	char words[80000];
	char tests[15][30];
	int testarray[15];
	ifstream myfile ("input.in");
	ofstream output ("output.txt", ios::trunc);
	myfile >> L >> D >> N;

//cout << L <<" " << D <<" " << N <<"\n";

	wordinc=0;
	for (d=0;d<D;d++) {
		for (l=0;l<L;l++) {
			myfile >> words[wordinc];
			wordinc++;
		}
	}

//wordinc=0;
//for (d=0;d<D;d++) {
//	cout << d << " ";
//	for (l=0;l<L;l++) {
//		cout << words[wordinc];
//		wordinc++;
//	}
//	cout << "\n";
//}

	for (n=1;n<=N;n++) {
		for (l=0;l<L;l++) {
			myfile >> a;
			if (a=='(') {
				x=0;
				myfile >> a;
				do {
					tests[l][x] = a;
					x++;
					myfile >>a;
				} while (a!=')');
				tests[l][x]=-1;
			}
			else {
				tests[l][0]=a;
				tests[l][1]=-1;
			}
		}

//for (l=0;l<L;l++) {
//	cout <<l;
//	for (x=0;tests[l][x]!=-1;x++) {
//		cout << tests[l][x];
//	}
//	cout << " ";
//}
//cout <<"\n";

	wordinc=0;
	count=0;
	for (d=0;d<D;d++) {
		match=1;
		for (l=0;l<L;l++) {
			lettermatch=0;
			for (x=0;tests[l][x]!=-1;x++) {
				if (words[wordinc]==tests[l][x]) lettermatch=1;
			}
			if (lettermatch==0) match=0;
			wordinc++;
		}
		if (match==1) count++;
	}

cout << count <<"\n";
output << "Case #" << n << ": " << count << "\n";
		
	}
	return 0;
}

