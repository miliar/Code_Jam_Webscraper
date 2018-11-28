#include <iostream>
#include <vector> 
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	int L, D, N;
	string str;

	vector <int> W;

	cin >> L >> D >> N;
	
	vector <string> lang;

	for ( int i = 0; i < D; i++ ) {
		//getline(cin, str);
		str.clear();
		cin >> str;
		lang.push_back(str);
	}

	for (int i = 0; i < N; i++ ) {
		int n = 0;
		W.clear();
		W.resize(D);

		cin >> str;

		if(str.size() == L) {
			if ( find(lang.begin(), lang.end(), str) != lang.end()) {
				n = 1;
			}
		} else {
			for (int j = 0, m = 0; j < str.size(); j++ ) {
				
				if( str[j] != '(' ) {
					//cout << "tulla";
					for (int k = 0; k < D; k++ ) {
			//			cout << lang[k];
						if(lang[k][m] == str[j]) { 
							//cout << "A";
							W[k]++;
						}	
					}
					m++;
				} else {
					//cout << "tulla";	
					//t//emp = P;
					//P.clear();
						
					while(str[++j] != ')') {
						for (int k = 0; k < D; k++ ) {
							if(lang[k][m] == str[j]) {
								W[k]++;
							}	
							
						}
					}
					m++;
				
				}

				
			}
			for (int k =0; k < D; k++ ) {
				if(W[k] ==  L) {
				//cout << W[k] << endl;
					n++;
				}
			}

		}
		cout << "Case #" << i+1 << ": " << n << endl; 
		str.clear();
		
	}

	//cout << endl;


	return 0;
}
