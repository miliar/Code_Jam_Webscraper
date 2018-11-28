#include <iostream>
#include <cstring>
#include <map>
#define MAX 150
using namespace std;
string str,strtmp;
map <string,int> mp;
int next(int j){
    int k = j + 1;
    while (k < str.length() && str[k] != '/') k++;
    return k - j;
}
int main(){
    int t,cas,m,n,len,i,j,nj,ans;
    freopen("A-large.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    cin >> t;
    for (int cas = 1; cas <= t; cas++){
        mp.clear();
        cin >> m >> n;
        ans = 0;
        for (i = 1; i <= m; i++){
            cin >> str;
            strtmp = "";
            for (j = 0; j < str.length(); j += nj){
                nj = next(j);
                strtmp += str.substr(j,nj);
                mp[strtmp] = i;
            }
        }
        for (i = 1; i <= n; i++){
            cin >> str;
            strtmp = "";
            for (j = 0; j < str.length(); j += nj){
                nj = next(j);
                strtmp += str.substr(j,nj);
                if (!mp[strtmp]){
                    ans++;
                    mp[strtmp] = i;
                }
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
