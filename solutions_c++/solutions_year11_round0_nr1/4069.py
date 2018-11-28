#include<stdio.h>

struct XD{int ind, but;};

int abs(int x){
    if(x >= 0) return x;
    else return -x;
}

int main(){
    int T,N,cnt,b,now_o, now_b, p_o, p_b,m,ind;
    XD robot_o[101], robot_b[101];
    char r;
    cnt = 0;
    scanf("%d",&T);
    while(T--){
        int time, k, j;
        time = k = j =0;
        cnt++;
        scanf("%d",&N);
        for(int i=1;i<=N;i++){
            scanf("%*c%c %d",&r,&b);
            if(r == 'O') robot_o[k].ind = i, robot_o[k++].but = b;
            else robot_b[j].ind = i, robot_b[j++].but = b;
        }
        p_o = p_b = 0;
        now_o = now_b = 1;
        for(int i=1;i<=N;i++){
            if(robot_o[p_o].ind == i && p_o < k){
                m = abs(robot_o[p_o].but - now_o) + 1;
                time+=m;
                now_o = robot_o[p_o].but;
                if(m >= abs(robot_b[p_b].but - now_b)) now_b = robot_b[p_b].but;
                else if(m < abs(robot_b[p_b].but - now_b)){
                    if(robot_b[p_b].but - now_b > 0) now_b += m;
                    else now_b -=m;
                }
                p_o++;
            }else if(robot_b[p_b].ind == i && p_b < j){
                m = abs(robot_b[p_b].but - now_b) + 1;
                time+=m;
                now_b = robot_b[p_b].but;
                if(m >= abs(robot_o[p_o].but - now_o)) now_o = robot_o[p_o].but;
                else if(m < abs(robot_o[p_o].but - now_o)){
                    if(robot_o[p_o].but - now_o > 0) now_o += m;
                    else now_o -= m; 
                }
                p_b++;
            }
        }
        printf("Case #%d: %d\n",cnt,time);
    }

    return 0;
}
