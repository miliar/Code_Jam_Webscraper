#include <stdio.h>
#include <string.h>

struct robot{
       char color;
       int pos;
};

int sign(int a, int b){
    return (a>b)? 1: -1;
}

int abs(int a){
    return (a>0)? a: -a;
}

int main(){
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, N, sum;
    char c[10]; 
    scanf("%d", &T);
    for(int k=1; k<=T; k++){
        robot bot[100];
        memset(bot, 0, sizeof(bot));
        sum = 0;
        scanf("%d", &N);      
        for(int i=0; i<N; i++){
            scanf("%s", c);
            bot[i].color = c[0];
            scanf("%d", &bot[i].pos);
        }
        int blue=0, orange=0, opos=1, bpos=1, count=0, origin=0;
        while(blue<N && orange<N){
              count = origin;
              
              if(bot[origin].color=='B'){
                 while(bot[count].color=='B') count++;
                 orange = count;
                 sum += abs(bpos-bot[origin].pos)+1;
                 int substr = bpos-bot[origin].pos;
                 bpos = bot[origin].pos;
                 if(orange==N){
                    for(int j=origin+1; j<N; j++){
                        sum += abs(bpos-bot[j].pos)+1;
                        bpos = bot[j].pos;
                    }           
                    break;           
                 }
                 if(abs(opos-bot[orange].pos)<=abs(substr))
                    opos = bot[orange].pos;
                 else
                    opos = opos + sign(bot[orange].pos, opos)*(abs(substr)+1);
                 origin++;  
                                
              }else if(bot[origin].color=='O'){
                 while(bot[count].color=='O') count++;
                 blue = count;
                 sum += abs(opos-bot[origin].pos)+1;
                 int substr = opos-bot[origin].pos;
                 opos = bot[origin].pos;
                 if(blue==N){
                    for(int j=origin+1; j<N; j++){
                        sum += abs(opos-bot[j].pos)+1;
                        opos = bot[j].pos;
                    }            
                    break;           
                 }
                 if(abs(bpos-bot[blue].pos)<=abs(substr))
                    bpos = bot[blue].pos;
                 else
                    bpos = bpos + sign(bot[blue].pos, bpos)*(abs(substr)+1);  
                 origin++;
              }
        }
        printf("Case #%d: %d\n", k, sum);                              
    }   
    return 0;   
}
