
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

//TopCoder defines
#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define dbg(e) cout<<(#e)<<" : "<<e<<endl
#define REP(i,n) for(int i=0;i<(n);i++)
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define pb  push_back
#define mp make_pair

//Extras
#define SI(x) scanf("%d", &x)
#define SLL(x) scanf("%lld", &x)
#define SD(x) scanf("%lf", &x)

typedef long long LL;

void main2() {
    string str;
    char ref[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    getline(cin, str);
    REP(i,sz(str)) if(str[i] != ' ') str[i] = ref[str[i]-'a'];
    cout << str << endl;
}

int main() {
    int test; SI(test); getchar(); REP(tt,test) {
        printf("Case #%d: ", tt+1);
        main2();
    }
}
