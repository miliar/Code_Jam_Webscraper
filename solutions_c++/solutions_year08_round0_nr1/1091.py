#include<iostream>
#include<string>
#include<map>
using namespace std;
const int MAX_N = 105;
const int MAX_M = 1005;
int mk[MAX_N];
int mark;
int n, m;
map<string, int> se_dict;
string se[MAX_N];
int query[MAX_M];
string aline;
int main() {
    memset(mk, 0, sizeof(mk));
    mark = 0;
    int T;
    cin >> T;
    int t_c;
    for (t_c = 1; t_c <= T; t_c++) {
        ++mark;
        cin >> n;
        getline(cin, aline);
        int se_c;
        se_dict.clear();
        for (se_c = 0; se_c < n; se_c++) {
            getline(cin, se[se_c]);
            se_dict[se[se_c]] = se_c;
        }
        cin >> m;
        getline(cin, aline);
        int query_c;        
        for (query_c = 0; query_c < m; query_c++) {
            string q;
            getline(cin, q);
            query[query_c] = se_dict[q];
            //cout << q << " : " << query[query_c] << endl;
        }
        int ans = 0;
        int idx;
        int cnt = 0;
        for (idx = 0; idx < m; idx++) {
            if (mk[query[idx]] != mark) {
                mk[query[idx]] = mark;
                cnt++;
                if (cnt == n) {
                    ans++;
                    cnt = 1;
                    mark++;
                    mk[query[idx]] = mark;
                }
            }
        }
        cout << "Case #" << t_c << ": " << ans << endl;
    }    
    
    return 0;
}
    
