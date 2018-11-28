#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>
#include<utility>
#include<cstdio>
#include<cstdlib>
using namespace std;

int main(){
    int l,d,n;
    cin>>l>>d>>n;
    vector<string> v;
    string s;
    for(int i=0;i<d;i++){
        cin>>s;
        v.push_back(s);
    }
    
    for(int i=0;i<n;i++){
        int res=0;
        cin>>s;
        
        vector<int> vi(l,0);
        vector< vector<int> > vt(27,vi);        
        
        int pos=0;
        int ok=1;
        for(int j=0;j<s.length();j++){
            if( s[j]=='(' ) ok=0;
            if( s[j]!='(' && s[j]!=')' ){
                vt[ s[j]-'a' ][pos]=1;
            }
            if( s[j]==')' ){
                ok=1;
            }
            if(ok) pos++;
        }
      
        for(int k=0;k<d;k++){
            string st=v[k];
            int ok=1;
            for(int p=0;p<st.size();p++){
                if( vt[ st[p]-'a' ][p]== 0 ){
                    ok=0;
                    break;
                }
            }
            if(ok) res++;
        }
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    
}
