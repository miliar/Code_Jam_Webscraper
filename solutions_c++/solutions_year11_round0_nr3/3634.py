#include<iostream>
#include<cmath>
using namespace std;

bool stat[1000];

void tambah(int x) {
     int i=0;
     while(x>0) {
                stat[i]=x%2;
                x/=2;
                i++;
                }
}                

int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,n,t,cse=1;
    
    scanf("%d",&t);
    while(t--) {
               scanf("%d",&n);
               int ot=0,ctr=1,xr,xor2,can[1000],tot=0;
               bool ktmu=0;
               for (i=0; i<n; i++) stat[i]=0;
               scanf("%d",&can[0]); xr=can[0]; tot=can[0];
               for (i=1; i<n; i++) {
                   scanf("%d",&can[i]);
                   xr=xr^can[i];
                   tot+=can[i];
                   }
               xor2=xr;
               for(i=0; i<n; i++) {
                        xor2=xr^can[i];
                        if (xor2==(xr^xor2)) {
                                             //cout<<(tot-can[i])<<endl;
                                             ktmu=1;
                                             ot=max(ot,tot-can[i]);
                                             }
                        }
               printf("Case #%d: ",cse); cse++;      
               if (!ktmu) printf("NO\n");
               else printf("%d\n",ot);                                                                    
               }
    
    //system("pause");
}
