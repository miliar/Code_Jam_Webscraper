#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#define For(I,A,B) for(int I = A; I < B; ++I)
using namespace std;

int main(){
	ifstream cin ("C-large.in");
	ofstream cout ("output.txt");
	int T;
	cin >> T;
	For(q,1,T+1){
		int N,r=0,b;
		long long S = 0;
		cin >> N;
		vector <int> a(N);
		For(i,0,N){
			cin >> b;
			r = r^b;
			S += a[i] = b;
		}
		if (r)
			cout << "Case #" << q << ": NO\n";
		else
			cout << "Case #" << q << ": " << S - (*min_element(a.begin(),a.end())) << endl;
	}
	return 0;
}