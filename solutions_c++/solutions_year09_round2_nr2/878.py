#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

	int T;
	cin >> T;
	getchar();

	int num;
	//int temp;
	
	vector <char> V, temp;

	char ch;

	for (int i= 0; i < T; i++ ) {
		long double num = 0;
		V.clear();
		while ( (ch =getchar()) != '\n') {
			V.push_back(ch);
			num = (num *10)+(ch-'0');
		}

		//cout << ": " << num;
		//cin >> num;

		temp = V;

		//reverse (V.begin(), V.end());

		next_permutation(V.begin(), V.end() );

		long double ans = 0;
		int k =1;

		for (int j = 0; j < V.size(); j++ ) {
			//cout << V[j];

			ans = (ans*10 + (V[j]-'0')) ;
			//k*= 10;
		}

		
		cout << "Case #" << i+1 << ": ";
		bool flag = true;
		


		
		if (ans > num) {
			for ( int ii =0 ;ii < V.size(); ii++ ) {
				cout << V[ii];
			}
		//}
			cout <<  endl;
		} else {
			//cout << "Anik";
			V.push_back('0');
			sort(V.begin(), V.end());
			if ( V[0] == '0' ) {
				int kk,lk;
				for (lk = 0; V[lk] == '0' ; lk++ );
				cout << V[lk];
				for ( kk = 0; kk < lk; kk++ ) {
					cout << "0";
				}
				for ( lk = kk+1 ; lk < V.size(); lk++ ) {
					cout << V[lk];
				}
			}

			cout<< endl;


		}


	
	
	}
	return 0;
}
