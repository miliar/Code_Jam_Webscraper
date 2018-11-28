#include<iostream>
#include<cstdio>
#include<string>
#include<conio.h>

using namespace std;

#define min(a,b) (a<b?a:b)
#define max(a,b) (a<b?b:a)
#define Size(x) (int)x.size()
#define FORI(i,n) for(int i = 0; i < n; i++)
#define FORB(i,be,en) for(int i = be; i <= en; i++)

int T,n,l,h;
int a[101];

int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    FORI(t,T) {
        printf("Case #%d: ",t+1);
        scanf("%d%d%d",&n,&l,&h);
        FORI(i,n) scanf("%d",&a[i]);
        int ans = -1;
        FORB(i,l,h) {
            bool flag = 1;
            FORI(j,n)
            if (a[j] % i != 0 && i % a[j] != 0) {
                flag = 0;
                break;
            }
            if (flag) {
                ans = i;
                break;
            }
        }
        if (ans > 0) printf("%d",ans);
        else printf("NO");
        if (t < T-1) printf("\n");
    }
    fclose(stdin);
    return 0;
}
