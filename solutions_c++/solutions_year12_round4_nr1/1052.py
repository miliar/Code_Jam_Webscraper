#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

const double eps = 1e-11;

int n, D;
vector<int> d,l;

vector<vector<char> > memo;

//(a,b) estic a 'a' agafant la 'b'
char f(int a, int b) {
    int pos,x;
    
    char &ans = memo[(a<0?n:a)][b];
    if (ans>=0) return ans;
    
    if (a==-1) { //la tinc agafada
        pos = 0;
        x = min(l[0],d[0]);
    }
    else {
        pos = d[a];
        if (d[a]<=d[b]-l[b]) pos=d[b]-l[b];
        x = min(d[b]-d[a],l[b]);
    }
    if (pos+2*x>=D) return ans=1;//puc arribar al final
    for (int i=b+1;i<n and d[i]<=pos+x*2;++i) {
        if (f(b,i)) return ans=1;
    }
    return ans=0;
}

int main() {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cin >> n;
        d = l = vector<int> (n,0);
        for (int i = 0; i<n;++i) cin >> d[i] >> l[i];
        cin >> D;
        memo=vector<vector<char> >(n+1,vector<char>(n+1,-1));
        char r = f(-1,0);
        cout <<"Case #" << cas << ": ";
        if (r==0) cout <<"NO" << endl;
        else cout <<"YES" <<endl;
    }
}
