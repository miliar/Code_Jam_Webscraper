#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

struct P {
    int h;
    int m;
};

vector<P> inia;
vector<P> inib;
vector<P> fima;
vector<P> fimb;

int cmp(P a, P b) {
    return a.h*60 + a.m < b.h*60 + b.m;
}

int menor(P a , P b, int t) {
    int k1,k2;
    k1 = a.h*60 + a.m + t;
    k2 = b.h*60 + b.m;
    if(k1 <= k2) return 1;
    return 0;
}

int main() {
    int n,t,na,nb,j,resa,resb,inst=1;
    P x;
    char lixo;
    scanf("%d" , &n);
    for(int i=0;i<n;i++) {
        scanf("%d" , &t);
        scanf("%d %d" , &na, &nb);
        resa = resb = 0;

        inia.clear();
        inib.clear();
        fima.clear();
        fimb.clear();

        for(j=0;j<na;j++) {
            scanf("%d%c%d" , &x.h, &lixo, &x.m);
            inia.push_back(x);
            scanf("%d%c%d" , &x.h, &lixo, &x.m);
            fima.push_back(x);
        }
        for(j=0;j<nb;j++) {
            scanf("%d%c%d" , &x.h, &lixo, &x.m);
            inib.push_back(x);
            scanf("%d%c%d" , &x.h, &lixo, &x.m);
            fimb.push_back(x);
        }

        sort(inia.begin(), inia.end(), cmp);
        sort(inib.begin(), inib.end(), cmp);
        sort(fima.begin(), fima.end(), cmp);
        sort(fimb.begin(), fimb.end(), cmp);


        int tob = 0;
        int toa = 0;

        for(j=0;j<na;j++) {
            if(tob < (int) fimb.size()) {
                if(menor(fimb[tob], inia[j], t)) {
                    //fimb.erase(fimb.begin());
                    tob++;
                }
                else resa++;
            }
            else resa++;
        }

        for(j=0;j<nb;j++) {
            if(toa < (int) fima.size()) {
                if(menor(fima[toa], inib[j], t)) {
                    //fima.erase(fima.begin());
                    toa++;
                }
                else resb++;
            }
            else resb++;
        }

        printf("Case #%d: %d %d\n" , inst++, resa, resb);    

    }
    return 0;
}
