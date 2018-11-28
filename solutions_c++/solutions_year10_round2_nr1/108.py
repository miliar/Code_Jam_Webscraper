#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

#define REP(i, n) for(int (i)=0; (i)<(n); ++(i))

#define INF 10000000

char buf[1000];

int pref(string got, string want){
    got += "/";
    want += "/";
    
    int i = 0;
    while( got[i] == want[i] ){
        i++;
        if ( i >= want.size() || i >= got.size() ) break;
    }
    
    
    int c = 0;
    
    if ( i == want.size() && want[i-1] == got[i-1] ) return 0;
    
    if ( want[i] == '/' ) i--;
    
    //else {
    while( i < want.size() ){
        if ( want[i] == '/' ) c++;
        i++;
    }
    
    
    //}
    //cout << "chcemy: " << want << " mamy " << got << " ruchow " << c << endl;
    
    
    return c;
}

int testcase(){
    vector<string> V;
    
    V.push_back("/");
    
    int n, m; scanf("%d%d", &n, &m);
    REP(i, n){
        scanf("%s", buf);
        V.push_back( buf );
    }
    
    int r = 0;
    REP(i, m){
        scanf("%s", buf);
        string s = buf;
        //cout << "zlecenie " << s << endl;
        int q = INF;
        
        REP(j, V.size()) q = min(q, pref(V[j], s));
        
        V.push_back( s );
        r += q;
    }
    return r;
}

int main(){
int z; scanf("%d", &z);
REP(i, z) {
    printf("Case #%d: %d\n",  i+1, testcase());
}
return 0;
}
