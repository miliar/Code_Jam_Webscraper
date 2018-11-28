#include <string>
#include <vector>
#include <iostream>

using namespace std;

struct AD {
    AD(int t, bool a): time(t), arr(a) {}
    int time;
    bool arr;
    bool operator<(const AD &o) const {
        if (time < o.time) return true;
        if (time > o.time) return false;
        if (arr && !o.arr) return true;
        return false;
    }
};

int s2t(const string &st) {
    int k = st.find(':');
    int h = atoi(st.substr(0, k).c_str());
    int m = atoi(st.substr(k+1, st.length()-k-1).c_str());
    return h*60+m;
}

void fill_vec(vector<AD> &sta, vector<AD> &stb, int nt, int tt) {
    for (int i=0; i<nt; i++) {
        string st1, st2;
        cin >> st1 >> st2;
        int t1 = s2t(st1);
        sta.push_back(AD(t1, false));
        int t2 = s2t(st2);
        stb.push_back(AD(t2+tt, true));
    }
}

int trains(vector<AD> &st) {
    sort(st.begin(), st.end());
    int cum=0;
    int min=0;
    for (vector<AD>::iterator i=st.begin(); i<st.end(); i++) {
        AD &ad = *i;
        if( ad.arr ) {
            cum++;
        } else {
            cum--;
        }
        min <?= cum;
    }
    return -min;
}

main() {
    int nc;
    cin >> nc;
    for (int ic=0; ic<nc; ic++) {
        int tt;
        cin >> tt;
        int na, nb;
        cin >> na >> nb;
        vector<AD> sta;
        vector<AD> stb;
        fill_vec(sta, stb, na, tt);
        fill_vec(stb, sta, nb, tt);
        int tota = trains(sta);
        int totb = trains(stb);
        cout << "Case #" << ic+1 << ": " << tota << " " << totb << endl;
    }
}
