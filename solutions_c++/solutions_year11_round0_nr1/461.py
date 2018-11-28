#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int update_pos(int temp, int pos[], int nxt[], int but[][4]){
    int i,j,k;
    int time=0;
    int a,b;
    a = but[temp][1];
    b = (1+a)%2;
    time = abs( pos[a] - but[temp][0])+1;
    pos[a] = but[temp][0];
    nxt[a] = but[temp][2];
    if ( abs( pos[b] - but[nxt[b]][0]) <= time) pos[b] = but[nxt[b]][0];
    else {
         if (pos[b] > but[nxt[b]][0]) pos[b] = pos[b] - time;
         if (pos[b] < but[nxt[b]][0]) pos[b] = pos[b] + time;
    }
    return time;
}    
    
                        




int main(){
    int i,j,k,temp={0},count,time;
    int t,n,fi[3]={0},nxt[3]={0},but[200][4]={0};
    int pos[3];
    char tempch;
    //FILE* fin = fopen("BotTrust.in","r");
    FILE* fin = fopen("A-large.in","r");
    FILE* fout= fopen("A-large.out","w");
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;++i){
        fscanf(fin,"%d",&n);
        for (j=1;j<=n;++j){
            tempch = ' ';
            while(tempch == ' ') fscanf(fin, "%c",&tempch);
            fscanf(fin,"%d",&temp);
            but[j][0] = temp;
            if (tempch == 'O') but[j][1] = 0;
            else if (tempch == 'B') but[j][1] = 1;
        }
        count = 0;
        for (j=1;j<=n;++j){
                while (but[j][1] == 0 && j <= n) ++j;
                if (count==0){ 
                               fi[1] = j;
                               count = j;
                }
                else if (count > 0){
                     but[count][2] = j;
                     count = j;
                }
                if (j == n+1) but[count][2] = count;
             
        }

        count = 0;
        for (j=1;j<=n;++j){
                while (but[j][1] == 1 && j <= n) ++j;
                if (count==0){ 
                               fi[0] = j;
                               count = j;
                }
                else if (count > 0){
                     but[count][2] = j;
                     count = j;
                }
                if (j == n+1) but[count][2] = count;
        }
        but[n][2]=n;
        time = 0;
        nxt[0]=fi[0];
        nxt[1]=fi[1];
        pos[0]=1;
        pos[1]=1;
        for (j=1;j<=n;++j){
            time += update_pos( j,  pos,  nxt,  but);
        }
        fprintf(fout,"Case #%d: %d\n",i, time);
            
    }
    
    //for (j=1;j<=n;++j) printf("%d %d %d, ",but[j][0], but[j][1], but[j][2]);
    
    return 0;
}

    
