#include<iostream>
using namespace std;

int T, a, b, len, mul;

int getLen(int a){
    if(a == 0) return 1;
    int cnt = 0;
    mul = 1;
    while(a != 0){
        a /= 10;
        mul *= 10;
        cnt++;
    }
    mul /= 10;
    return cnt;
}

int roate(int n){
    int last = n % 10;
    n  = n / 10 + last * mul;
    return n;
}

int solve(){
    int ans = 0;
    len = getLen(a);
    if(len == 1) return 0;
    for(int i = a; i <= b; i++){
        int m = i;
        for(int j = 1; j < len; j++){
            m = roate(m);
            if(m == i) break;
            if(m > i  && a <= m && m <= b) ans++;
        }
    }
    return ans;
    
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin>>T;
    for(int t = 1; t <= T; t++){
        cin>>a>>b;
        cout<<"Case #"<<t<<": "<<solve()<<endl;
    }
    return 0;
}