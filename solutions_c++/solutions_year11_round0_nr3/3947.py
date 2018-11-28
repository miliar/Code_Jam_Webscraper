#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main(){
        int nn;scanf("%d",&nn);
        for(int npr=1;npr<=nn;npr++){
                int n;scanf("%d",&n);
                int asum=0;
                int xsum=0;
                int mins=1000*1000*1000;
                for(int i=0;i<n;i++){
                        int v;scanf("%d",&v);
                        asum+=v;
                        xsum^=v;
                        mins=min(mins,v);
                }
                printf("Case #%d: ",npr);
                if(xsum==0)printf("%d\n",asum-mins);
                else puts("NO");
        }
        return 0;
}
