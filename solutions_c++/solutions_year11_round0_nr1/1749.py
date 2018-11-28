#include <iostream>
#include <algorithm>
#define MAXN 200000
using namespace std;
int abso(int n){
    return n < 0 ? -n : n;
}
int main(){
    int T, N, L, otime, btime, prevb, prevo, tc = 1;
    char name[2];
    scanf("%d", &T);
    while(T--){
           btime = 0, otime = 0;
           prevb = 1, prevo = 1;    
           scanf("%d", &N);
           for(int i = 0; i < N; i++){
                   scanf("%s %d", name, &L);
                   if(name[0] == 'B'){
                         btime += abso(L - prevb) + 1;
                         if(btime <= otime) btime = otime + 1;  
                         prevb = L;
                   }
                   else{
                         otime += abso(L - prevo) + 1;
                         if(otime <= btime) otime = btime + 1;
                         prevo = L;
                   }
           }    
           printf("Case #%d: %d\n", tc, max(otime, btime));
           tc++;
    }
    return 0;
}

