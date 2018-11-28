#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int getFirst(vector<pair<char, int> >& v, char c) {
    int i = 0;
    for (vector<pair<char, int> >::iterator it=v.begin(); it!=v.end(); ++it,++i) {
        if (it->first==c)
            return i;
    }
    return -1;
}

int main() {
    int t;
    cin>>t;

    for (int i=0; i<t; i++) {
        vector<pair<char,int> > inp;
        int s = 0;
        cin>>s;
        for (int j=0; j<s; j++) {
            char tmp1; int tmp2;
            cin>>tmp1>>tmp2;
            inp.push_back(make_pair(tmp1,tmp2));
        }
        //cout<<"done!\n";
        int curO=1, curB=1,steps=0;
        while (inp.size()) {
            int pO = getFirst(inp, 'O');
            int pB = getFirst(inp, 'B');
            bool eraseInp = false;
            stringstream sO, sB;
            //move O towards the instruction.
            if (pO>=0) {
                if (curO < inp[pO].second) {
                    curO++;
                    sO<<"Move to button "<<curO;
                } else if (curO > inp[pO].second) {
                    curO--;
                    sO<<"Move to button "<<curO;
                } else {
                    if (inp[0].first=='O') {
                        sO<<"Push button "<<curO;
                        eraseInp = true;
                    } else {
                       sO<<"Stay at button "<<curO;
                    }
                }
            }
            if (pB>=0) {
                if (curB < inp[pB].second) {
                    curB++;
                    sB<<"Move to button "<<curB;
                } else if (curB > inp[pB].second) {
                    curB--;
                    sB<<"Move to button "<<curB;
                } else {
                    if (inp[0].first=='B') {
                        sB<<"Push button "<<curB;
                        eraseInp = true;
                    } else {
                        sB<<"Stay at button "<<curB;
                    }
                }
            }
            if (eraseInp)
                inp.erase(inp.begin());
            steps++;
            //cout<<steps<<"# "<<sO.str()<<" | "<<sB.str()<<endl;
        }

        cout<<"Case #"<<i+1<<": "<<steps<<endl;
    }
    return 0;
}
