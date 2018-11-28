#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <list>

using namespace std;

class node : public map<char, node> {
};

int main() {
    node base;

    int L, D, N;
    cin >> L >> D >> N;

    // Read D words
    vector<string> words(D);
    for (int i = 0; i < D; i++) {
        cin >> words[i];
    }

    /*
    for (int i = 0; i < D; i++) {
        cout << words[i] << endl;
    }
    */

    // Build tree
    vector<string>::const_iterator it;
    for (it = words.begin(); it != words.end(); it++) {
        const string& word = *it;

        node* curr = &base;
        string::const_iterator sit;
        for (sit = word.begin(); sit != word.end(); sit++) {
            const char& c = *sit;
            curr = &((*curr)[c]);
        }
    }

    // Process N cases
    for (int i = 0; i < N; i++) {
        string tc;
        cin >> tc;

        list<node*> poss;
        poss.push_back(&base);

        string::const_iterator sit;
        bool grouping = false;
        list<node*> newposs;
        for (sit = tc.begin(); sit != tc.end(); sit++) {
            if (*sit == '(') {
                grouping = true;
                continue;
            } else if (*sit == ')') {
                grouping = false;
                poss = newposs;
                newposs.clear();
                continue;
            }
            const char& c = *sit;

            node::iterator mit;

            // Go through current possibilities
            list<node*>::iterator pit;
            node *curr;
            for (pit = poss.begin(); pit != poss.end(); pit++) {
                curr = *pit;
                mit = curr->find(c);
                if (mit != curr->end()) {
                    // Found; add to new possiblities
                    newposs.push_back(&(mit->second));
                }
            }

            if (!grouping) {
                poss = newposs;
                newposs.clear();
            }
        }

        cout << "Case #" << (i+1) << ": " << poss.size() << endl;
    }
}
