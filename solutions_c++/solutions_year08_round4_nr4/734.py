#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
char line[60000];
char nline[60000];

int comp(char * str){
    int t = 0;
    char ch;
    
    ch = str[0];
    for (char * p = str; *p; ){
        while (*p && *p == ch)
              p ++;
        t ++;
        ch = *p;
    }
    
    return t;
}
              
int main(){
    
    int c, t;
    scanf("%d", &t);
    
    for (int casno = 1; casno <= t; casno ++){
        int k;
        scanf("%d", &k);
        scanf("%s", line);
        
       // printf("%s\n", line);
        vector<int> p(k, 0);
        
        for (int i = 0; i < k; i ++)
            p[i] = i;
        int len = strlen(line);
        int Min = len + 1000000;
        do{
            for (int i = 0; i < len; i += k){
                for (int j = 0; j < k; j ++){
                    nline[i + j] = line[i + p[j]];
                }
            }
            nline[len] = '\0';
            Min = min(Min, comp(nline));
        }while (next_permutation(p.begin(), p.end()));
        
        printf("Case #%d: %d\n", casno, Min);
    }
    
    return 0;
}
        
        
        
        
