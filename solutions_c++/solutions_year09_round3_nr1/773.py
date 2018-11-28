#include <iostream>
#include <set>
#include <string>
#include <map>
using namespace std;

string s;
int x[100];
long long ans;

long long getAns(long long  k){
    ans = 0;
    //cout<<k<<endl;
    for (int i=0 ;i<s.length(); ++i){
        ans = ans*k+x[i];
       // cout<<x[i];
    }   // cout<<endl;
    return 0;
}
    
int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int T;
    cin>>T;
    getline(cin,s);
    for (int I =1 ;I<= T; ++I){
        cout<<"Case #"<<I<<": ";
        getline(cin,s);
        int cnt = 0;
        set<char> ss;
        for (int i=0 ;i<s.length(); ++i){
            if (ss.find(s[i]) == ss.end()){
                ++cnt;
                ss.insert(s[i]);
            }    
        }    
        //++cnt;
        x[0] = 1;
        map<char,int> m;
        m[s[0]] = 1;
        int k = 0;
        for (int i=1 ;i<s.length(); ++i){
            int t;
            if (m.find(s[i]) == m.end()){
                if (k == 1) ++k;
                t = k++;
                m.insert(pair<char,int>(s[i],t));
            }    
            else t = m[s[i]];
            x[i] = t;
        }    
        //cout<<k<<endl;
        if (cnt == 1) cnt = 2;
        getAns(cnt);
        cout<<ans<<endl;
    }    
    return 0;
}    