#include<cstdio>
#include<algorithm>

const int MAXN = 1000+10;

int l[MAXN];
int p[MAXN];
int odr[MAXN];

bool cmp(int i,int j){
    if (p[i]==p[j]){
        if (l[i]==l[j]){
            return i<j;
        } else {
            return l[i]<l[j];
        }
    } else {
        return p[i]<p[j];
    }
}

int n;

int main(){
    int noc;
    scanf("%d",&noc);
    for (int tnoc=1;tnoc<=noc;++tnoc){
        printf("Case #%d:",tnoc);
        scanf("%d",&n);
        for (int i=0;i<n;++i){
            scanf("%d",&l[i]);
        }
        for (int i=0;i<n;++i){
            scanf("%d",&p[i]);
            p[i] = 100-p[i];
            odr[i] = i;
        }
        std::sort(odr,odr+n,cmp);
        for (int i=0;i<n;++i){
            printf(" %d",odr[i]);
        }
        printf("\n");
    }
    return 0;
}
