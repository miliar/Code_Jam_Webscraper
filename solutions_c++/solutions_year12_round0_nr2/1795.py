#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>

using namespace std;

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

int t,s,p,n;

int main(){
    cin >> t;
    rep(cs,t){
        cin >> n >> s >> p;
        int ans = 0;
        rep(i,n){
            int x; cin >> x;
            if(x%3==0){
                if(x/3>=p) ++ans;
                else if(x>=3 && x/3+1>=p && s>0){
                    ++ans; --s;
                }
            }else if(x%3==1){
                if(x/3+1>=p) ++ans;
            }else{
                if(x/3+1>=p) ++ans;
                else if(x/3+2>=p && s>0){
                    ++ans; --s;
                }
            }
        }
        cout << "Case #" << cs+1 << ": " << ans << endl;
    }
    return 0;
}

