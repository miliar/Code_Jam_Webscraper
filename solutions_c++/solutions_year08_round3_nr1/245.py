#include<iostream>
#include<algorithm>
using namespace std;

bool comp(long long i1, long long i2){
	return i1 > i2;
}

int main(){
	int N;
	cin >> N;
	for(int times = 1; times <= N; times++){
		int P, K, L;
		cin >> P >> K >> L;
		long long freq[1001];
		for(int i = 0; i < L; i++){
			cin >> freq[i];
		}
		sort(freq, freq+L, comp);
		long long count = 0;
		int cP = 1;
		int cK = 0;
		for(int i = 0; i < L; i++){
			count += freq[i] * cP;
			cK++;
			if(cK >= K){
				cK = 0;
				cP++;
			}
		}
		cout << "Case #" << times << ": " << count << endl;
	}
	return 0;
}
