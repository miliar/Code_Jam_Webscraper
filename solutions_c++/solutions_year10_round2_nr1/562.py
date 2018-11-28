#include <iostream>
#include <string>
using namespace std;
string p[110],c[110];
string tou(string& s){
    s.erase(0,1);
    if(s.size() == 0){
        return "";
    }
    string res;
    res = s.substr(0,s.find('/'));
    s.erase(0,s.find('/'));
    return res;
}
int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    cin >> T;
    for(int I = 1;I <= T;++I){
        cout << "Case #" << I << ": ";
        int n,m;
        cin >> n >> m;
        for(int i = 0;i < n;++i){
            cin >> p[i];
        }
        for(int i = 0;i < m;++i)
            cin >> c[i];
        string cur,tmp,tt;
        int j,ans(0);
        for(int i = 0;i < m;++i){
            tmp = c[i];
            cur = "";
            while(tmp != ""){
                tt = tou(tmp);
                if(tt == "") break;
                cur += "/";
                cur += tt;
//                cout << cur << endl;
                for(j = 0;j < i;++j)
                    if(c[j].find(cur) == 0) break;
//                cout << "@ " << j << endl;
                if(j < i) continue;
                for(j = 0;j < n;++j)
                    if(p[j].find(cur) == 0) break;
//                cout << "# " << j << endl;
                if(j == n) ++ans;
            }
        }
        cout << ans << endl;
    }
}
