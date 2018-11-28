#include <iostream>
#include <string>

using namespace std;

const int maxc=30, maxn=200;
char c[maxc][maxc];
bool d[maxc][maxc];

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    
    int n;
    cin >> n;
        
    for (int p=1; p<=n; ++p) {
        memset(c,0,sizeof(c));
        memset(d,0,sizeof(d));
        
        int k;
        string s;
        
        cin >> k;
        for (int i=0; i!=k; ++i) {
            cin >> s;
            c[s[0]-'A'][s[1]-'A']=c[s[1]-'A'][s[0]-'A']=s[2];
        }
        
        cin >> k;
        for (int i=0; i!=k; ++i) {
            cin >> s;
            d[s[0]-'A'][s[1]-'A']=d[s[1]-'A'][s[0]-'A']=true;
        }
        
        char ret[maxn]; int len=0;
        
        cin >> k;
        cin >> s;
        for (int i=0; i!=k; ++i) {
            if (len && c[ret[len]-'A'][s[i]-'A']) ret[len]=c[ret[len]-'A'][s[i]-'A'];
            else {
                 ret[++len]=s[i];
            
                 for (int j=1; j!=len; ++j)
                     if (d[ret[j]-'A'][s[i]-'A']) {
                        len=0;
                        break;
                     }                   
            }
        }
        
        cout << "Case #" << p << ": ";
        
        if (!len) cout << "[]";
        else {
             cout << "[" << ret[1];
             for (int i=2; i<=len; ++i)
                 cout << ", " << ret[i];
             cout << "]";
        }
        cout << endl;
    }
    
    return 0;
}
