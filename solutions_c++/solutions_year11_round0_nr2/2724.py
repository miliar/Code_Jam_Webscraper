#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>


using namespace std;

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define repd(i,n,m) for(int i=n;i<(int)(m);i++)
#define repvi(v,i) for(vector<int>::iterator i = v.begin(); i < v.end();i++)
#define repvs(v,i) for(vector<string>::iterator i = v.begin(); i < v.end();i++)

int main() {
	freopen("b.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int cases, C, D, N;
	string temp, t;
	cin >> cases;
	getline(cin, temp);
	repd(nn, 1, cases+1) {
		cout << "Case #" << nn << ": [";
	
		getline(cin, temp);
		stringstream ss;
		ss << temp;

		ss >> C;

		vector<string> combine;
		rep(i, C) {
			ss >> t;
			combine.push_back(t);
		}

		ss >> D;
		vector<string> opposed;
		rep(i, D) {
			ss >> t;
			opposed.push_back(t);
		}

		ss >> N;
		string items;
		ss >> items;
		//end of input

		string elements(items.substr(0,1));
		int size = items.size();
		repd(i,1, size) {
			elements.push_back(items[i]);
			if (elements.size() > 1) {
				rep(j, C) {
					string com = combine[j].substr(0,2);
			if (elements.size() > 1) {
					if (elements.substr(elements.size()-2) == com) {
						elements = elements.substr(0, elements.size()-2);
						elements.push_back(combine[j][2]);
					} else {
						reverse(com.begin(), com.end());
						if (elements.substr(elements.size()-2) == com) {
							elements = elements.substr(0, elements.size()-2);
							elements.push_back(combine[j][2]);
						}
					}
					}
				//	
				}

				rep(j, D) {
					int pos1, pos2;
					pos1 = elements.find(opposed[j][0]);
					pos2 = elements.find(opposed[j][1]);
					if (pos1 != -1 && pos2 != -1) {
						elements.clear();
					}
				}
			}
		}
		rep(k, elements.size()) {
			if (k == 0)
				cout << elements[k];
			else
				cout << ", " << elements[k];
		}
		cout << "]" << endl;
	}	

	
	return 0;
}
