
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main(){
        int nn;scanf("%d",&nn);
        for(int npr=1;npr<=nn;npr++){
                int n;scanf("%d",&n);
                int prevtim[2]={0,0};
                int prevpos[2]={1,1};
                int last=0;
                for(int i=0;i<n;i++){
                        char c;
                        int pos;scanf(" %c%d",&c,&pos);
                        int blue=(c=='B');
                        int moveend=max(prevtim[blue]+abs(prevpos[blue]-pos),last);
                        last=prevtim[blue]=moveend+1;
                        prevpos[blue]=pos;
                }
                printf("Case #%d: %d\n",npr,last);
        }
        return 0;
}
