#include<cstdio>
#include<set>
#include<map>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int ja[1100];

map <string, int> pl;
map <string, int>::iterator it;

int main() {
    char in[110];
    string novo;
    int N,Q,S,i,j,k,foi,res,inst=1;
    scanf("%d\n" , &N);
    for(i=0;i<N;i++) {
        pl.clear();
        res = 0;
        scanf("%d\n", &S);
        for(j=0;j<S;j++) {
            fgets(in , 110, stdin);
            novo = in;            
            pl.insert(pair<string,int> (novo,j));
        }
        scanf("%d\n", &Q);
        memset(ja,0,sizeof(ja));
        foi = 0;
        for(j=0;j<Q;j++) {
            fgets(in, 110, stdin);
//            for(k=0; strcmp(pl[k].p , in.p)!=0;k++);
            novo = in;            
            it = pl.find(novo);            
            k = (*it).second;
            if(ja[k] == 0) {
                ja[k] = 1;
                foi++;
            }
            if(foi == S) {
                res++;
                foi = 1;
                memset(ja,0,S*sizeof(int));
                ja[k] = 1;
            }
        }
        
        printf("Case #%d: %d\n" , inst++, res);
    }
    return 0;
}
