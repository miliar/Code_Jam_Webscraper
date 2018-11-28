#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<int, double> pid;
typedef unsigned long long ull;
typedef vector<pii> vpii;
typedef vector<pid> vpid;

#define FO(i,s,e,p) for(int i=(s);i<(e);i+=p)
#define FOD(i,s,e,p) for(int i=(s);i>(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define REP(i,n) FOR(i,0,n)
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair

bool inline checkx(string* arr, char inp, char another){
    REP(i,4) {
        int count = 0;
        REP(j,4) if(arr[i][j] == inp || arr[i][j] == another) count++;
        if(count == 4) return true;
    }
    REP(j,4) {
        int count = 0;
        REP(i,4) if(arr[i][j] == inp || arr[i][j] == another) count++;
        if(count == 4) return true;
    }
    int count = 0;
    REP(i,4){
        if(arr[i][i] == inp || arr[i][i] == another) count++;
    }
    if (count == 4) return true;
    count = 0;
    REP(i,4){
        if(arr[i][3-i] == inp || arr[i][3-i] == another) count++;
    }
    if (count == 4) return true;
    return false;
}

int main() {
    int T, c =1;
    cin>>T;
    while(T--){
        string inp[4];
        REP(i,4) cin>>inp[i];
        if(checkx(inp, 'X', 'T')) {
                cout<<"Case #"<<c++<<": X won"<<endl;
                continue;
        }
        if(checkx(inp, 'O', 'T')) {
                cout<<"Case #"<<c++<<": O won"<<endl;
                continue;
        }
        bool incom = false;
        REP(i,4) REP(j,4) if(inp[i][j] == '.') incom |= true;
        if(incom) {
            cout<<"Case #"<<c++<<": Game has not completed"<<endl;
        } else {
            cout<<"Case #"<<c++<<": Draw"<<endl;
        }
    }
    return 0;
}

