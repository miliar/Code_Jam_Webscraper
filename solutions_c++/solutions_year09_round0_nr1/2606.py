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
	int n, d, l;
	
	cin >> l;
	cin >> d;
	cin >> n;
	string* dict;
	dict = new string[d];
	
	for(int i = 0; i < d; i++)
		cin >> dict[i];
	for(int i = 0; i < n; i++){
		char c;
		c = getchar();
		vector <char>* word;
		
		vector <char> letter;
		word = new vector <char> [l];
		for(int j = 0; j < l; j++){
			
			letter.clear();
			c = getchar();
			if (c == '('){
				c = getchar();
					while (c != ')'){
						letter.push_back(c);
						c = getchar();
					}
			}
			else
				letter.push_back(c);
			word[j] = letter;
			
		}
		int res = 0;
		for(int i = 0; i < d; i++){
			bool maybe = true;
			for(int j = 0; j < l; j++){
				bool isin = false;
				for (int k = 0; k < word[j].size(); k++){
					if (word[j][k] == dict[i][j]){
						isin = true;
						break;
					}
				}
					if (!isin){
						maybe = false;
						break;
					}
			}
			if (maybe)
				res++;
		}
				

		
		cout << "Case #" << i + 1 << ": " << res << "\n";
	}
}