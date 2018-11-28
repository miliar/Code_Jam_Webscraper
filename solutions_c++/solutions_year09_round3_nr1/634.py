#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
#include <math.h>
using namespace std;




int main(){
	int n;	
	cin >> n;	
	for(int i = 0; i < n; i++){

		string code;
		cin >> code;
		if (code.length() == 1){
			cout << "Case #" << i + 1 << ": 1" << endl;
			continue;
		}
		vector <char> trans;
		for (int k = 0; k < code.length(); k++){
			bool istrans = false;
			for(int j = 0; j < k; j++)
				if (code[j] == code[k]){
					istrans = true;
					break;
				}
			if (!istrans)
				trans.push_back(code[k]);
		}
		if(trans.size() == 1)
			trans.push_back('!');
		
			
			swap(trans[0], trans[1]);
		
		long long res = 0;
		int base = trans.size();
		for (int j = 0; j < code.length(); j++){
			int price;
			for(int k = 0; k < trans.size(); k++)
				if (trans[k] == code[j]){
					price = k;
					break;
				}
				
			res += price;
			if (j != code.length() - 1)
				res *= base;
		}
		cout << "Case #" << i + 1 << ": " << res << endl;
	
		
	}
}