# include <iostream>
# include <vector>
# include <cmath>
# include <string>
# include <set>
# include <algorithm>
# include <cstring>
# include <queue>
# include <stack>
# include <map>
using namespace std;

string str, a;
bool vis[30];
int m, tt;

bool eleccion(int j, string res, bool mayor)
{
    bool w[10];
    memset(w, 0, sizeof w);
    if (j==m) {
        if (res.compare(str)>0) {
            cout<<"Case #"<<tt<<": "<<res<<endl;
            return true;
        }
        return false;
    }
    int i, n=a.size();
    char c;
    bool cierto;
    for (i=0; i<n; i++) {
        cierto=mayor;
        if ((mayor || a[i]>=str[j]) && !vis[i] && !w[a[i]-'0']) {
            vis[i]=true;
            w[a[i]-'0']=true;
            res.push_back(a[i]);
            if (a[i]>str[j]) {
                cierto=true;
            }
            if (eleccion(j+1, res, cierto)) {
                return true;
            }
            res.erase(res.size()-1, 1);
            vis[i]=false;
        }
    }
    return false;
}

int main()
{
    int t, i, n;
    scanf("%d", &t);
    tt=1;
    char temp;
    while(t--) {
        memset(vis, 0, sizeof vis);
        cin>>str;
        m=str.size();
        a=str;
        sort(a.begin(), a.end());
        if (!eleccion(0, "", false)) {
            a.insert(1, "0");
            sort(a.begin(), a.end());
            n=a.size();
            if (a[0]=='0') {
                for (i=0; i<n; i++) {
                    if (a[i]>'0') {
                        temp=a[0];
                        a[0]=a[i];
                        a[i]=temp;
                        break;
                    }
                }
            }
            cout<<"Case #"<<tt<<": "<<a<<endl;
        }
        tt++;
    }
    return 0;
}
