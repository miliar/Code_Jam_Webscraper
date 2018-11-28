#include <iostream>
#include <vector>
#include <string>
#include <cstring>

//#define __SMALL_DATASET__
#define __LARGE_DATASET__

#ifdef __SMALL_DATASET__
	const int l_size = 10,
		d_size = 25,
		n_size = 10;
#else
	const int l_size= 15,
		d_size = 5000,
		n_size = 500;
#endif

using namespace std;

bool is_match(string word, string acase) {
	int i = 0, j = 0;
	bool par = false;
	while (acase[j]) {
		if (par) {
			if (acase[j] == word[i]) {
				while(acase[j] != ')') j++;
				j++;
				i++;
				par = false;
			} else if (isalpha(acase[j])) {
				j++;
			} else
				return false;

		} else {
			if (acase[j] == word[i]) {
				i++; j++;
			} else if (acase[j] == '(') {
				par = true;
				j++;
			} else 
				return false;
		}
		
	}

	return true;
}

int main() {
	int l, d, n; /* l = length of each word, d = count of words, n = test cases */
	vector<string> words, cases;
	int match_count;
	int i, j;
	
	cin >> l >> d >> n;
	
	for (i = 0; i < d ; i++) {
		char temp[1000];
		cin >> temp;
		words.push_back(temp);
	}

	for (i = 0; i < n; i++) {
		char temp[1000];
		cin >> temp;
		cases.push_back(temp);
	}
	
	for (i = 0; i < n; i++) {
		match_count = 0;
		for (j = 0; j < d; j++) {
			if (is_match(words[j], cases[i]))
				match_count++;
		}
		cout << "Case #" << i+1 << ": " << match_count << endl;
	}	

	return 0;
}