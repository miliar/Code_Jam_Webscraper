#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i)
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i)
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i)
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std;
static const double EPS = 1e-9;
typedef long long ll;

class Tree {
  public:
    double weight;
    string feature;
    Tree *left, *right;

    Tree(double _w, string _s) : weight(_w), feature(_s), left(NULL), right(NULL) {}
    ~Tree() {
        if (left != NULL)
            delete left;
        if (right != NULL)
            delete right;
    }

    double getP(set<string> &w) {
        if (left == NULL && right == NULL)
            return weight;
        if (w.find(feature) != w.end()) {
            return left->getP(w)*weight;
        } else {
            return right->getP(w)*weight;
        }
    }
};

Tree *getTree(string input) {
    int deep = 0;
    bool isEnd = true;
    int start = -1;
    int end = -1;
    int nstart[2] = {-1, -1};
    int nend[2] = {-1, -1};
    int countS = 0;
    int countE = 0;

    REPV(input, i) {
        if (input[i] == '(') {
            if (deep == 0) {
                assert(start == -1);
                start = i;
            } else if (deep == 1) {
                assert(countS <= 1);
                nstart[countS++] = i;
                isEnd = false;
            }
            ++deep;
        } else if (input[i] == ')') {
            --deep;
            if (deep == 0) {
                assert(end == -1);
                end = i;
            } else if (deep == 1) {
                assert(countE <= 1);
                nend[countE++] = i;
            }
        }
    }
    assert(deep == 0);
//    cerr << input << " " << start << " " << end << endl;
    assert(start != -1 && end != -1);

    if (isEnd) {
        istringstream iss(input.substr(start+1, end-start-1));
        double weight;
        iss >> weight;
        return new Tree(weight, "");
    }

    assert(countS == 2 && countE == 2);
    
    istringstream iss(input.substr(start+1, nstart[0]-start-1));
    string feature;
    double weight;
    iss >> weight >> feature;
    Tree *p = new Tree(weight, feature);
    p->left = getTree(input.substr(nstart[0], nend[0]-nstart[0]+1));
    p->right = getTree(input.substr(nstart[1], nend[1]-nstart[1]+1));
    return p;
}

int main(void)
{
    int N;
    cin >> N;
    string buf;
    REP(caseID, N) {
        int L;
        cin >> L;
        getline(cin, buf); // remove \n
        string input;
        REP(i, L) {
            getline(cin, buf);
            while(!buf.empty() && buf[0] == ' ') buf.erase(buf.begin());
            input += buf;
        }

        Tree *root = getTree(input);

        cout << "Case #" << caseID+1 << ":" << endl;
        int A;
        cin >> A;
        REP(i, A) {
            string name;
            cin >> name;
            int n;
            cin >> n;
            set<string> fets;
            REP(i, n) {
                string fet;
                cin >> fet;
                fets.insert(fet);
            }
            printf("%.7lf\n", root->getP(fets));
        }

        delete root;
    }
    
    return 0;
}
