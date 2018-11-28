#include <iostream>
#include <math.h>

#include <set>

using namespace std;

set<int> myset;
	



int run() {
	int a, b;
	int r = 0;
	cin >> a;
	cin >> b;

	int n = log10(b);
	int m = pow(10,n);

	for(int i=a; i<b; i++) {
		int j=i;
		//~ cout << "########## " << i << " ##########" << endl;
		myset.clear();
		
		for(int k=0; k<n; k++) {
			j = (j%m)*10 + (j/m);
			//~ cout << j << endl;
			if(j>i && j<b+1) myset.insert(j);
		
		}
		r += myset.size();
	}
	
	
	
	return r;
}



int main() {
	int n;
	cin >> n;
	for(int i=0; i<n; i++) {
		cout << "Case #" << i+1 << ": " << run() << endl;
	}
	
	return 0;
}