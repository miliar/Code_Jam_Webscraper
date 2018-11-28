#include <cstdio>
#include <cstring>
#include <set>
#include <string>

using namespace std;

int main() {
    int nt, ct;
    char cs[1000];
    
    scanf(" %d" , &nt);
    for (ct=1; ct<=nt; ct++) {
        set <string> dr;
        int n,m;
        
        scanf(" %d %d",&n,&m);
        
        for (int i=0; i<n; i++) {
            scanf(" %s",cs);
            string s = cs;
            
            for (int j=1; j<s.size(); j++)
                if (s[j]=='/') {
                    dr.insert(s.substr(0, j));
                }
            dr.insert(s);
        }
        
        int res=0;
        
        for (int i=0; i<m; i++) {
            scanf(" %s",cs);
            string s = cs;
            
            for (int j=1; j<s.size(); j++)
                if (s[j]=='/') {
                    string s2=s.substr(0, j);
                    if (dr.find(s2)==dr.end())
                        res++;
                    dr.insert(s2);
                }
            if (dr.find(s)==dr.end()) res++;
            dr.insert(s);
        }
        
        printf("Case #%d: %d\n",ct, res);
    }
    
    return 0;
}

