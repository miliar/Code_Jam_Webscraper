#include <iostream>
#include <string>
#include <cstring>
#include <sstream>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;

template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}
inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}

bool c[2000001];

int main(){
    int t;
    cin >> t;

    for(int i=0;i<t;++i){
        int a,b;
        long long ret=0;

        memset(c, false, sizeof(c));
        cin >> a >> b;
        for(int j=a;j<=b;++j){
            string pat = toString(j),tmpstr;
            int cnt = 0, tmpi;
            while(1){
                tmpi = toInt(pat);
                if(a <= tmpi && tmpi <= b){
                    if(c[tmpi]) break;
                    c[tmpi] = true;
                    cnt++;
                }
                tmpstr = "";
                tmpstr += pat[pat.size()-1];
                tmpstr += pat.substr(0,pat.size()-1);
                pat = tmpstr;
            }
            ret += (long long)cnt * (cnt-1) / 2;
        }
        cout << "Case #" << i+1 << ": " << ret << endl;
    }
}
