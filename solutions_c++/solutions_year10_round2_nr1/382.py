#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;
int n,m,tot;
char pa[101][110], npa[101][110];
map<string,int> mp;
map<string,int>::iterator it;

int main() {
    int tt, cas=1;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out","w", stdout);
    scanf("%d",&tt);
    while(tt--) {
        scanf("%d%d",&n,&m);
        mp.clear();
        tot=0;
        for(int i=0; i<n; i++) {
            scanf("%s",pa[i]);
            string str(pa[i]);
            it=mp.find(str);
            if(it==mp.end()) {
                //cout<<str<<endl;
                mp[str]=tot++;
              for(int j=str.length()-1; j>=1; j--) {
                if(str[j]=='/') {
                    string sub=str.substr(0, j);
                    it=mp.find(sub);
                    if(it==mp.end()) {
                        mp[sub]=tot++;
                        //cout<<sub<<endl;
                    }
                    else break;
                }
              }
            }
        }
        int ans=0;
        for(int i=0; i<m; i++) {
            scanf("%s",npa[i]);
            string str(npa[i]);
            it=mp.find(str);
            if(it==mp.end()) {
                ans++;
                mp[str]=tot++;
            for(int j=str.length()-1; j>=1; j--) {
                if(str[j]=='/') {
                    string sub=str.substr(0, j);
                    it=mp.find(sub);
                    if(it==mp.end()) {
                        mp[sub]=tot++;
                        ans++;
                    }
                    else break;
                }
            }
          }
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    //system("pause");
    return 0;
}
