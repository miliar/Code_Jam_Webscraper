#include <vector>
#include <iostream>

using namespace std;

char tbl[100][100];

void shift(int x, int y, int n){
	int pos = 0;
	for(int i = x + 1; i < n; i++){
		if(tbl[y][i] != '.') break;
		pos++;
	}
	if(pos > 0){
		tbl[y][x + pos] = tbl[y][x];
		tbl[y][x] = '.';
	}
}

void rotate(int n){
	for(int i = 0; i < n; i++){
		for(int l = n - 1; l >= 0; l--){
			shift(l, i, n);
		}
	}
}

struct LinearChecker {
	int k;
	int current;
	int count;
	int ret;
	LinearChecker(int k) : k(k) {
		current = 0;
		count = 0;
		ret = 0;
	}

	void push(int n){
		if(current == n){
			count++;
		} else {
			current = n;
			count = 1;
		}
		if(count >= k){
			if(current == 'R'){
				ret |= 1;
			} else if(current == 'B'){
				ret |= 2;
			}
		}
	}
	
	int result(){
		return ret;
	}
	
};

int check(int n, int k){
	int ret = 0;

	for(int i = 0; i < n; i++){
		LinearChecker c1(k);
		LinearChecker c2(k);
		for(int j = 0; j < n; j++){
			c1.push(tbl[i][j]);
			c2.push(tbl[j][i]);
		}
		ret |= c1.result();
		ret |= c2.result();
	}

	for(int i = 0; i < n; i++){
		LinearChecker c1(k);
		LinearChecker c2(k);
		LinearChecker c3(k);
		LinearChecker c4(k);
		for(int j = 0; j < n - i; j++){
			c1.push(tbl[i + j][0 + j]);
			c2.push(tbl[0 + j][i + j]);
			c3.push(tbl[(n - i) - j][0 + j]);
			c4.push(tbl[(n - 1) - j][i + j]);
		}
		ret |= c1.result();
		ret |= c2.result();
		ret |= c3.result();
		ret |= c4.result();
	}
	
	for(int i = 0; i < n; i++){
		LinearChecker c1(k);
		LinearChecker c2(k);
		for(int j = 0; j < n - i; j++){
			
		}
		ret |= c1.result();
		ret |= c2.result();
	}
	

	return ret;
}

int solve(int n, int k){
	rotate(n);
	return check(n, k);
}

int dump(int n){
	cout << "-----------" << endl;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			cout << tbl[i][j] << " ";
		}
		cout << endl;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		int n, k;
		cin >> n >> k;
		for(int j = 0; j < n; j++){
			for(int k = 0; k < n; k++){
				cin >> tbl[j][k];
			}
		}
		//		dump(n);
		int ret = solve(n, k);
		cout << "Case #" << (i + 1) << ": ";
		switch(ret){
		case 0:
			cout << "Neither";
			break;
		case 1:
			cout << "Red";
			break;
		case 2:
			cout << "Blue";
			break;
		case 3:
			cout << "Both";
			break;
		default:
			throw "error";
			break;
		}
		cout << endl;
		//		dump(n);
	}
}
