#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(void) {

	int numProbs;
	cin >> numProbs;

	for (int pnum = 1; pnum <= numProbs; pnum++) {

		map<char,bool> existence;
		for (char x = '0'; x <= '9'; x++)
			existence[x] = false;
		for (char x = 'a'; x <= 'z'; x++)
			existence[x] = false;

		string text;
		cin >> text;

		// Update existences
		for (int i = 0; i < text.size(); i++)
			existence[text[i]] = true;

		// Count exists
		int base = 0;
		for (char x = '0'; x <= '9'; x++)
			if (existence[x]) base++;
		for (char x = 'a'; x <= 'z'; x++)
			if (existence[x]) base++;
		if (base <= 1) base = 2;

		// Value per symbol
		map<char,int> symbols;
		for (char x = '0'; x <= '9'; x++)
			symbols[x] = -1;
		for (char x = 'a'; x <= 'z'; x++)
			symbols[x] = -1;

		
		int curval = 0;
			
		// Assign values
		symbols[text[0]]=1;
		for (int i = 1; i < text.size(); i++)
			if (symbols[text[i]]==-1) {
				if (curval == 1) curval = 2;
				symbols[text[i]] = curval;
				curval++;
			}

		// Calculate value
		long long basemulti = 1;
		long long val=0;
		for (int i = text.size()-1; i >=0; i--) {
			val += symbols[text[i]]*basemulti;
			basemulti*=base;
		}

		cout << "Case #" << pnum << ": " << val << endl;

	}

	return 0;
}