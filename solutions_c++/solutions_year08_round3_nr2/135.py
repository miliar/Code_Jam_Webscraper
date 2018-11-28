#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>
#include<numeric>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iterator>
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define CLEAR(t) memset((t), 0, sizeof(t))

#define sz size()
#define pb push_back
#define pf push_front

#define VI vector<int>
#define VS vector<string>
#define LL long long

#define add 1
#define substract 2

int sign[50];
string s;
LL total;

bool calculate() {
    LL num;
    LL tot = 0;
    num = 0;
    LL ten = 1;
    for(int i=s.sz-1; i>=0; i--) {
        num = num + ten*(s[i]-'0');
        if( !sign[i] ) { ten *= 10; continue; }
        else if( sign[i] == add ) tot += num, num = 0, ten = 1;
        else if( sign[i] == substract ) tot -= num, num = 0, ten = 1;
    }
    //cout <<"tot :"<<tot<<endl;
    //system("pause");
    if( tot < 0 ) tot *= -1;
    return (tot % 2 == 0 || tot % 3 == 0 || tot % 5 == 0 || tot % 7 == 0) ;
    
}

void solve( int x ) {
    if( x == s.sz ) {
        if( calculate() ) total++;
        return;
    }
    
    REP(i,3) {
        sign[x] = i;
        solve( x+1 );
    }
}

int main() {
    int n;
    
    freopen("b2.in","r",stdin);
    freopen("b2.out","w",stdout);
    
    cin >> n;
    REP(ncase, n ) {
        cin >> s;
        sign[0] = add;
        total = 0;
        solve( 1 );
        printf("Case #%d: %lld\n",ncase+1, total);
    }
    
    //system("pause");

    return 0;
}
