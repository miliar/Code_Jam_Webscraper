#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

int find_run(int cur, int ns, const vector<int> &qs) {
    vector<bool> flags;
    flags.assign(ns, false);
    int fcnt=ns;
    vector<int>::const_iterator it=qs.begin()+cur; 
    for ( ; it<qs.end(); it++) {
        int q=*it;
        if (!flags[q]) {
            fcnt--;
            flags[q] = true;
        }
        if (fcnt==0) break;
    }
    return it-qs.begin();
}

main() {
    int nc;
    cin >> nc;
    for (int ic=0; ic<nc; ic++) {
        int ns;
        cin >> ns;
        string dummy;
        getline(cin, dummy);
        vector<string> ses;
        for (int is=0; is<ns; is++) {
            string se;
            getline(cin, se);
            ses.push_back(se);
        }
        int nq;
        cin >> nq;
        getline(cin, dummy);
        vector<int> qs;
        for (int iq=0; iq<nq; iq++) {
            string se;
            getline(cin, se);
            vector<string>::iterator it = find(ses.begin(), ses.end(), se);
            int ise = it-ses.begin();
            qs.push_back(ise);
        }
        int cur = 0;
        int cnt = 0;
        while (cur < qs.size()) {
            cur = find_run(cur, ses.size(), qs);
            // cout << cur << endl;
            cnt++;
        }
        if (cnt==0) cnt = 1;
        cout << "Case #" << ic+1 << ": " << cnt-1 << endl;
    }
}
