#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int64,int64> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

int main(){
    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        //Eo(_);
        printf("Case #%d: ",_+1);
        int64 x,s,r,t,n; cin >> x >> s >> r >> t >> n;
        vector<pip> all;
        real basetime = real(x)/real(s);
        //Eo(basetime);
        int64 zzzz = x;
        for (int i = 0; i < n; i++){
            int64 st,fin,add;
            cin >> st >> fin >> add;
            if (st>=x)continue;
            if (fin>=x)fin=x;
            all.push_back(pip(add,fin-st));
            basetime -= real(fin-st)/real(s);
            basetime += real(fin-st)/real(s+add);
            zzzz -= (fin-st);
        }
        //Eo(basetime);
        all.push_back(pip(0,zzzz));
        sort(all.begin(),all.end());
        real used = 0;
        for (int i = 0; i < all.size(); i++){
//            Eo(all[i].first);Eo(all[i].second); Eo(basetime); Eo(used);
            real ll = 0;
            real rr = all[i].second;
            for (int cnt = 0; cnt < 10000; cnt++){
                real mm = (ll+rr)*0.5;
                real zz = mm/real(r+all[i].first);
                if (zz+used<=t){
                    ll = mm;
                } else {
                    rr = mm;
                }
            }
            //Eo(rr);
            basetime -= rr/real(s+all[i].first);
            basetime += rr/real(r+all[i].first);
            used += rr/real(r+all[i].first);
        }
        printf("%.12lf\n",double(basetime));
    }
	return 0;
}

