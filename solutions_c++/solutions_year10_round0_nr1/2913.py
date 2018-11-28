#include <iostream>
using namespace std;
int main(){
    freopen("A.txt","r",stdin);
    freopen("A.out","w",stdout);
    int N,n,k;
    cin >> N;
    for(int i = 0;i < N;++i){
        cin >> n >> k;
        n = 1 << n;
        if(k % n == n-1) printf("Case #%d: ON\n",i+1);
        else printf("Case #%d: OFF\n",i+1);
    }
}
