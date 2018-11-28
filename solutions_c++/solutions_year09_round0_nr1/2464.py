#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

#define sz(a) (int)a.size()
#define all(a) a.begin(),a.end()
#define pb push_back
#define mp(a, b) insert(make_pair(a,b))

using namespace std;

int main(){
    int l,d,n;
    cin >> l >> d >> n;
    vector<string> v;
    for(;d--;){
        string tmp;
        cin >> tmp;
        v.pb(tmp);
    }
    
    for(int c=0;c<n;++c){
        vector<string> s;
        string tmp;
        cin >> tmp;
        bool flag = false;
        string str="";
        for(string::iterator i=tmp.begin(); i!=tmp.end(); ++i){
            if(*i == '('){
                flag = true;
                if(str!="")s.pb(str);
                str="";
            }else if(*i == ')'){
                flag = false;
                if(str!="")s.pb(str);
                str="";
            }else if(!flag){
                str += *i;
                if(str!="")s.pb(str);
                str="";
            }else{
                str += *i;
            }
        }
        s.pb(str);

        int ans=0;
        for(int i=0;i<sz(v);++i){
            int cnt=0;
            for(int j=0;j<sz(v[i]);++j){
                //cout << s[j]<<" from "<<v[i][j]  << endl;
                if(find(all(s[j]), v[i][j]) != s[j].end()){
                    ++cnt;
                }else break;
            }
            if(cnt == l)++ans;
        }
        cout << "Case #"<<c+1<<": "  <<ans  << endl;
    }
    return 0;
}
