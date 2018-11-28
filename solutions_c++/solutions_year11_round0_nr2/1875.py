#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int testcase = 1; testcase <= T; ++testcase) {
	int C, D, N;
	cin >> C;
	map<pair<char,char>,char> combines;
	for (int i = 0; i < C; ++i) {
	    char c1,c2,c3;
	    cin >> c1 >> c2 >> c3;
	    combines[make_pair(c1,c2)] = c3;
	    combines[make_pair(c2,c1)] = c3;
	}	
	cin >> D;
	set<pair<char,char> > opposed;
	for (int i = 0; i < D; ++i) {
	    char c1,c2;
	    cin >> c1 >> c2;
	    opposed.insert(make_pair(c1,c2));
	    opposed.insert(make_pair(c2,c1));
	}
	cin >> N;
	vector<char> chars;
	char c;
	cin >> c;
	chars.push_back(c);
	for (int i = 1; i < N; ++i) {
	    cin >> c;
	    if (chars.size() > 0) {
		if (combines.find(make_pair(c,chars[chars.size()-1])) != combines.end()) {
		    chars[chars.size()-1] = combines[make_pair(c,chars[chars.size()-1])];
		} else {
		    bool flag = false;
		    for (int j = 1; j <= chars.size(); ++j) {
			if (opposed.find(make_pair(chars[chars.size()-j],c)) != opposed.end()) {
			    chars.clear();
			    flag = true;
			    break;
			}
		    }
		    if (!flag) {
			chars.push_back(c);
		    }
		}
	    } else {
		chars.push_back(c);
	    }
	}
	
	cout << "Case #" << testcase << ": [";

	for (int i = 0; i < chars.size(); ++i) {
	    cout << chars[i];
	    if (i != chars.size()-1) {
		cout << ", ";
	    }
	}
	cout << "]" << endl;
    }

}
