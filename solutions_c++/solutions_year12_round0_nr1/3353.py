#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <sstream>

using namespace std;

int main()
{
    char m[26];
    m[int('y'-'a')]='a';
    m[int('e'-'a')]='o';
    m[int('q'-'a')]='z';
    m[int('z'-'a')]='q';
        
    string test[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi","rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","de kr kd eoya kw aej tysr re ujdr lkgc jv"};    
    string op[3] = {"our language is impossible to understand","there are twenty six factorial possibilities","so it is okay if you want to just give up"};
    
    for(int i=0; i<3; i++) {    
        string a=test[i];
        string b=op[i];
        for(int j=0; j<a.size(); j++) {
            if(a[j]>='a' && a[j]<='z') {
                m[int(a[j]-'a')]=b[j];
            }
        }
    }
  
    string cases;
    stringstream str;
    getline(cin, cases);
    str << cases;
    
    int T;
    str >> T;
    string g,s;
    for(int t=1; t<=T; t++) {        
        getline(cin, g);
        s=g;
        for(int i=0; i<g.size(); i++) {
            if(g[i]>='a' && g[i]<='z') {
                s[i]=m[int(g[i]-'a')];
            }
        }
        cout << "Case #" << t << ": " << s << endl;
    }
            
    return 0;
}
