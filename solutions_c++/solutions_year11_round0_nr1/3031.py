#include <cstdio>
#include <utility>
#include <cstdlib>
using namespace std;

pair <int,int> a[103];
int prvi[103],drugi[103];
char unos[142];

int solve (){
    int n,kol1=0,kol2=0,t;
    scanf ("%d",&n);
    for (int i=0;i<n;++i){
        scanf ("%s%d",unos,&t);
        if (unos[0]=='O'){
           prvi[kol1++]=t;
           a[i]=make_pair(t,0);
        }
        if (unos[0]=='B'){
           drugi[kol2++]=t;
           a[i]=make_pair(t,1);
        }
    }
    int poz1=1,poz2=1,raz=0,niz1=0,niz2=0;
    int rj=0;
    for (int i=0;i<n;++i){
        if (a[i].second==0){
             raz=abs(poz1-prvi[niz1++])+1;
             poz1=prvi[niz1-1];
             rj+=raz;
             //if (niz2>=kol2) continue;
             if (poz2<drugi[niz2]){
                poz2+=raz; 
                if (poz2>drugi[niz2]) poz2=drugi[niz2];
             } 
             if (poz2>drugi[niz2]){
                poz2-=raz; 
                if (poz2<drugi[niz2]) poz2=drugi[niz2];
             } 
        }
        if (a[i].second==1){
             raz=abs(poz2-drugi[niz2++])+1;
             poz2=drugi[niz2-1];
             rj+=raz;
             //if (niz1>=kol1) continue;
             if (poz1<prvi[niz1]){
                poz1+=raz; 
                if (poz1>prvi[niz1]) poz1=prvi[niz1];
             } 
             if (poz1>prvi[niz1]){
                poz1-=raz; 
                if (poz1<prvi[niz1]) poz1=prvi[niz1];
             } 
        }
        //printf ("%d %d %d %d %d\n",rj,poz1,poz2,raz,rj);
    }
    return rj;
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        printf ("Case #%d: %d\n",i+1,solve());
    }
    return 0;
}
