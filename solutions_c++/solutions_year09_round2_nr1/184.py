#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef double ret_t;

class Node {
public:
    Node():feature(""), left(0), right(0) {};
    double p;
    string feature;
    Node * left;
    Node * right;
};

class Solver {
public:
    string s;
    int p;
    Node * tree;
    void makeTree(Node ** at) {
        *at = new Node;
        for (; s[p] != '('; ++p)
            ;
        ++p;

        while (s[p] == ' ')
            ++p;

        string prob;
        while (s[p] == '.' || (s[p] >= '0' && s[p] <= '9'))
            prob += s[p++];
        {
            stringstream A(prob);
            A >> (*at)->p;
        }

        while (s[p] == ' ')
            ++p;
        
        //cerr<<'('<<((*at)->p);
        if (s[p] == ')') {
            //cerr<<')'<<endl;
            ++p;
            return;
        }
        
        while (s[p] >= 'a' && s[p] <= 'z')
            (*at)->feature += s[p++];

        //cerr<<endl;
        makeTree(&((*at)->left));
        makeTree(&((*at)->right));
        //cerr<<')'<<endl;

        for (; s[p] != ')'; ++p)
            ;
        ++p;
    }
    ret_t solve(vector<string> feat) {
        Node * at(tree);
        double ret = 1;
        while (true) {
            ret *= at->p;
            if (at->feature.size() == 0)
                break;
            vector<string>::iterator lo = lower_bound(feat.begin(), feat.end(),
                                                      at->feature);
            if (lo != feat.end() && at->feature == *lo)
                at = at->left;
            else
                at = at->right;
        }
        return ret;
	}
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        int L;
        {
            getline(cin, s);
            stringstream A(s);
            A >> L;
        }
        string treedesc;
        for (int i = 0; i < L; ++i) {
            getline(cin, s);
            treedesc += s;
            treedesc += " ";
        }
        solver.s = treedesc;
        solver.p = 0;
        solver.makeTree(&(solver.tree));
        cout << "Case #" << no << ":\n"; // multi-line
        int nA;
        {
            getline(cin, s);
            stringstream A(s);
            A >> nA;
        }
        for (int i = 0; i < nA; ++i) {
            getline(cin, s);
            stringstream A(s);
            string nm;
            int no;
            A >> nm >> no;
            vector<string> feat(no);
            for (int j = 0; j < no; ++j) A >> feat[j];
            sort(feat.begin(), feat.end());
            cout << fixed << setprecision(7) << solver.solve(feat) << endl; // float
        }

        // *** give output ***
        //cout << "Case #" << no << ": " << ret << endl; // one line
    }
    return 0;
}
