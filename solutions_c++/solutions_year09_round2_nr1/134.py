#include <cstdio>
#include <string>
using namespace std;
int t,tt,i,j,k,l,e,n,q,m;
int b[100000][2],a[100000],c[100000];
double f[100000],p;
string s[100000],T[100000];
char ch,st[100000];
bool qq;
int main() {
   freopen("Al.in","r",stdin);
   freopen("Al.out","w",stdout);
   scanf("%d",&t);
   for (tt=1; tt<=t; tt++) {
      scanf("%d",&n); ch=' ';
      while (ch!='(') ch=getchar();
      e=1; s[1]=""; a[1]=0; i=1; m=1; ch=getchar();
      while (e>0) {
         if (ch>='0' && ch<='9') {
            p=ch-'0'; q=0;
            while (true) {
               ch=getchar();
               if (ch=='.') q=1; else if (ch>='0' && ch<='9') {
                  p=p*10+ch-'0';
                  if (q>0) q++;
               } else break;
            }
            for (j=1; j<q; j++) p/=10;
            f[i]=p;
         } else if (ch>='a' && ch<='z') {
            s[i]="";
            while (ch>='a' && ch<='z') {
               s[i]=s[i]+ch; ch=getchar();
            }
         } else {
           if (ch=='(') {
             e++; b[i][a[i]]=++m; a[i]++;
             c[m]=i; i=m; s[i]=""; a[i]=0;
           } else if (ch==')') {
             e--; i=c[i];
           }
           ch=getchar();
         }
      }
      printf("Case #%d: \n",tt);
      scanf("%d\n",&n);
      for (i=1; i<=n; i++) {
         scanf("%s",st);
         scanf("%d",&l);
         for (k=0; k<l; k++) { scanf("%s",st); T[k]=st; }
         p=f[1]; j=1;
         while (a[j]>0) {
            qq=false;
            for (k=0; k<l; k++) if (T[k]==s[j]) { qq=true; break; }
            if (qq) j=b[j][0]; else j=b[j][1];
            p*=f[j];
         }
         printf("%.8lf\n",p);
      }
   }
   return 0;
}
