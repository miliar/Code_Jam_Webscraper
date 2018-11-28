#include<cstdio>

const int MAXN = 10000+10;
int n,alld;
int d[MAXN];
int l[MAXN];
int fr,ba;
int a[MAXN];
int b[MAXN];

bool check(){
    if (d[0]>l[0]){
        return false;
    }
    fr = 0;
    ba = 0;
    a[fr] = d[0];
    b[fr] = d[0];
    for (int i=1;i<n;++i){
        while (fr<=ba){
            if (a[fr]+b[fr]<d[i]){
                ++fr;
            } else {
                break;
            }
        }
        if (fr>ba){
            return false;
        }
        int ta = d[i];
        int tb = -1;
        for (int j=fr;j<=ba;++j){
            int tc = d[i]-a[j];
            if (l[i]<tc){
                tc = l[i];
            }
            if (tc>tb){
                tb = tc;
            }
        }
        if (tb!=-1&&ta+tb>a[ba]+b[ba]){
            ++ba;
            a[ba] = ta;
            b[ba] = tb;
        }
    }
    return a[ba]+b[ba]>=alld;
}

int main(){
    int noc;
    scanf("%d",&noc);
    for (int tnoc=1;tnoc<=noc;++tnoc){
        printf("Case #%d: ",tnoc);
        scanf("%d",&n);
        for (int i=0;i<n;++i){
            scanf("%d%d",&d[i],&l[i]);
        }
        scanf("%d",&alld);
        if (check()){
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
