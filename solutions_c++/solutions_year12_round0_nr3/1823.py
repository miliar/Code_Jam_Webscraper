#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map>
#include<set>

using namespace std;

typedef pair<int,int> pint;

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

int pw[10];

int main(){
    int tt; cin >> tt;
    pw[0]=1;
    rep(i,8) pw[i+1]=pw[i]*10;
    rep(cs,tt){
        int a,b; cin >> a >> b;
        int keta=0,aa=a;
        while(aa){aa/=10; ++keta;}
        set<pint> ans;
        repp(n, a, b-1){
//            cerr<< "n: "<<n << endl;
            rep(i, keta-1){
                int m = n/pw[i+1] + n%pw[i+1]*pw[keta-i-1];
//                cerr << m << endl;
                if(m >= pw[keta-1] && n < m && m <= b) ans.insert(make_pair(n,m));
            }
        }
        cout << "Case #" << cs+1 << ": " << ans.size() << endl;
    }
    return 0;
}

