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
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

vector<pip> a;

int main(){
    int T; cin >> T;
    for (int _ = 0; _ < T; _++){
        int n; cin >> n;
        {
            string s;
            int q;
            a.clear();
            for (int i = 0; i < n; i++){
                cin >> s >> q;
                if (s[0] == 'O') a.push_back(pip(0,q));
                else a.push_back(pip(1,q));
            }
        }
        a.push_back(pip(0,100));
        a.push_back(pip(1,100));
        int p[2] = {1,1};
        int res = 0;
        for (int i = 0; i < n; i++){
            int t = a[i].first;
            int x = a[i].second;
            int q = -1;
            for (int j = i+1; ; j++) if (a[j].first != t){
                q = a[j].second;
                break;
            }
            for (;p[t] != x;){
                if (p[t] > x) p[t]--;
                else if (p[t] < x) p[t]++;
                else assert(0);
                if (p[t^1] > q)p[t^1]--;
                else if (p[t^1] < q) p[t^1]++;
                res++;
            }
            if (p[t^1] > q)p[t^1]--;
            else if (p[t^1] < q) p[t^1]++;
            res++;
        }
        printf("Case #%d: %d\n",_+1,res);
    }
    return 0;
}

