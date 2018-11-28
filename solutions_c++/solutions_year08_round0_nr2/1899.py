#include <algorithm>
#include <cstdio>
using namespace std;

struct arr{
    int t1,t2,type;
    bool used;
}train[205];
inline bool cmp(const arr&,const arr&);
int tot,addt,nl,nr,h1,h2,m1,m2;
char ch;

int main(){
    scanf("%d",&tot);
    for (int cases=0;cases<tot;++cases){
        scanf("%d%d%d",&addt,&nl,&nr);
        for (int i=0;i<nl;++i){
            scanf("%d%c%d%d%c%d",&h1,&ch,&m1,&h2,&ch,&m2);
            train[i].t1=h1*60+m1;
            train[i].t2=h2*60+m2;
            train[i].used=false;
            train[i].type=0;
        }
        for (int i=0;i<nr;++i){
            scanf("%d%c%d%d%c%d",&h1,&ch,&m1,&h2,&ch,&m2);
            train[nl+i].t1=h1*60+m1;
            train[nl+i].t2=h2*60+m2;
            train[nl+i].used=false;
            train[nl+i].type=1;
        }
        sort(train,train+nl+nr,cmp);
        int ansl=0,ansr=0;
        for (int i=0;i<nl+nr;++i){
            if (train[i].used) continue;
            if (train[i].type==0) ++ansl;
            else ++ansr;
            int cur=i;
            for (int j=cur+1;j<nl+nr;++j){
                if (train[j].used) continue;
                if (train[j].type==train[cur].type) continue;
                if (train[j].t1<train[cur].t2+addt) continue;
                train[j].used=true;
                cur=j;
            }
        }
        printf("Case #%d: %d %d\n",cases+1,ansl,ansr);    
    }
    return 0;
}

inline bool cmp(const arr &a,const arr &b){
    if (a.t1<b.t1) return true;
    if (a.t1>a.t1) return false;
    return a.t2<b.t2;
}
