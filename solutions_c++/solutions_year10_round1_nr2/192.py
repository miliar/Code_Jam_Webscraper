#include <iostream>

using namespace std;

int D, I, M, N;
int numbers[200];

int getChangeCost(int a, int b) {
	return abs(a-b);
}

int getSmoothCost(int a, int b) {
	if(a == b)
		return 0;
	else
		return (abs(a-b) - 1) / M * I;
}

int getCost() {
	int cost[200][300];
	for(int j=0; j<=255; j++)
		cost[0][j] = 0;
	for(int i=1; i<=N; i++)
		for(int j=0; j<=255; j++) {
			cost[i][j] = cost[i-1][j];
			if(numbers[i] != j)
				cost[i][j] += D;
			for(int k=0; k<=255; k++) {
				if(M == 0 && k != j)
					continue;
				int t = cost[i-1][k] + getChangeCost(numbers[i], j) + getSmoothCost(k, j);
				if(t < cost[i][j])
					cost[i][j] = t;
				t = cost[i-1][k] + getSmoothCost(k, j) + D + I;
				if(t < cost[i][j])
					cost[i][j] = t;
				if(M == 0 && numbers[i] != j)
					continue;
				t = cost[i-1][k] + getSmoothCost(k, numbers[i]) + getSmoothCost(numbers[i], j) + I;
				if(t < cost[i][j])
					cost[i][j] = t;
			}
		}
	int best = cost[N][0];
	for(int j=0; j<=255; j++)
		if(cost[N][j] < best)
			best = cost[N][j];
	return best;
}

int main(int argc, char* argv) {
	int T;
	cin >>T;
	for(int i=0; i<T; i++) {
		cin >>D >>I >>M >>N;
		for(int j=1; j<=N; j++)
			cin >>numbers[j];
		cout <<"Case #" <<i+1 <<": " <<getCost() <<endl;
	}
	return 0;
}
