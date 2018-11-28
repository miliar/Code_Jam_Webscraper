#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdio.h>

using namespace std;

int main() {
    freopen("out.txt", "w", stdout);
    int cases, i;

    cin >> cases;
    for (int cas=1;cas<=cases;cas++) {
	vector<char> elements;
	vector<string> combine;
	vector<string> oppose;
	
	int c,d;
	string s;
	cin >> c;
	for (i=0;i<c;i++) {
	    cin >> s;
	    combine.push_back(s);
	}

	cin >> d;
	for (i=0;i<d;i++) {
	    cin >> s;
	    oppose.push_back(s);
	}

	int e;
       
	cin >> e >> s;
	elements.push_back(s[0]);
	for (i=1;i<e;i++) {
	    bool combined = false;
	    for (int j=0;j<combine.size();j++) {
		if (elements.size() <= 0)
		    break;

		int pos = combine[j].find(s[i]);

		if (pos < 0 || pos > 1) continue;
		else if (pos == 1) {
		    if (combine[j][0] == elements[elements.size()-1]) {//combine
			elements[elements.size()-1] = combine[j][2];
			combined = true;
			break;
		    }
		} else if (pos == 0) {
		    if (combine[j][1] == elements[elements.size()-1]) {//combine
			elements[elements.size()-1] = combine[j][2];
			combined = true;
			break;
		    }
		}
	    }
	    if (!combined) {
		elements.push_back(s[i]);
	    }

	    for (int j=0;j<oppose.size();j++) {
		if (oppose[j][0] == elements[elements.size() - 1]) {
		    for (int k=0;k<elements.size()-1;k++) {
			if (elements[k] == oppose[j][1]) {
			    elements.clear();
			    break;
			}
		    }
		} else if (oppose[j][1] == elements[elements.size() - 1]) {
		    for (int k=0;k<elements.size()-1;k++) {
			if (elements[k] == oppose[j][0]) {
			    elements.clear();
			    break;
			}
		    }
		}
	    }
	}

	cout << "Case #" << cas << ": [";
	for (i=0;i<elements.size();i++) {
	    if (i > 0)
		cout << ", ";
	    cout << elements[i];
	}
	cout << ']' << endl;
	
    }

    return 0;
}
