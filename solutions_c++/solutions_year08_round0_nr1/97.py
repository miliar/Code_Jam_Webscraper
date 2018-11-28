#include <stdio.h>
#include <map>
#include <vector>
#include <string>
using namespace std;

int dpmat[1100][110];
char buffer[1000];

int main(){
    int ntc;
    scanf("%d", &ntc);
    int ttc=0;
    while (ntc--){
        map<string, int> namemo;
        int n;
        scanf("%d", &n);
        gets(buffer);
        for (int i=0;i<n;i++){
            gets(buffer);
            namemo[buffer] = i;
        }
        memset(dpmat,-1,sizeof(dpmat));
        int m;
        scanf("%d", &m);
        gets(buffer);
        for (int i=0;i<m;i++){
            gets(buffer);
            int num = namemo[buffer];
            
            if (i){
                for (int j=0;j<n;j++)
                if (j!=num)
                    for (int k=0;k<n;k++)
                        if (dpmat[i-1][k]!=-1){
                            int tres = dpmat[i-1][k]+(j!=k);
                            if ((dpmat[i][j]==-1) || (tres<dpmat[i][j]))
                                dpmat[i][j]=tres;
                        }                             
            } else {
                for (int j=0;j<n;j++)
                    if (j!=num)
                        dpmat[0][j]=0;
            }
        }        
        int res = 2000000000;
        for (int i=0;i<n;i++){
            if (dpmat[m-1][i]!=-1)
                res<?=dpmat[m-1][i];
        }
        
        printf("Case #%d: %d\n", ++ttc, res);
    }
    
    return 0;    
}
