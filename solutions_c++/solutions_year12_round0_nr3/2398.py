#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int A, B, digits, total, tmp;

void procesar(int num){
	int k, pos = digits-1, pivote, pot, current, limit, n1, m1;
	char n[digits], m[digits];
	bool distinct;
	vector<int> gen;
	vector<int>::iterator it;
	n1 = num;
	// num to string
	distinct = false;
	current = num%10;
	while(pos >= 0){
		n[pos] = num%10 + '0';
		if(current != num%10)
			distinct = true;
		current = num%10;
		num /= 10;
		pos -= 1;
	}
	if(distinct){
		// corrimientos
		limit = digits-1;
		pivote = limit;
		while(pivote >= 1){
			// corrimiento circular
			for(k = 0; k < digits; k++){
				m[k] = n[pivote%digits];
				pivote += 1;
			}
			// string back to num
			m1 = 0;
			pot = 1;
			for(k = digits-1; k >= 0; k--){
				current = m[k] - '0';
				m1 += current*pot;
				pot *= 10;
			}
			// compare
			if((m1 > n1) && (m1 <= B)){
				it = find(gen.begin(), gen.end(), m1);
				if(it == gen.end()){
					gen.push_back(m1);
					total += 1;
				}
			}
			limit -= 1;
			pivote = limit;
		}
	}
	gen.clear();
}

int main(){
	int T, i, j;
	cin >> T;
	for(i = 1; i <= T; i++){
		cin >> A >> B;
		total = 0;
		digits = 0;
		// count number of digits
		tmp = A;
		while(tmp != 0){
			tmp /= 10;
			digits += 1;
		}
		// check for every number between A and B
		for(j = A; j < B; j++)
			procesar(j);
		cout << "Case #" << i << ": " << total << endl;
	}
	return 0;
}
