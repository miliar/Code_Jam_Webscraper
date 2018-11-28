#include <iostream>
#include <string>

using namespace std;

#define MAXN 128

int main(){
	int N;

	int x[MAXN], y[MAXN];

	cin >> N;
	for(int Case = 1; Case <= N; Case++){
		unsigned long long int n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

	unsigned long long int X = x0, Y = y0;
	x[0] = (int)X, y[0] = (int)Y;
	for(int i = 1; i <= (int)(n-1); i++){
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		x[i] = (int)(X % 3), y[i] = (int)(Y % 3);
	}

	int count = 0;
	for(int i = 0; i < (int)n; i++)
		for(int j = i+1; j < (int)n; j++)
			for(int k = j+1; k < (int)n; k++)
				if (((x[i] + x[j] + x[k]) % 3 == 0) && ((y[i] + y[j] + y[k]) % 3 == 0))
					count++;

		cout << "Case #" << Case << ": " << count << endl;
	}
	return 0;
}
