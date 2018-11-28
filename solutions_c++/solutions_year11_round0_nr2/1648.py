#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;t++) {
        int C;
        cin>>C;
        map<pair<char, char>, char> M;
        for (int i=0;i<C;i++) {
            string s;
            cin>>s;
            M[make_pair(s[0],s[1])] = s[2];
            M[make_pair(s[1],s[0])] = s[2];
        }
        int D;
        cin>>D;
        set<pair<char, char> > R;
        for (int i=0;i<D;i++) {
            string s;
            cin>>s;
            R.insert(make_pair(s[0], s[1]));
            R.insert(make_pair(s[1], s[0]));
        }
        int N;
        cin>>N;
        string cur;
        {
            string s;
            cin>>s;
            for (int j=0;j<s.size();j++) {
                char c = s[j];
                cur += c;
                int n = cur.size() - 1;
                while (cur.size() >= 2 && M.count(make_pair(cur[n], cur[n-1])) > 0) {
                    char x = M[make_pair(cur[n], cur[n-1])];
                    cur.resize(cur.size() - 2);
                    cur += x;
                }
                for (int k=0;k<cur.size();k++) for (int m=k+1;m<cur.size();m++) {
                    if (R.count(make_pair(cur[k], cur[m])) > 0) {
                        cur = "";
                        break;
                    }
                }
            }

        }
        cout << "Case #" << t << ": [";
        for (int j=0;j<cur.size();j++) {
            if (j != 0) cout << ", ";
            cout << cur[j];
        }
        cout << "]" << endl;
    }
}
