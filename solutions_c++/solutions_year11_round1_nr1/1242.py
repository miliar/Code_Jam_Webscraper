#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t=1;t<=T;t++) {
		cout << "Case #" << t << ": ";

		int PD, PG, N;
		cin >> N >> PD >> PG;

		int f=1;
		if (PD%4==0) f*=4;
		else if (PD%2==0) f*=2;
		if (PD%25==0) f*=25;
		else if (PD%5==0) f*=5;

		if (N*f>=100) {
			if (PG==100 && PD !=100) cout << "Broken";
			else if (PG==0 && PD !=0) cout << "Broken";
			else cout << "Possible";
		}
		else cout << "Broken";
		int g=(100/f);
		//cout << N << " " << PD << " " << PG << ": " << g << " " << g*PD << ",.............." << ;

		cout << endl;
	}

	return 0;
}