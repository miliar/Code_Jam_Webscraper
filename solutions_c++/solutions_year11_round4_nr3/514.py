#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <utility>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <inttypes.h>

using namespace std;

#define MAX 1024

int PD[MAX];
int Prime[MAX];
int NPrime[MAX];

int main(){
    FILE *fin = fopen("C-small-attempt0.in","r");
    FILE *fout = fopen("C.out","w");

    for(int i = 2 ; i < MAX ; i++) Prime[i] = 1;
    NPrime[0] = Prime[0] = 0;
    NPrime[1] = Prime[1] = 0;
    for(int i = 2 ; i < MAX ; i++){
        if(Prime[i]){
            NPrime[i] = NPrime[i-1] + 1;
            for(int j = 2*i ; j < MAX ; j+=i)  Prime[j] = 0;
        }
        else NPrime[i] = NPrime[i-1];
    }

    int nt;
    fscanf(fin,"%d",&nt);
    int teste;
    for(int teste = 1 ; teste <= nt ; teste++){
        int n;
        fscanf(fin,"%d",&n);
        int ans = 0;
        if(n == 1){
            fprintf(fout,"Case #%d: %d\n",teste,ans);
        }
        else{
            for(int i = 1 ; i <= n ;i++)   PD[i] = i;
            ans = 1;
            for(int i = 2 ; i <= n ;i++){
                if(PD[i] != 1){
                    ans++;
                    for(int j = 2*i; j <= n; j+=i){
                        PD[j] /= PD[i];
                    }
                }
            }
            //printf("%d %d\n", ans, NPrime[n]);
            fprintf(fout,"Case #%d: %d\n",teste,ans - NPrime[n]);
        }
    }
    return 0;
}
