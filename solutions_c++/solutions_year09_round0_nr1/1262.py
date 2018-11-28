#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define rep(i,n) for (int i = 0; i < n; i++)

vector<string> dic;

int rec(string &q, string &cur, int pos)
{
    int i = pos;
    while (i < q.size()) {
        if (q[i] == '(') {
            string prev = cur;
            int ed = i+1;
            while (q[ed] != ')') ed++;
            int ans = 0;
            for (int j = i+1; j < ed; j++) {
                cur = prev + q[j];
                string cured = prev + (char)(q[j]+1);
                //cout << cur << ',' << cured << endl;
                vector<string>::iterator start = lower_bound(dic.begin(), dic.end(), cur);
                vector<string>::iterator end = lower_bound(dic.begin(), dic.end(), cured);
                if (start == end) continue; // cannot be found
                ans += rec(q, cur, ed+1);
            }
            return ans;
        } else {
            cur += q[i++];
        }
    }
    //cout << cur << endl;
    if (binary_search(dic.begin(), dic.end(), cur)) return 1;
    else return 0;
}

int main()
{
    int l, d, n;
    cin >> l >> d >> n;
    rep(i,d) {
        string word;
        cin >> word;
        dic.push_back(word);
    }
    sort(dic.begin(), dic.end());
    rep(i,n) {
        string q, cur;
        cin >> q;
        cout << "Case #" << i+1 << ": " << rec(q, cur, 0) << endl;
    }
}
