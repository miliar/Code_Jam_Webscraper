#include<iostream>
#include<vector>
#include<map>
using namespace std;

char combina(char a, char b, vector<string> &VC) {
	for(int i = 0; i < VC.size(); ++i) {
		if((VC[i][0] == a && VC[i][1] == b) || (VC[i][0] == b && VC[i][1] == a)) {
			return VC[i][2];
		}
	}
	return '\0';
}

bool opuestos(char a, char b, vector<string> &VD) {
	for(int i = 0; i < VD.size(); ++i) {
		if((VD[i][0] == a && VD[i][1] == b) || (VD[i][0] == b && VD[i][1] == a)) {
			return true;
		}
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	//cout << T << endl;
	for(int i = 0; i < T; ++i) {
		int C, D, N;
		cin >> C;
		//cout << C << " ";
		vector<string> VC(C);
		for(int j = 0; j < C; ++j) {
			cin >> VC[j];
					//cout << VC[j] << " ";
		}
		
		cin >> D;
		//cout << D << " ";
		vector<string> VD(D);
		for(int j = 0; j < D; ++j) {
			cin >> VD[j];
					//cout << VD[j] << " ";
		}
		
		string R;
		char tmp, comb;
		cin >> N;
		//cout << N << endl;
		if(N--) {
			cin >> tmp;
			R += tmp;
					//cout << tmp;;
		}
		for(int j = 0; j < N; ++j) {
			cin >> tmp;
					//cout << tmp;;
			if(comb = combina(tmp, R[R.size() - 1], VC)) {
				R.erase(R.size()-1);
				R += comb;
			} else {
				bool ingresa = false;
				for(int k = 0; k < R.size(); ++k) {
					if(opuestos(tmp, R[k], VD)) {
						R = "";
						ingresa = true;
					}
				}
				if(!ingresa) {
					R += tmp;
				}
			}
		}
		cout << "Case #" << i+1 << ": [";		
		for(int j = 0; j < R.size(); ++j) {
			if(j) {
				cout << ", ";
			}
			cout << R[j];
		}
		cout << "]" << endl;
	}
	return 0;
}