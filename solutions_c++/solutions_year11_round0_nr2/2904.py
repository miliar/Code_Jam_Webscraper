#include <cstdio>
#include <vector>
using namespace std;

vector <pair<int,char> > like[30];
vector <int> hate[30];
char unos[103],niz[103];

void solve (int test){
     int d,n,c;
     scanf ("%d",&c);
     for (int i=0;i<c;++i){
         scanf ("%s",unos);
         like[unos[0]-'A'].push_back(make_pair(unos[1]-'A',unos[2]));
         like[unos[1]-'A'].push_back(make_pair(unos[0]-'A',unos[2]));
     }
     scanf ("%d",&d);
     for (int i=0;i<d;++i){
         scanf ("%s",unos);
         hate[unos[0]-'A'].push_back(unos[1]-'A');
         hate[unos[1]-'A'].push_back(unos[0]-'A');
     }
     scanf ("%d%s",&n,unos);
     int poz=0;
     for (int i=0;i<n;++i){
         niz[poz++]=unos[i];
         abc:;
         if (poz<=1){
            continue;
         }
         for (int j=0;j<like[niz[poz-1]-'A'].size();++j){
             if (like[niz[poz-1]-'A'][j].first==niz[poz-2]-'A'){
                niz[poz-2]=like[niz[poz-1]-'A'][j].second;
                --poz;
                goto abc;
             }
         }
         for (int j=0;j<poz-1;++j){
             for (int k=0;k<hate[niz[j]-'A'].size();++k){
                 if (hate[niz[j]-'A'][k]==niz[poz-1]-'A'){
                    poz=0;
                    goto abc;
                 }
             }
         }
     }
     for (int i=0;i<30;++i){
         hate[i].clear();
         like[i].clear();
     }
     printf ("Case #%d: [",test);
     for (int i=0;i<poz;++i){
         if (i==poz-1) printf ("%c",niz[i]); else printf ("%c, ",niz[i]);
     }
     printf ("]\n");
     return;
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        solve(i+1);
    }
    return 0;
}
