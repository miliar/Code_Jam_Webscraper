#include <string>
#include <iostream>
using namespace std;
char c[200][200];
bool d[200][200];
int main() {
    int T;
    cin>>T;
    for (int TT=1;TT<=T;TT++) {
        for(char x='A';x<='Z';x++)for(char y='A';y<='Z';y++)
            c[x][y]=0,d[x][y]=false;
        int n;
        string s;
        cin>>n;
        for(;n>0;n--) {
            cin>>s;
            c[s[0]][s[1]]=s[2];
            c[s[1]][s[0]]=s[2];
        }
        cin>>n;
        for(;n>0;n--) {
            cin>>s;
            d[s[0]][s[1]]=true;
            d[s[1]][s[0]]=true;
        }
        cin>>n;
        cin>>s; 
        string ans="";
        for(int i=0;i<s.size();i++) {
            if (ans.empty()) ans=ans+(s[i]);
            else {
                char x=c[ans[ans.size()-1]][s[i]];
                if (x>0) ans[ans.size()-1]=x;
                else {
                    ans=ans+(s[i]);
                    for (int j=0;j+1<ans.size();j++)
                        if (d[ans[j]][s[i]]) ans="";
                }
            }
        }
        cout<<"Case #"<<TT<<": [";
        for(int i=0;i<ans.size();i++) {
            if (i>0) cout<<", ";
            cout<<ans[i];
        }
        cout<<"]"<<endl;
    }
    return 0;
}
