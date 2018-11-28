#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
//#include <pair>
using namespace std;

set<pair<int,int> > sett;

int main(){
    FILE *f = fopen("c.in","r");
    FILE *o = fopen("c.out","w");
    
    int T,A,B,m; 
    char s[100];
    char ss[100];
    fscanf(f,"%d",&T);
    for (int t = 1 ; t <= T ; t++){
        fscanf(f,"%d %d",&A,&B);
        int ans = 0;
        sett.clear();
        for (int n = B-1 ; n >= A ;n--) {
            sprintf(s,"%d",n);
            int l = strlen(s);
            s[l] = s[0];
            s[l+1] = 0;
            for (int i = 1 ; i < l ;i++){
                
                if (s[i] != '0') {
                    m = atoi(s+i);
                    if (m <= B && n < m){
                        sett.insert(pair<int,int>(n,m));
                    }
                }
                s[i+l] = s[i];
                s[i+l+1] = 0;
            }
        }
        ans = sett.size();
        printf("finish case %d ans = %d\n",t,ans);
        fprintf(o,"Case #%d: %d\n",t,ans);
    }
    
    fclose(f);
    fclose(o);
    //system("pause");
}
