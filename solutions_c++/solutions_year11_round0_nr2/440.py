#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

struct ElementList {
    int combinenum;
    char combine[64][3];
    int opposednum;
    char opposed[64][2];
    vector <char> list;
    void init() {
        int i;
        cin >> combinenum;
        assert(combinenum <= 64);
        for (i = 0; i < combinenum; i++) {
            cin >> combine[i][0];
            cin >> combine[i][1];
            cin >> combine[i][2];
        }
        cin >> opposednum;
        assert(opposednum <= 64);
        for (i = 0; i < opposednum; i++) {
            cin >> opposed[i][0];
            cin >> opposed[i][1];
        }
        list.clear();
    }
    void push(char e) {
        // try to combine
        if (!list.empty()) {
            int last = list.size() - 1;
            for (int i = 0; i < combinenum; i++) {
                if (combine[i][0] == e && combine[i][1] == list[last]) {
                    list[last] = combine[i][2]; // combine
                    return;
                }
                if (combine[i][1] == e && combine[i][0] == list[last]) {
                    list[last] = combine[i][2]; // combine
                    return;
                }
            }
        }

        // if combine, function returns and do not check
        // check opposed
        if (!list.empty()) {
            for (int i = 0; i < opposednum; i++) {
                char oe; //opposedelement
                if (opposed[i][0] == e) {
                    oe = opposed[i][1];
                } else if (opposed[i][1] == e) {
                    oe = opposed[i][0];
                } else {
                    continue;
                }

                for (int j = 0; j < list.size(); j++) {
                    if (list[j] == oe) {
                        list.clear();
                        return;
                    }
                }
            }
        }

        // if opposed, function returns
        list.push_back(e);
    }
    void output() {
        cout << '[';
        for (int i = 0; i < list.size(); i++) {
            if (i != 0) {
                cout << ", ";
            }
            cout << list[i];
        }
        cout << ']';
    }
};

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    ElementList l;
    int seqnum;
    char e;

    for (coden = 1; coden <= t; coden++)
    {
        l.init(); // init from cin
        cin >> seqnum;
        for (int i = 0; i < seqnum; i++) {
            cin >> e;
            l.push(e);
        }

        // output result
        cout << "Case #" << coden << ": ";
        l.output();
        cout << endl;
    }
    return 0;
}

