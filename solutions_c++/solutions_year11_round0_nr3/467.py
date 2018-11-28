#include <cstdio>
#include <cstring>
const int N=1005;
int n;
int a[N];

void init(){
    scanf("%d",&n);
    for (int i=1;i<=n;i++) scanf("%d",&a[i]);
}

void solve(){
    int ret=0;
    for (int i=1;i<=n;i++) ret^=a[i];
    if (ret!=0) printf("NO\n");
    else{
        ret=0;
        int Min=0x7FFFFFFF;
        for (int i=1;i<=n;i++){
          if (a[i]<Min) Min=a[i];
          ret+=a[i];
        }
        ret-=Min;
        printf("%d\n",ret);
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Tc;
    scanf("%d",&Tc);
    for (int i=1;i<=Tc;i++){
        printf("Case #%d: ",i);
        init();
        solve();
    }
}
