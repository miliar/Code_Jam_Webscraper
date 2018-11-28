#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8

int T;

char buf[150];

bool check(int mask){
	long long val = 0;
	for (int i=0; buf[i]; i++){
		if (buf[i] != '?'){
			val = (val << 1) | (buf[i] - '0');
		} else {
			val = (val << 1) | (mask & 1);
			mask >>= 1;
		}
	}
	long long root = sqrt((double) val) - 1;
	while (root * root < val){
		root++;
	}
	if (root * root == val){
		return true;
	} else {
		return false;
	}
}

void answer(int mask){
	long long val = 0;
	for (int i=0; buf[i]; i++){
		if (buf[i] == '?'){
			buf[i] = '0' + (mask & 1);
			mask >>= 1;
		}
	}
}

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		cin >> buf;
		for (int i=0; i<(1<<20); i++){
			if (check(i)){
				answer(i);
				cout << buf << endl;
				break;
			}
		}
	}
	return 0;
}