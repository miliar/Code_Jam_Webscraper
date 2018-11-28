#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;

#define MOD 10007

int T, c, r, best, co;
int room[10][10], sum[10];
char ch;

bool isOk(int R, int C) {
    if(room[R][C] == -1) return 0;
    if(R > 0 && C > 0 && room[R-1][C-1] == 1) return 0;
    if(R > 0 && C < c-1 && room[R-1][C+1] == 1) return 0;
    if(C > 0 && room[R][C-1] == 1) return 0;
    if(C < c-1 && room[R][C+1] == 1) return 0;
    return 1;
}

void go(int R, int C, int N) {
    if(R == r) {
        best >?= N;
        return;
    }
    if(R == r-1) co = 0;
    else co = sum[R+1];
    if(N+(c-C+1)/2 +co<= best) return;
    if(isOk(R,C)) {        
        room[R][C] = 1;
        if(C < c-1) go(R,C+1,N+1);
        else go(R+1,0,N+1);
        room[R][C] = 0;
    }
    if(C < c-1) go(R,C+1,N);
    else go(R+1,0,N);
}

int main() {
    scanf("%d",&T);
    for(int z=0;z<T;z++) {
        best = 0;
        scanf("%d %d",&r,&c);
        scanf("%c",&ch);
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                scanf("%c",&ch);
                if(ch == '.') room[i][j] = 0;
                else room[i][j] = -1;
            }
            scanf("%c",&ch);
        }
        sum[r-1] = 0;
        for(int i=r-1;i>=0;i--) {
            int tmp = 0, tsum = 0;
            for(int j=0;j<c;j++) {
                if(room[i][j] == 0) tmp++;
                else {
                    tsum += (tmp+1)/2;
                    tmp = 0;
                }
            }
            tsum += (tmp+1)/2;
            if(i == r-1) sum[r-1] = tsum;
            else sum[i] = sum[i+1]+tsum;
        }            
        go(0,0,0);       
        printf("Case #%d: %d\n",z+1,best);
    }
    return 0;
} 
            
        
