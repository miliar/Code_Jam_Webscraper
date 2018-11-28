#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

struct train {
    int cnt, id;
    bool station; // 0 for A, 1 for B
    bool operator<(const train & t) const {
        if (cnt > t.cnt) return 1;
        else if (cnt < t.cnt) return 0;
        return id < t.id;
    }
};

int conv(string &s) {
    int ret = 0;
    ret += (s[0]-'0') * 10 * 60;
    ret += (s[1]-'0') * 60;
    ret += (s[3]-'0') * 10;
    ret += (s[4]-'0');
    return ret;
}

int main () {
    int N, i, j, cse=0;
    cin >> N;
    while (N--) {
        int na, nb, t;
        int num[2];
        fill(num, num+2, 0);
        cin >> t >> na >> nb;
        string line;
        getline(cin, line);
        set<pair<int, train> > se;
        for (i=0; i<na+nb; i++) {
            getline(cin, line);
            stringstream ss(line);
            string s1, s2;
            ss >> s1 >> s2;
            int t1=conv(s1), t2=conv(s2)+t;
            train tr1, tr2;
            tr1.id = i*2;
            tr1.cnt = -1;
            tr2.id = i*2+1;
            tr2.cnt = 1;
            if (i < na) {
                tr1.station = 0;
                tr2.station = 1;
            }
            else {
                tr1.station = 1;
                tr2.station = 0;
            }
            se.insert(make_pair(t1, tr1));
            se.insert(make_pair(t2, tr2));
        }
        int cnt[2];
        fill(cnt, cnt+2, 0);
        set<pair<int, train> >::iterator it;
        while (!se.empty()) {
            it = se.begin();
            int ti = it->first;
            train tr = it->second;
            cnt[tr.station] += tr.cnt;
            if (cnt[tr.station] < 0) {
                num[tr.station]++;
                cnt[tr.station] = 0;
            }
            se.erase(se.begin());
        }
        cout << "Case #" << ++cse << ": " << num[0] << " " << num[1] << endl;
    }

    return 0;
}
