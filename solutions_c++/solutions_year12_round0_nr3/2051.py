#include <iostream>
#include <algorithm>
using namespace std; 
int getdigits(int a){
	int len = 0; 
	while (a > 0){
		len++;
		a /= 10; 
	}
	return len; 
}

int main(){
	freopen("/Users/qiaomiao/Downloads/C-large.in", "r", stdin);
	freopen("/Users/qiaomiao/code/googlejam/out.txt", "w", stdout);
	int t, A, B, tot, len; 
	int tens[9] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
	int* a = new int[10];
	cin >> t; 
	for (int i = 0; i < t; i++){
		cout << "Case #" << i+1 <<": ";
		cin >> A >> B; 
		len = getdigits(A); 
		tot = 0;
		for (int j = A; j <= B; j++) {
			for (int k = 0; k < len; k++) {
				a[k] = j/tens[k] + (j % tens[k]) * tens[len - k];
				if (a[k] > B || a[k] < A) a[k] = j; 
			}
			sort(a, a + len);
			for (int k = 1; k < len; k++) if (a[k] != a[k - 1]) tot++; 
		}
		tot /= 2;
		cout << tot << endl; 
	}
	fclose(stdin);
	fclose(stdout);
}