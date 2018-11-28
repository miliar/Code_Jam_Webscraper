#include <iostream>
#include <string>
using namespace std;
bool vi[20][26];
string a[5010];
bool ok(string s){
    for(int i = 0;i < s.size();++i)
        if(!vi[i][s[i] - 'a']) return 0;
    return 1;
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int l,d,n;
    cin >> l >> d >> n;
    for(int i = 0;i < d;++i) cin >> a[i];
    for(int i = 1;i <= n;++i){
        string s;
        int k(0);
        memset(vi,0,sizeof(vi));
        cin >> s;
        for(int j = 0;j < l;++j){
            if(s[k] == '('){
                ++k;
                while(s[k] >= 'a' && s[k] <= 'z'){
                    vi[j][s[k]-'a'] = 1;
                    ++k;
                }
            }
            else vi[j][s[k]-'a'] = 1;
            ++k;
        }
        int ans(0);
        for(int j = 0;j < d;++j)
            if(ok(a[j])) ++ans;
        cout << "Case #" << i << ": " << ans << endl;
    }
}
