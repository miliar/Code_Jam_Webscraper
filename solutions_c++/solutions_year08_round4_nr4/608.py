#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void apply(char str1[], char str2[], int arr[], int k) {
	int i = 0;
	while(str1[i] != 0) {
		for(int j = 0; j < k; j++) {
			str2[i+j] = str1[i+arr[j]];
		}
		i = i+k;
	}
	str2[i] = 0;
}

int main() {
	int N;
	cin >> N;
	char str[2000], str2[2000];
	int k;
	int arr[5];
	for (int n = 1; n <= N; n++) {
		cin >> k;
		cin >> str;
		for(int i = 0; i < k; i++)
			arr[i] = i;
		int min = 100000;
		do {
			apply(str, str2, arr, k);
			int len = 0;
			char cur = ' ';
			for(int i = 0; str2[i] != 0; i++) {
				if(str2[i] != cur) {
					cur = str2[i];
					len ++;
				}
			}
			if(min > len)
				min = len;
		} while(next_permutation(arr, arr+k));
		cout << "Case #" << n << ": " << min << endl;
	}
	return 0;
}