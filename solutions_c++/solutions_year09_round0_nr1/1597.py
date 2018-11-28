#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int l, d, n;
    cin >> l >> d >> n;

    vector<string> vs;
    for(int i=0;i<d;i++) {
        string s;
        cin >> s;
        vs.push_back(s);
    }
    
    for(int cnt=1;cnt<=n;cnt++) {
        string s;
        cin >> s;
        vector<string> vs2(l);
        int idx = 0;
        bool paren = false;
        for(int i=0;i<s.size();i++) {
            if(s[i] == '(') {
                paren = true;
            }
            else if(s[i] == ')') {
                idx++;
                paren = false;
            }
            else {
                if(paren) {
                    vs2[idx] += s[i];
                }
                else {
                    vs2[idx] += s[i];
                    idx++;
                }
            }
        }
        int ans = 0;
        for(int i=0;i<d;i++) {
            bool match = true;
            for(int j=0;j<l;j++) {
                if(vs2[j].find(vs[i][j]) == vs2[j].npos) {
                    match = false;
                    break;
                }
            }
            if(match)
                ans++;
        }
        cout << "Case #" << cnt << ": " << ans << endl;
    }
    
    return 0;
}
