#include <iostream>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <cctype>
#include <set>
#include <cmath>
#include <climits>
#include <sstream>
#include <fstream>
#include <list>
#include <functional>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define SZ size()
#define pp push_back

typedef long long LL;
typedef vector <int> vi;
typedef vector <double> vd;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair<int,int> pii;
typedef vector <LL> vll;

char dAlpha[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main() {
    freopen("dashboard.in","r",stdin);
    freopen("dashboard.out","w",stdout);
    int n,m;
    char s[1000];
    string res = "";
    gets(s);
    n = atoi(s);
    for(int i=0;i<n;i++) {
            res = "";
            gets(s);
            m = strlen(s);
            for(int j=0;j<m;j++) {
                    if(s[j] == ' ') res+=" ";
                    else res+=dAlpha[s[j]-'a'];
            }
            printf("Case #%d: %s\n",i+1,res.c_str());
    }
    return 0;
}
