#include <iostream>

using namespace std;


int main(){
	int T, N;
	int r[50];
   	char c;
   	
	cin >> T >> ws; 

	for (int cnt = 1; cnt <=T; ++cnt){
		cout << "Case #" << cnt << ": ";
		cin >> N;
		for (int i=0; i<N; ++i){
			r[i] = 0;
			for (int j=0; j<N; ++j){
				cin >> c;
				if (c=='0')
					r[i]++;
				else if (c=='1')
					r[i]=0;
			}
		}
/*		for (int i=0; i<N; ++i){
			cout << "Row " << i << " : " << r[i] << endl;
		} */
		int sum=0;
		for (int j=0; j<N; ++j){
			if (r[j]<N-j-1){
				int i;
				for (i=j+1; i<N; ++i){
					if (r[i]>=N-j-1)
						break;
				}
				if (i>=N)
					cerr << "ERROR! No solution? " << endl;
//				cerr << "MOVE: " << j << " " << i << endl;
				int move = r[i];
				for (int k=i; k>=j+1; --k){
					r[k] = r[k-1];
				}
				r[j] = move;
				sum += i-j;
/*				cerr << "After move: " << endl;
				for (int l=0; l<N; ++l){
					cerr<< r[l] << " " ;
				}
				cout << endl; */
			}
		}
		cout << sum;
		cout << endl;
	}

	cerr << "Program Terminated Properly." << endl;

	return 0;
}
