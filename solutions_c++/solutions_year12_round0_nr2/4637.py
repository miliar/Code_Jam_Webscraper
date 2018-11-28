#include <stdio.h>
#include <algorithm>
using namespace std;

int n,s,p;

int check(int x){
    int tmp = x%3;
    switch (tmp){
        case 0:
            if (x/3+1>=p && x/3<p && x/3+1<=30 && x/3-1>=0) return 0;
            else if (x/3>=p) return 1;
            else return -1;
            break;
        case 1:
            if (x/3+1>=p) return 1;
            else return -1;
            break;
        case 2:
            if (x/3+2>=p && x/3+1<p && x/3+2<=30) return 0;
            else if (x/3+1>=p) return 1;
            else return -1;
            break;
    }
}

int main(){
    int t,ans,c;
    int a[110];
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for (int k=1; k<=t; k++){
        ans = 0; c = 0;
        scanf("%d%d%d",&n,&s,&p);
        for (int i=0; i<n; i++){
            scanf("%d",&a[i]);
            int x = check(a[i]);
            if (x>0) ans++;
            if (x==0) c++;
        }
        ans += min(s,c);
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
