#include <cstdio>
#include <iomanip>
#include <iostream>
using namespace std;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Tc,n,cnt,i,j,x;
    scanf("%d",&Tc);
    for (j=1;j<=Tc;j++){
        printf("Case #%d: ",j);
        scanf("%d",&n);
        cnt=0;
        for (i=1;i<=n;i++){
            scanf("%d",&x);
            if (x!=i) cnt++;
        }
        cout << fixed << setprecision(6) << (double)cnt << endl;
    }
}
