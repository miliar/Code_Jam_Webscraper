/*alien language*/
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int L,D,N;
	vector<string> dict;
	int nummatch=0;
	string temp;
	cin >> L >> D >> N;
	
	for (int i=0;i<=D;i++) {
		getline(cin,temp);
		if (i!=0) dict.push_back(temp);
	}
	// for (int i=0;i<D;i++) {
		// cout << dict[i] << endl;
	// }
	// cout << "*************\n";
	for (int i=0;i<N;i++) {
		cin >> temp;
		vector<string> filter, filter2;
		filter.clear();
		for (int j=0;j<dict.size();j++) {
			filter.push_back(dict[j]);
		}
		
		int idx=0,j=0;
		while (j<temp.length()) {
			// cout << "temp : " << temp << endl;

			// for (int k=0;k<filter.size();k++) {
				// cout << filter[k] << endl;
			// }
			// cout << "---------------\n";
			filter2.clear();
			if (temp[j]=='(') {
				j++;
				while (temp[j]!=')') {
					for (int k=0;k<filter.size();k++) {
						if (filter[k][idx] == temp[j])	filter2.push_back(filter[k]);
					}
					j++;
				}
			}
			else {
				for (int k=0;k<filter.size();k++) {
					if (filter[k][idx] == temp[j])	filter2.push_back(filter[k]);
				}
			}
			filter.clear();
			for (int k=0;k<filter2.size();k++) {
				filter.push_back(filter2[k]);
			}
			idx++;
			j++;
		}
		cout << "Case #" << i+1 << ": " << filter2.size() << endl;
	}
}
