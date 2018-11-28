#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

bool visited[1001];
vector<int> edge[1001];

bool solve(int arg){
    int n = edge[arg].size();
    bool ret = false;
    if(visited[arg]) return true;
    visited[arg] = true;

    for(int i=0;i<n;i++){
        ret = solve(edge[arg][i]);
        if(ret) break;
    }
    return ret;
}

int main(){
    int t;
    cin >> t;

    for(int x=1;x<=t;x++){
        int n,tmp,e;
        bool ret;
        cin >> n;
        for(int i=0;i<1001;i++){
            edge[i].clear();
        }

        for(int i=0;i<n;i++){
            cin >> tmp;
            for(int j=0;j<tmp;j++){
                cin >> e;
                edge[i].push_back(e-1);
            }
        }

        for(int i=0;i<n;i++){
            memset(visited,false, sizeof(visited));
            ret = solve(i);
            if(ret) break;
        }

        printf("Case #%d: %s\n", x, ret?"Yes":"No");
    }
}
