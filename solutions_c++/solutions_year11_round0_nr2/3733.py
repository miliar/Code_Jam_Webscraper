#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int T;
    int C,D,N;
    int p;
    string base;

    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        map<string,char> c;
        map<char,char> d;
        string t;

        cin >> C;
        for(int i=0;i<C;i++) { cin >> t;
            c[t.substr(0,2)] = t[2];
            swap(t[0],t[1]);
            c[t.substr(0,2)] = t[2];
        }
        cin >> D;
        for(int i=0;i<D;i++) { cin >> t;
            d[t[0]] = t[1];
            d[t[1]] = t[0];
        }
        cin >> N >> base;

        map<string,char>::iterator it;
        map<char, char>::iterator it2;

        string ret = base.substr(0,1);
        int len = 1;
        string ss;
        for(int i=1;i<N;i++) {
            ret += base[i];
            len++;
            if(len<2) continue;
            ss = ret.substr(len-2);
            it = c.find(ss);
            if(it != c.end()) {
                ret = ret.substr(0,len-2) + it->second;
                len--;
            } else {
                it2 = d.find(base[i]);
                if(it2 != d.end()) {
                    if(ret.find(it2->second) != string::npos) {
                        ret.clear();
                        len = 0;
                    }
                }
            }
        }

        base = ret;
        printf("Case #%d: [", tc);
        for(int i=0;i<base.size();i++) {
            printf("%c", base[i]);
            if(i < base.size()-1) printf(", ");
        }
        printf("]\n");
    }

    return 0;
}
