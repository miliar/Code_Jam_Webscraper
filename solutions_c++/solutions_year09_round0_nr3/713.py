#include <iostream>
using namespace std;
//var
string p,s;
int f[20];

void khoitao(void) {
     p="welcome to code jam";
     memset(f,0,sizeof(f));
};

int scs(int x) {
    int dem=0;
    do {
       dem++;
       x=x/10;
    } while (x>0);
    return dem;
};

void xuli(void) {
     int i,j,n,m;
     n=s.length();
     m=p.length();
     f[0]=1;
     for (i=0;i<n;i++) {
         for (j=0;j<m;j++) if (s[i]==p[j]) {
             f[j+1]+=f[j];
             f[j+1]=f[j+1]%10000;
         };
     };
             
     int kq;
     kq=f[m]%10000;
     for (i=1;i<=(4-scs(kq));i++) printf("0");
     printf("%d\n",kq);
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i;
    scanf("%d\n",&t);
    for (i=1;i<=t;i++) {
        khoitao();
        printf("Case #%d: ",i);
        getline(cin,s);
        xuli();
    };
    return 0;
};
