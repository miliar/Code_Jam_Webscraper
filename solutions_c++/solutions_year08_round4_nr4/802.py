#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
	int A[1000000];

int main() {
	
			int nTC;
	scanf("%d", &nTC);
	
	for (int kasus=1; kasus<=nTC; kasus++) {
		int K;
		string s;
		string s1;
		scanf("%d", &K);
		cin >> s;
		s1=s;
		for (int i=1; i<=K; i++) A[i-1]=i-1;
		int hasil=1000000000;
		do {
			for (int j=0; j<s.length()/K; j++) {
			for (int i=0; i<K; i++) {
				s1[j*K+A[i]]=s[j*K+i];
			}
			}
			//cout << s1 << endl;
			int nunik=1;
			for (int i=1; i<s1.length(); i++) {
				if (s1[i]!=s1[i-1])
					nunik++;
			}
			hasil=min(hasil, nunik);
		} while (next_permutation(A, A+K));
		printf("Case #%d: %d\n", kasus, hasil);
	}
	return 0;
}
