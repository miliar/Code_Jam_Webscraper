#include<iostream>
#include<cstdio>
using namespace std;

char ans[111],an;

int table[5000]={0};
int com[5000]={0};
bool opp[5000]={0};          // =1  -> clear

bool opposed(char c){
    for(int i=1;i<an;i++){
        if(opp[ table[c]+table[ans[i]] ]){
            return 1;
        }
    }
    return 0;
}

int main(){
    int T,c,d,n,cas=1;
    char s,t,u;
    
    table['Q'] = 1;
    table['W'] = 3;
    table['E'] = 9;
    table['R'] = 27;
    table['A'] = 81;
    table['S'] = 243;
    table['D'] = 729;
    table['F'] = 2187;
    
    scanf("%d",&T);
    while(T--){
        
        for(int i=0;i<5000;i++){
            com[i] = opp[i] = 0;
        }
        
        scanf("%d",&c);
        for(int i=0;i<c;i++){
            scanf("%d",&s);     //read ' '
            scanf("%c%c%c",&s,&t,&u);
            com[ table[s]+table[t] ] = u;
        }
        
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            scanf("%d",&s);     //read ' '
            scanf("%c%c%c",&s,&t);
            opp[ table[s]+table[t] ] = 1;
        }
        
        scanf("%d",&n);
        scanf("%d",&s);     //read ' '
        an = 1;
        ans[0] = 0;         //don't use
        for(int i=0;i<n;i++){
            scanf("%c",&s);
            if(t = com[ table[s]+table[ans[an-1]] ]){
                ans[an-1] = t;
            }else if(opposed(s)){
                an = 1;
            }else{
                ans[an++] = s;
            }
        }
        
        printf("Case #%d: [", cas++);
        if(an>1) printf("%c", ans[1]);
        for(int i=2;i<an;i++){
            printf(", %c", ans[i]);
        }
        printf("]\n");
    }
    
    return 0;
}
