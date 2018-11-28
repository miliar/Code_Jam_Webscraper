#include<iostream>
using namespace std;
int n,k;
int main(){
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        scanf("%d%d", &n, &k);
        printf("Case #%d: ",i);
        int N=(1<<n)-1;
        int K=k&N;
        if (K==N) printf("ON\n");else
        printf("OFF\n");
    }
    return 0;
}
