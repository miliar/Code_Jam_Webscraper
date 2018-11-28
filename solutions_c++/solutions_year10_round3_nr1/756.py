#include <stdio.h>
#include <conio.h>
#include <vector>

using namespace std;


int main(){
    int n,t,r;
    int izq,der;
    scanf("%d",&t);
    vector<int> vi;
    vector<int> vd;
    for (int t2=1;t2<=t;t2++){
        scanf("%d",&n);            
        vi.assign(n,0);
        vd.assign(n,0);                
        for (int i=0;i<n;i++){
            scanf("%d %d",&izq,&der);
            vi[i]=izq;
            vd[i]=der;
            }
        r=0;
        for (int i=0;i<n-1;i++){
            for (int j=i+1;j<n;j++){        
                if (vi[i]<vi[j]){
                   if (vd[j]<vd[i])
                      r++;                 
                   }
                }
            }
        printf("Case #%d: %d\n",t2,r); 
        }
    getch();
    return 0;
    }

