#include <iostream>
#include <cstring>

using namespace std;

int main() {
	int t, n, score, min, c;
	int bits[32];
	bool answer_no;
	
	cin >> t;
	for(int j=0; j<t; j++) {
		answer_no = false;
		min = 10000000;
		score = 0;
			
		bzero(bits, 32 * sizeof(int));			
	
		cin >> n;
		for(int i=0; i<n; i++) {
			cin >> c;
			score += c;
			if( c < min ) min = c;
			int mask = 1;
			for(int b=0; b<32; b++) {
				if( c & mask ) bits[b]++;
				mask = mask << 1;	
			} 					
		}

		for(int i=0; i<32 && !answer_no; i++) {
			if( bits[i]%2 ) answer_no = true;
		}			 

		cout << "Case #" << j+1 << ": ";
		if(answer_no )
			cout << "NO\n";
		else  
			cout << score-min << "\n";
	
	}
}


