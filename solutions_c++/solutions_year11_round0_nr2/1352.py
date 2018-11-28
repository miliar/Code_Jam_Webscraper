#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int ASCII_SIZE = 256;
typedef long long int LL;

ostream& operator<<(ostream& os, vector<char> v) {
    os << "[";
    for(int i = 0; i < v.size(); ++i) {
        cout << v[i];
        if(i != (v.size() - 1)) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase) {
        int c, d, n;
        vector<vector<char> > combinations(ASCII_SIZE, vector<char>(ASCII_SIZE, 0));
        cin >> c;
        for(int i = 0; i < c; ++i) {
            string tmp;
            cin >> tmp;
            combinations[tmp[0]][tmp[1]] = combinations[tmp[1]][tmp[0]] = tmp[2];
        }
        vector<vector<char> > opposing(ASCII_SIZE, vector<char>());
        cin >> d;
        for(int i = 0; i < d; ++i) {
            string tmp;;
            cin >> tmp;
            opposing[tmp[0]].push_back(tmp[1]);
            opposing[tmp[1]].push_back(tmp[0]);
        }
        vector<int> present(ASCII_SIZE, 0);
        cin >> n;
        string invocation;
        cin >> invocation;
        vector<char> elements;
        for(int i = 0; i < n; ++i) {
            char new_element = invocation[i];
            while(!elements.empty() && combinations[elements.back()][new_element] != 0) {
                new_element = combinations[elements.back()][new_element];
                --present[elements.back()];
                elements.pop_back();
            }
            bool conflict = false;
            FOREACH(it, opposing[new_element]) {
                if(present[*it] > 0) {
                    conflict = true;
                    break;
                }
            }
            if(conflict) {
                elements.clear();
                fill(present.begin(), present.end(), 0);
            } else {
                elements.push_back(new_element);
                ++present[new_element];
            }
        }
        cout << "Case #" << testCase << ": " << elements << endl;
    }
}
