#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

pair<char,char> sortpair(pair<char,char> in) {
    if(in.first < in.second)
        return in;
    else
        return make_pair(in.second, in.first);
}

void printQ(vector<char> q) {
    cout << "[";
    for(int i=0;i+1<q.size();i++) {
        cout << q[i] << ", ";
    }
    if(q.size())
        cout << q[q.size()-1];
    cout << "]" << endl;
}

void solve(int i) {
    vector<char> ansQ;

    stringstream ss;
    string s;

    int C = 0;
    cin >> C;
    map<pair<char,char>, char> mC;
    while(C--) {
        cin >> s;
        mC[sortpair(make_pair(s[0], s[1]))] = s[2];
    }

    int D = 0;
    cin >> D;
    bool mD[256][256] = {0};
    while(D--) {
        cin >> s;
        mD[s[0]][s[1]] = true;
        mD[s[1]][s[0]] = true;
    }

    int N = 0;
    cin >> N;
    while(N--) {
        char c;
        cin >> c;
        ansQ.push_back(c);
        if(ansQ.size()>=2) {
            char a,b;
            a = ansQ[ansQ.size()-1];
            b = ansQ[ansQ.size()-2];
            map<pair<char,char>, char>::iterator iter = mC.find(sortpair(make_pair(a,b)));
            if(iter != mC.end()) {
                ansQ.pop_back();
                ansQ.pop_back();
                ansQ.push_back(mC[sortpair(make_pair(a,b))]);
            }
        }
        int size = ansQ.size();
        for(int i=0;i<size-1;i++) {
            for(int j=i+1;j<size;j++) {
                if(mD[ansQ[i]][ansQ[j]]) {
                    ansQ.clear();
                    i=j=size;
                }
            }
        }
    }

    cout << "Case #" << i << ": ";
    printQ(ansQ);
}

int main(int argc, void **argv) {
    int N;
    cin >> N;
    for(int i=0;i<N;i++) {
        solve(i+1);
    }
}

