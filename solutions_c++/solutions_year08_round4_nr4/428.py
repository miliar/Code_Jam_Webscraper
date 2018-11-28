#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

char buffer[100000];
char butemp[100000];

int main(){
    int ntc,ttc=0;
    scanf("%d", &ntc);
    while (ntc--){
        int k;
        scanf("%d", &k);
        gets(buffer); // trash
        gets(buffer);
        
        vector<int> permutor;
        for (int i=0;i<k;i++)
            permutor.push_back(i);
            
        int res = strlen(buffer);
        int len = res;
        do {
            for (int i=0;i<len;i++){
                int left = i-i%k;
                butemp[i] = buffer[left+permutor[i-left]];
            }
            int tres = 1;
            for (int i=1;i<len;i++){
                if (butemp[i]!=butemp[i-1]) tres++;
            }
            res<?=tres;
        } while (next_permutation(permutor.begin(), permutor.end()));
        
        printf("Case #%d: %d\n", ++ttc, res);
    }
    
    return 0;
}
