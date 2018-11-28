#include <iostream>
#include <set>
#include <map>
#include <string>
#include <stack>

using namespace std;

//class ctree : public map<string, ctree> {
//};

class ctree {
    public:
        ctree() : yes(NULL), no(NULL) {}
        double weight;
        string feature;
        ctree *yes;
        ctree *no;
};

ostream& operator<<(ostream& out, ctree& tree) {
    out << "(" << tree.weight;
    if (!tree.feature.empty()) {
        out << " " << tree.feature << endl;
    }
    if (tree.yes != NULL) {
        out << " " << *(tree.yes);
    }
    if (tree.no != NULL) {
        out << " " << *(tree.no);
    }
    out << ")" << endl;
}

enum eState {
    INIT,
    WEIGHT,
    POST_WEIGHT,
    FEATURE,
    POST_FEATURE,
    POST_CHILD1,
    POST_CHILD2
};

void doCase(int caseNum) {
    int L;
    cin >> L;

    // Eat the endl
    string tmp;
    getline(cin, tmp);
    
    ctree root;
    ctree *curr = &root;

    eState state = POST_FEATURE;
    int depth = 0;
    string weight;
    string feature;
    stack<ctree *> nodes;
    stack<eState> states;
    for (int i = 0; i < L; i++) {
        string line;
        getline(cin, line);

        if (state == WEIGHT) {
            state = POST_WEIGHT;
            curr->weight = atof(weight.c_str());
        }
        else if (state == FEATURE){
            state = POST_FEATURE;
                    curr->feature = feature;
        }

        string::const_iterator sit;
        for (sit = line.begin(); sit != line.end(); sit++) {
            const char& c = *sit;
            if (c == '(') {
                if (state != POST_FEATURE && state != POST_CHILD1) {
                    cerr << "Unexpected ( in state " << state << endl;
                    exit(1);
                }
                weight.erase();
                feature.erase();
                ctree *child = new ctree;
                if (state == POST_FEATURE) {
                    curr->yes = child;
                } else {
                    curr->no = child;
                }
                nodes.push(curr);
                states.push(state);
                curr = child;
                state = INIT;
                depth++;
            } else if (c == ' ' || c == '\t') {
                if (state == WEIGHT) {
                    state = POST_WEIGHT;
                    // parse weight
//                    cout << "***** weight is " << weight << endl;
                    curr->weight = atof(weight.c_str());
                } else if (state == FEATURE) {
                    state = POST_FEATURE;
                    // save feature
                    curr->feature = feature;
//                } else if (state != INIT) {
//                    cerr << "Unexpected state " << state << " for whitespace" << endl;
//                    exit(1);
                }
            } else if ((c >= '0' && c <= '9') || c == '.') {
                if (state == INIT) state = WEIGHT;
                if (state == WEIGHT) {
                    weight.push_back(c);
                } else {
                    cerr << "Unexpected digit" << endl;
                    exit(1);
                }
            } else if (c >= 'a' && c <= 'z') {
                if (state == POST_WEIGHT) {
                    state = FEATURE;
                }
                if (state == FEATURE) {
                    feature.push_back(c);
                } else {
                    cerr << "Unexpected letter " << c << endl;
                    exit(1);
                }
            } else if (c == ')') {
                if (state == WEIGHT || state == POST_WEIGHT || state == POST_CHILD2) {
                    if (state == WEIGHT) {
                        // parse weight
//                        cout << "***** weight is " << weight << endl;
                        curr->weight = atof(weight.c_str());
                    }
                    curr = nodes.top();
                    nodes.pop();
                    state = states.top();
                    states.pop();
                    depth--;
                    if (state == POST_CHILD1) state = POST_CHILD2;
                    else if (state == POST_FEATURE) state = POST_CHILD1;
                } else {
                    cerr << "Unexpected )" << endl;
                    exit(1);
                }
            }
        }

//        cout << "C" << caseNum << "L" << (i+1) << ": " << line << endl;
    }

//    cout << *(root.yes) << endl;
    ctree* base = root.yes;

    int A;
    cin >> A;

    // Eat the endl
    getline(cin, tmp);

    cout << "Case #" << caseNum << ":" << endl;
    for (int i = 0; i < A; i++) {
        string animal;
        int n;
        cin >> animal >> n;
        double prob = 1.0;

        set<string> ctics;

        for (int j = 0; j < n; j++) {
            string ctic;
            cin >> ctic;

            ctics.insert(ctic);
        }

        // Navigate the tree
        ctree* now = base;
        while (true) {
            prob *= now->weight;
            string& ct = now->feature;
            if (!(ct.empty())) {
                if (ctics.count(ct) > 0) {
                    now = now->yes;
                } else {
                    now = now->no;
                }
            } else {
                break;
            }
        }
        printf("%0.7f\n", prob);

//        string line;
//        getline(cin, line);

//        cout << "C" << caseNum << "A" << (i+1) << ": " << line << endl;
    }
}

int main() {
    int N;

    cin >> N;

    for (int i = 0; i < N; i++) {
        doCase(i+1);
    }
}
