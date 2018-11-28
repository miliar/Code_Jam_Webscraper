#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int l,d,n;
int ans;
vector<string> v;
bool h[20][30];
    
void insert(string &s,int &d){
    for (int i=0 ;i<s.length(); ++i) h[d][s[i]-'a'] = true;
    ++d;
}
    
int main(){
   // freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    string s;
    cin>>l>>d>>n; 
    v.clear();
    for (int i=0 ;i<d ;++i){
        cin>>s;
        v.push_back(s);
    }    
    for (int i=1 ;i<=n ;++i){
        cin>>s;
        memset(h,0,sizeof(h));
        printf("Case #%d: ",i);
        string t = "";
        int cnt = 0;
        int d = 0;
        for (int j=0 ;j<s.length(); ++j){
            if (s[j] == '('){
                ++cnt;
                if (t != "") {
                    insert(t,d);
                    t = "";
                }    
            }    
            else if (s[j] == ')'){
                --cnt;
                if (t != ""){
                    insert(t,d);
                    t = "";
                }    
            }    
            else {
                t += s[j];
                if (!cnt ){
                    insert(t,d);
                    t = "";
                }    
            }    
        }    
        ans = 0;
        for (int j=0 ;j<v.size(); ++j){
            bool f = true;
            for (int k=0 ;k<v[j].size(); ++k) if(!h[k][v[j][k]-'a']){
                f = false;
                break;
            }
            if (f) ++ans;    
        }    
        printf("%d\n",ans);
    }    
    return 0;
}    
