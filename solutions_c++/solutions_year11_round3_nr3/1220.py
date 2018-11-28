#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int N;
	cin >> N;
	for(int i = 0; i < N; i++){
		int A,L,H;
		cin >> A >> L >> H;
		vector <int> V;
		V.resize(A);
		for(int j = 0; j < A; j++){
			cin >> V[j];
		}
		int vys = 0;
		bool ok;
		for(int j = L; j < H+1; j++){
			ok = true;
			for(int k = 0; k < A; k++){
				if( V[k] % j == 0 || j % V[k] == 0) vys = j;
				else ok = false; 
			}
			if (ok) {
				cout << "Case #" << i+1 << ": "<< j << endl;
				break;
			}
		}
		if(!ok) cout << "Case #" << i+1 << ": NO" << endl; 
	}
    //system("PAUSE");
    return 0;
}
