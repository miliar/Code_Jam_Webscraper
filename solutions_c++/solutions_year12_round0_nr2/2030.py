#include<iostream>
#include<cstdio>
using namespace std;

int flag[101][2];//[1]代表>=score，[2]是[1]>=score下分别0是surprising，1非surprising，2同时满足
int res;
void pick(int num, int score) {
    int temp = score / 3;
    if(score % 3 == 0) {
        //cout<<"temp="<<temp<<endl;
        if(temp >= res) {
            if(temp - 1 >=0) {
                flag[num][0] = 1;
                flag[num][1] = 2;
            } else if(temp == 0) {
                flag[num][0] = 1;
                flag[num][1] = 1;
            }
        } else if(temp - 1 >= 0 && temp >= res -1 ) {
            flag[num][0] = 1;
            flag[num][1] = 0;
        } else {
            //
        }
    }
    if(score % 3 == 1) {
        if(temp >= res -1) {
            if(temp - 1 >= 0) {
                flag[num][0] = 1;
                flag[num][1] = 2;
            } else if(temp == 0) {
                flag[num][0] = 1;
                flag[num][1] = 1;
            }
        } else {
            //
        }
    }
    if(score % 3 == 2) {
        if(temp >= res - 1) {
            flag[num][0] = 1;
            flag[num][1] = 2;
        } else if(temp >= res - 2) {
            flag[num][0] = 1;
            flag[num][1] = 0;
        } else {
            //
        }
    }
}

int main() {
    freopen("bb.in","r",stdin);
    freopen("output.txt","w",stdout);
    int ca,num,surp,score;
    scanf("%d",&ca);    
    for(int i = 1; i <= ca; ++i) {
        memset(flag,0,sizeof(flag));
        scanf("%d%d%d",&num,&surp,&res);
        int cnt = 0, cnt0 = 0, cnt1 = 0, cnt2 = 0;
        for(int j = 0; j != num; ++j) {
            scanf("%d",&score);
            pick(j,score);
        }
        for(int k = 0; k != num; ++k) {
            if(flag[k][0] == 1) {
                cnt++;
                if(flag[k][1] == 0) {
                    cnt0++;
                } else if(flag[k][1] == 1) {
                    cnt1++;
                } else if(flag[k][1] == 2) {
                    cnt2++;
                }
            }
        }
        int ans;
        if(surp <= cnt0) {
            ans = cnt2 + cnt1 + surp;
        } else {
            ans = cnt;
        }
        //printf("Case #%d: %d %d %d %d\n",i,cnt,cnt0,cnt1,cnt2);
        printf("Case #%d: %d\n",i,ans);
    }
}
