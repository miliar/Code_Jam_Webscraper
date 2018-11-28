#include <iostream>
#include <string>
#include <deque>
#include <sstream>
#include <cctype>
#include <algorithm>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	
	string trash;
	getline(cin, trash);
	
	int found;
	string input;
	int iLower, iUpper;
	string sLower, sUpper;
	int len;
	for(int i = 0; i < cases; i++) {
		found = 0;
		getline(cin, input);
		int pos = input.find(" ");
		sLower = input.substr(0, pos);
		sUpper = input.substr(pos+1);
		len = sLower.length();
		iLower = atoi(sLower.c_str());
		iUpper = atoi(sUpper.c_str());
		
		deque<int> search, duplicates;
		for(int j = iLower; j <= iUpper; j++) {
			search.clear();
			duplicates.clear();
			search.push_back(-1);
			duplicates.push_back(-1);
		
			stringstream i;
			i << j;
			string slook = i.str();
			if(slook.length() != len) continue;
			
			for(int k = 0; k < len; k++) {
				char tmp = slook[0];
				slook.erase(slook.begin());
				slook.push_back(tmp);
				if(slook[0] == '0') {
					continue;
				}
				
				int ilook = atoi(slook.c_str());
				if(j < iLower) continue;
				if(j > iUpper) continue;
				
				deque<int>::iterator iterSearch = find(search.begin(), search.end(), j);
				
				if(j > ilook) {
				if(iterSearch == search.end()) {
					search.push_front(j);
				} else {
					deque<int>::iterator iterDuplicates = find(duplicates.begin(), duplicates.end(), j);
					if(iterDuplicates == duplicates.end()) {
						duplicates.push_front(j);
						found++;
					} else {
						continue;
					}
				}
				}
				
				iterSearch = find(search.begin(), search.end(), ilook);
				
				if(iterSearch == search.end()) {
					search.push_front(ilook);
				} else {
					deque<int>::iterator iterDuplicates = find(duplicates.begin(), duplicates.end(), ilook);
					if(iterDuplicates == duplicates.end()) {
						duplicates.push_front(ilook);
						found++;
					} else {
						continue;
					}
				}
				
				
				
				
			}
		}
	
		cout << "Case #" << i << ": " << found << endl;
	}

	return 0;
}
