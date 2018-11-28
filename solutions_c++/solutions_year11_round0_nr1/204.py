#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin>>T;
	for (int i=1; i<=T; i++) {
		int N; cin>>N;

		int t=0, tO=0, tB=0, pO=1, pB=1;
		while(N--) {
			char ch; int p; cin>>ch>>p;
			int curr;
			switch(ch) {
				case 'B':
					curr=max(abs(p-pO)-tB,0)+1;
					tO+=curr;
					pO=p;
					tB=0;
					break;
				case 'O':
					curr=max(abs(p-pB)-tO,0)+1;
					tB+=curr;
					pB=p;
					tO=0;
					break;
			}
			t+=curr;
		}
		cout << "Case #" << i << ": " << t << endl;
	}
	return 0;
}
