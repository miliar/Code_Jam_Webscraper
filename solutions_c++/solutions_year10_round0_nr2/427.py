#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int t,n;
vector<int> dif,ans,now;
vector<vector<int> > bnum;

void pnt (vector<int> tp) {
     for (int k=tp.size()-1; k>=0; k--) printf("%d",tp[k]);
}

// 1=a<b, 0=a>b
bool cmpb (vector<int> a,vector<int> b) {
     if (a.size()!=b.size()) return a.size()<b.size();
     for (int i=b.size()-1; i>=0; i--)
         if (a[i]!=b[i]) return a[i]<b[i];
     return 0;
}

vector<int> subt (vector<int> a,vector<int> b) {
   vector<int> res;
   //pnt(a); printf(" - "); pnt(b); printf(" = ");
   for (int i=0; i<b.size(); i++) {
       if (a[i]<b[i]) { a[i]+=10; a[i+1]--; }
       res.push_back(a[i]-b[i]);
       }
   for (int i=b.size(); i<a.size(); i++) {
       if (a[i]<0) { a[i]+=10; a[i+1]--; }
       res.push_back(a[i]);
       }
   for (int i=res.size()-1; i>=1; i--) {
       if (res[i]==0) res.pop_back(); 
          else break;
       }
   //pnt(res); printf("\n");
   return res;
}

vector<int> mod (vector<int> a,vector<int> b) {
   vector<int> nb;
   while (cmpb(a,b)==0) {
      nb=b;
      while (cmpb(a,nb)==0) {
         nb.insert(nb.begin(),0);
         fflush(stdout);
         }
      nb.erase(nb.begin());
      while (cmpb(a,nb)==0) a=subt(a,nb);
      }
   
   return a;
}

vector<int> gcd (vector<int> a,vector<int> b) {
   if (cmpb(a,b)==1) swap(a,b);
   //pnt(a); printf(" mod "); pnt(b); printf("\n");
   vector<int> cmn=mod(a,b);
   if (cmn.size()==1 && cmn[0]==0) return b;
   return gcd(b,cmn);
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    for (int j=0; j<51; j++)
        bnum.push_back(dif);
    for (int i=0; i<t; i++) {
        scanf("%d",&n);
        for (int j=0; j<n; j++) {
            char strn[1000];
            bnum[j].clear();
            scanf("%s",strn);
            int len=strlen(strn);
            for (int k=len-1; k>=0; k--)
                bnum[j].push_back(strn[k]-'0');
            }
        int del=0;
        sort(bnum.begin(),bnum.begin()+n,cmpb);
        for (int j=0; j<n-1; j++)
            if (bnum[j]==bnum[j+1]) {
               bnum.erase(bnum.begin()+j); 
               j--; del++;
               }
        n-=del;
        if (n==1) {
           printf("Case #%d: 0\n",i+1);
           continue;
           }
        /*
        for (int j=0; j<n; j++) {
            pnt(bnum[j]);
            printf("\n");
            }
        */
        dif=subt(bnum[1],bnum[0]);
        for (int j=2; j<n; j++)
            dif=gcd(dif,subt(bnum[j],bnum[j-1]));
        now=mod(bnum[0],dif);
        //printf("dif: "); pnt(dif); printf("\n"); pnt(now); printf("\n");
        if (now[0]==0 && now.size()==1) {ans.resize(1); ans[0]=0;}
           else ans=subt(dif,now);
        //printf("cmp: %d\n",cmpb(bnum[0],bnum[1]));
        printf("Case #%d: ",i+1);
        pnt(ans);
        printf("\n");
        }
    
}
