#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#include<fstream>

using namespace std;

#define sz size()
#define st stringstream
#define len length()
#define f(i,p,n) for(int i=p;i<n;i++)
#define sort(v) sort(v.begin(),v.end())
#define pb push_back

int main() {
    
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    
    int loop, m, n, l;
    string s, out, str;
    char ch;cin >> loop;
    map<char,char> oppose;
    map<string, char> combine;
    
    f(k,0,loop){
        
        s = "";
        cin >> m;
        f(i,0,m) {
            cin >> s;
            combine[s.substr(0,2)] = s[2];
            out = ""; out += s[1];out += s[0];combine[out] = s[2];
            s = "";
        }
        
        cin >> n;
        f(i,0,n) {
            cin >> s;
            oppose[s[0]] = s[1];
            s = "";
        }
        cin >> l;
        str = "";
        cin >> str;
        bool boo = false;
        out = "";
        int pos = 0;
        f(i,0,l) {
            
            //cout << pos << endl;
            ch = str[i];
            if (pos-1 >= 0) {
                s = "";
                s += str[i];s += out[pos-1];
                
                if (combine[s]) {
                    out = out.substr(0,pos-1);
                    out += combine[s];
                    boo = true;
                }
            }         
            if (!boo) {
                for (int j = 0; j < pos; j++) {
                    if (oppose[out[j]] == ch || oppose[ch] == out[j]) {
                        out = "";
                        boo = true;
                        pos = 0;
                        break;
                    }
                }
            }
            if (!boo) {
                out += ch;
                pos++;
            }    
            boo = false;
        }
        
        cout << "Case #" << k+1 <<": [";
        f(p,0,pos-1){
            
            cout << out[p] << ", ";
        }
        if (pos > 0) cout << out[pos-1];
        cout << "]" << endl ;
        combine.clear();
        oppose.clear();
    }
    return 0;
    //system("pause");
    //return 0;
}            
                
        
        
