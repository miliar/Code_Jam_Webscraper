#include<stdio.h>
using namespace std;

int main(){
    int n,r,t,k;
    scanf("%d\n",&t);
    for(int i=0;i<t;i++){
        long long tsum = 0;
        scanf("%d%d%d",&r,&k,&n);
        int arr[n];
        int sum[n][n];
        for(int j=0;j<n;j++){
            scanf("%d",&arr[j]);
            sum[j][j] = arr[j];
            tsum += arr[j];
        }

        if(tsum <= k){
            printf("Case #%d: %lld\n", i+1, tsum*r);
            continue;
        }

        for(int x=0;x<n;x++){
            for(int y=x+1;y<n;y++){
                sum[x][y] = sum[x][y-1] + arr[y];
            }
        }

        for(int x=0;x<n;x++){
            for(int y=0;y<x;y++){
                sum[x][y] = sum[x][n-1] + sum[0][y];
            }
        }

        int end[n];
        for(int x=0;x<n;x++)
            end[x] = x-1>=0?x-1:x-1+n;

        for(int x=0;x<n;x++){
            int y  = end[x];
            while(sum[x][y] > k) {y--; if(y<0)y+=n;}
            end[x] = y;
        }

        int cnt = 0;
        long long money = 0;
        int cur = 0;
        while(1){
            if(cnt>=r)break;
            money += sum[cur][end[cur]];
            cnt++;
            cur = (end[cur]+1)%n;
        }

        printf("Case #%d: %lld\n", i+1, money);
    }
    return 0;
}
