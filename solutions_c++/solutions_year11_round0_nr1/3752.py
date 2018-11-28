#include<iostream>
#include<vector>
#define pb push_back
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cse=1,t,i,j,n,tmp;
    char dum;

    scanf("%d",&t);
    while(t--) {
               vector<int> b,o,tot;
               int ctr=0,ptrb=1,ptro=1,nowo=0,nowb=0,nowtot=0,nextb=0,nexto=0;
               scanf("%d",&n);
               for (i=0; i<n; i++) {
                   scanf(" %c %d",&dum,&tmp);
                   if (dum=='B') {b.pb(tmp); tot.pb(tmp);}
                   else {o.pb(tmp); tot.pb(-tmp);}
                   }
               if (b.size()>0) nextb=b[nowb];
               if (o.size()>0) nexto=o[nowo];
               while(nowtot<tot.size()) {
                                        int lkh,lkh2,temp=tot[nowtot];
                                        //printf("ptro = %d ptrb = %d temp = %d nowtot = %d",ptro,ptrb,temp,nowtot);
                                        if (temp<0) {
                                                lkh=-temp-ptro;
                                                if (lkh<0) lkh*=-1;
                                                ctr+=lkh+1; //printf(" lkh = %d ",lkh);
                                                ptro=-temp; nowtot++; nowo++;
                                                if (nowo<o.size()) nexto=o[nowo];
                                                lkh2=nextb-ptrb;    
                                                int lk;
                                                if (lkh2<0) lk=-lkh2; else lk=lkh2;
                                                lk=min(lk,lkh+1);
                                                if (lkh2>0) ptrb+=lk; else ptrb-=lk;
                                                }
                                        else {
                                             lkh=temp-ptrb;
                                                if (lkh<0) lkh*=-1;
                                                ctr+=lkh+1; //printf(" lkh = %d ",lkh);
                                                ptrb=temp; nowtot++; nowb++;
                                                if (nowb<b.size()) nextb=b[nowb];
                                                lkh2=nexto-ptro;    
                                                int lk;
                                                if (lkh2<0) lk=-lkh2; else lk=lkh2;
                                                lk=min(lk,lkh+1);
                                                if (lkh2>0) ptro+=lk; else ptro-=lk;
                                                }
                                        //printf(" ctr = %d nextb = %d nexto = %d \n",ctr,nextb,nexto);
                                        }
               printf("Case #%d: %d\n",cse,ctr); cse++;
               }
    //system("pause");
}
