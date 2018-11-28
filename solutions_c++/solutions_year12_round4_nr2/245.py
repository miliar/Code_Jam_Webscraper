#include<cstdio>
#include<algorithm>

const int MAXN = 1000+10;

int n,w,l;
int r[MAXN];
int odr[MAXN];
int posx[MAXN];
int posy[MAXN];

bool cmp(int ta,int tb){
    return r[ta]>r[tb];
}

void solve(int ww,int ll){
    int start = -r[odr[0]];
    int fr = 0;
    int ba;
    while (fr<n){
        start += r[odr[fr]];
        ba = fr;
        int tot = 0;
        while (true){
            ++ba;
            if (ba>=n){
                break;
            }
            if (r[odr[ba]]+r[odr[ba-1]]+tot>ww){
                break;
            } else {
                tot += r[odr[ba]]+r[odr[ba-1]];
            }
        }
        tot = 0;
        for (int i=fr;i<ba;++i){
            if (i!=fr){
                tot += r[odr[i]];
            }
            posx[odr[i]] = start;
            posy[odr[i]] = tot;
            tot += r[odr[i]];
        }
        start += r[odr[fr]];
        fr = ba;
    }
}

int main(){
    int noc;
    scanf("%d",&noc);
    for (int tnoc=1;tnoc<=noc;++tnoc){
        printf("Case #%d:",tnoc);
        scanf("%d%d%d",&n,&w,&l);
        for (int i=0;i<n;++i){
            scanf("%d",&r[i]);
            odr[i] = i;
        }
        std::sort(odr,odr+n,cmp);
        solve(std::min(w,l),std::max(w,l));
        if (w>l){
            for (int i=0;i<n;++i){
                printf(" %d.0 %d.0",posx[i],posy[i]);
            }
        } else {
            for (int i=0;i<n;++i){
                printf(" %d.0 %d.0",posy[i],posx[i]);
            }
        }
        printf("\n");
    }
    return 0;
}
