/*lcfr*/




#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cmath>


#define FO(i,s,e,p) for(int i=(s);i<int(e);i+=p)
#define FOD(i,s,e,p) for(int i=(s);i>int(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define ALL(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)

#define MEM(tab,fill) memset(tab,fill,sizeof(tab))

#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<sstream>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<bitset>
#include<map>
#include<cassert>

using namespace std;


#define pb push_back
#define ll long long
#define EPS 0.0000001
#define MOD 1000000009
#define mp make_pair
#define fi first
#define se second
#define inf ((1<<29)-1)
#define deb(a) cout<<#a<<' '<<a<<endl;
#define PI pair<ll,ll>
#define llu unsigned ll

#define AL(a) (a).begin(),(a).end()

string in[4];

bool get(char c){
    bool ki=0;
    FOR(i,0,4){
        bool z=1;
        FOR(j,0,4) z&=(in[i][j]==c || in[i][j]=='T');
        ki|=z;
    }

    FOR(j,0,4){
        bool z=1;
        FOR(i,0,4) z&=(in[i][j]==c || in[i][j]=='T');
        ki|=z;
    }
    bool z=1;
    FOR(i,0,4)
    FOR(j,0,4) if(i-j==0) z&=(in[i][j]==c || in[i][j]=='T');
    ki|=z;

    z=1;
    FOR(i,0,4)
    FOR(j,0,4) if(i+j==3) z&=(in[i][j]==c || in[i][j]=='T');
    ki|=z;
    return ki;

}

void solve(){
    FOR(i,0,4) cin>>in[i];
    int sm=0;
    FOR(i,0,4)FOR(j,0,4) sm+=(in[i][j]=='.');


    bool ki1=get('X');
    bool ki2=get('O');
    if(ki1 && ki2) assert(0);

    if(ki1) cout<<"X won";
    else if(ki2) cout<<"O won";
    else if(sm==0) cout<<"Draw";
    else cout<<"Game has not completed";
}


int main() {
    freopen("C:\\a","r",stdin);
    freopen("C:\\w","w",stdout);
    int t;cin>>t;
    FORE(i,1,t){
        printf("Case #%d: ",i);
        solve();
        cout<<endl;
    }


    return 0;
}
