#include <iostream>
#include <map>
#include <vector>

using namespace std;

string v;
const string w = "welcome to code jam";

int cache[510][30];
const int MO = 10000;

int go(int vp, int wp) {
    if (w.size() == wp) return 1;
    if (v.size() == vp) return 0;

    int &ret = cache[vp][wp];
    if (ret >= 0) return ret;

    ret = go(vp + 1, wp);
    if (v[vp] == w[wp]) ret = (ret + go(vp + 1, wp + 1)) % MO;

    return ret;
}

int main() {

    int cases;
    cin >> cases;

    string line;
    getline(cin,line);

    for(int cs=0; cs<cases; cs++) {
        getline(cin,v);
        memset(cache,-1,sizeof(cache));

        printf("Case #%d: %04d\n", cs+1, go(0,0));
    }

}
