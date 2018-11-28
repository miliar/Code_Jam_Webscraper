#include<iostream>
#include<algorithm>
using namespace std;

int kaimynas[10001], kaimynas2[10001];
bool pan[10001];

int main() {
	long rez = 0;
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		fill(kaimynas, kaimynas+10001, -1);
		fill(kaimynas2, kaimynas2+10001, -1);
		fill(pan, pan+10001, false);
		int N;
		rez = 0;
		cin >> N;
		for(int u = 1; u <= N; u++) {
			int A, B;
			cin >> A >> B;
			kaimynas[A] = B;
			kaimynas2[B] = A;
		}
		for(int m = 1; m <= 10000; m++)
		if (kaimynas[m] != -1) {
			for(int n = 1; n < kaimynas[m]; n++) 
			if (kaimynas2[n] != -1)
				if (!pan[n])
					rez++;
			pan[kaimynas[m]] = true;
		}
		cout << "Case #" << i << ": " << rez << endl;
	}
	return 0;
}
