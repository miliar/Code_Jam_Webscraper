#include <iostream>
using namespace std;

typedef long long bint;

int n;
bint v1[800];
bint v2[800];

void input() {
	cin >> n;
	for(int i=0;i<n;i++)
		cin >> v1[i];
	for(int i=0;i<n;i++)
		cin >> v2[i];
}

int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		sort(v1, v1+n);
		sort(v2, v2+n);
		bint tot = 0;
		for(int i=0;i<n;i++) {
			tot += v1[i]*v2[n-1-i];			
		}
		cout << "Case #" << casei << ": " << tot << endl;
	}
	
	return 0;
}
