#include <iostream>
#include <string>
#include <memory.h>
using namespace std;

char map[256][256];
bool op[256][256];

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        memset(map,0,sizeof(map));
        memset(op,0,sizeof(op));
        int C,D,N;
        cin>>C;
        for(int i=0;i<C;i++) {
            string s;
            cin>>s;
            map[s[0]][s[1]] = s[2];
            map[s[1]][s[0]] = s[2];
        }
        cin>>D;
        for(int i=0;i<D;i++) {
            string s;
            cin>>s;
            op[s[1]][s[0]] = op[s[0]][s[1]] = true;
        }
        cin>>N;
        string q, o="";
        cin>>q;
        for(int i=0;i<N;i++) {
            cerr<<" ... processing "<<i<<endl;
            bool mapped = false;
            if(o=="") o=q[i];
            else {
                char c = o[o.length()-1];
                if(map[c][q[i]]>0) {
                    o[o.length()-1] = map[c][q[i]];
                    mapped = true;
                } else {
                    o = o+q[i];
                }
            }
            if(!mapped && o.length()>1) {
                char last = q[i];
                for(int j=0;j<o.length()-1;j++) {
                    if(op[o[j]][last]) {
                        o="";
                        break;
                    }
                }
            }
        }

        cout<<"Case #"<<ci<<": [";
        for(int i=0;i<o.length();i++) {
            cout<<o[i];
            if(i!=o.length()-1) cout<<", ";
        }
        cout<<"]"<<endl;
    }

    return 0;
}

