#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

int count[10], _count[10];

void calCount(int N, int *arr){
	for(int i = 0; i < 10; i++)
		arr[i] = 0;
	while(N){
		arr[N%10]++;
		N /= 10;
	}
}

bool eq(){
	for(int i = 1; i < 10; i++)
		if(count[i] != _count[i])
			return false;
	return true;
}

int main() {
    freopen("B-small.in", "r", stdin);
    freopen("B-small.txt", "w", stdout);

	int T;
	cin >> T;
    for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		calCount(N, count);
		do
			calCount(++N, _count);
		while(!eq());
		cout << "Case #" << t << ": " << N << endl;
    }

    return 0;
}
