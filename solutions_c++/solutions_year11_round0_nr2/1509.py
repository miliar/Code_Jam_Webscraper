// GCJ 2011, mrozik
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

int main() {
    
    int t, T; cin>>T;
    for (int t=1; t<=T; t++) {
        
        vector<string> cc;
        int C; cin>>C;
        while ( C --> 0) {
            string s; cin>>s; cc.push_back(s);
        }

        vector<string> dd;
        int D; cin>>D;
        while ( D --> 0) {
            string s; cin>>s; dd.push_back(s);
        }
        
        int n; string s, z;
        cin>>n>>s;
        for (int i=0; i<int(s.length()); i++) {
            
            if (z!="")
                for (int j=0; j<int(cc.size()); j++)
                    if (cc[j][0]==s[i] && cc[j][1]==*z.rbegin()
                        || cc[j][1]==s[i] && cc[j][0]==*z.rbegin()) {
                        *z.rbegin() = cc[j][2];
                        goto next;
                    }
                
            for (int j=0; j<int(dd.size()); j++)
                if (dd[j][0]==s[i] && z.find(dd[j][1])!=string::npos
                    || dd[j][1]==s[i] && z.find(dd[j][0])!=string::npos) {
                    z="";
                    goto next;
                }
            
            z+=s[i];
            
            next: {}
        }
        
        cout<<"Case #"<<t<<": [";
        for (int i=0; i<int(z.size()); i++) {
            cout<<z[i];
            if (i+1<int(z.size()))
                cout<<", ";
        }
        cout<<"]"<<endl;
        
    }
    
    return 0;
}
