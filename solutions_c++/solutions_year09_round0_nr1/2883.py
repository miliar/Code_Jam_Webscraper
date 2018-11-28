/*
 * words.cpp
 *
 *  Created on: 3/09/2009
 *      Author: Ting
 */

#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	int l, d, n;
	cin >> l;
	cin >> d;
	cin >> n;
	int i, j, k;
	vector<string> dict;
	string w, p;
	for (i=0; i < d; i++) {
		cin >> w;
		dict.push_back(w);
	}


	char a;
	vector<string> pattern;
	string::iterator it;
	for (i=0; i < n; i++) {
		cin >> p;
		pattern.push_back(p);
	}

	for (i = 0; i < n; i++)
	{
		int count= 0;
		p = pattern[i];
		for (j = 0; j < d; j++){
			bool match = true;
			w = dict[j];
			it = p.begin();
			for (k = 0; k < l; k++)
			{
				bool match1 = false;
				a = w.at(k);
				if (*it != '(') {
					if (a != *it) match = false;
				}
				else{
					++it;
					while(*it!=')'){
						if (!match1){
							match1 = a==*it;
						}
						++it;
					}
					if(!match1) match = false;
				}
				++it;
			}
			if(match) count++;
		}
		cout << "Case #" << (i+1) << ": " << count << endl;
	}
	return 0;
}
