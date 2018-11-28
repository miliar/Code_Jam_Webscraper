#include <cstdlib>
#include <climits>
#include <sstream>
#include <string>
#include <iostream>
#include <cstdio>

// STL
#include <algorithm>
#include <vector>
#include <map> // contains multimap
#include <set> // contains multiset
#include <queue> // contains priority_queue
#include <deque>
#include <list>
#include <stack>


using namespace std;


void solve(int k) {
    list<char> lst;
    list<char>::iterator itlst;
    multimap<char,char> opposed;
    multimap<char,char>::iterator itt;
    pair<multimap<char,char>::iterator,multimap<char,char>::iterator> rg;
    map<string,char> combine;
    map<string,char>::const_iterator it, end;
    char a[2], b, c;
    bool boo;

    for (int i = 0; i < k; ++i) {
        cin >> a[0] >> a[1] >> b;
        string str(a, 2);
        combine[str] = b;
        c = a[0];
        a[0] = a[1];
        a[1] = c;
        string str2(a, 2);
        combine[str2] = b;
    }
    end = combine.end();

    cin >> k;
    for (int i = 0; i < k; ++i) {
        cin >> a[0] >> a[1];
        opposed.insert(pair<char,char>(a[0], a[1]));
        opposed.insert(pair<char,char>(a[1], a[0]));
    }

    cin >> k;
    a[1] = 0;
    for (int i = 0; i < k; ++i) {
        cin >> a[0];
        // Combine
        string str(a, 2);
        if ((it = combine.find(str)) != end) {
            if (!lst.empty()) lst.pop_back();
            lst.push_back(it->second);
            a[1] = it->second;
            continue;
        }
        
        // Oppose
        rg = opposed.equal_range(a[0]);
        boo = false;
        for (itt=rg.first; itt!=rg.second; ++itt) {
            if (find(lst.begin(), lst.end(), itt->second) != lst.end()) {
                lst.clear();
                boo = true;
                a[1] = 0;
                break;
            }
        }

        if (!boo) {
            lst.push_back(a[0]);
            a[1] = a[0];        
        }
    }

    int size = lst.size() - 1;
    for (itlst = lst.begin(); size > 0; ++itlst) {
        cout << *itlst << ", ";
        --size;
    }
    if (itlst != lst.end()) cout << *itlst;
}


int main() {
    int numcase, k, l;

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    cin >> numcase;
    for (int i = 0; i < numcase; ++i) {
        cin >> k;
        cout << "Case #" << i + 1 << ": [";
        solve(k);
        cout << "]" << endl;
    }

    return 0;
}
