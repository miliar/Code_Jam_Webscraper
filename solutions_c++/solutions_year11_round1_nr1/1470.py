/* 
 * File:   main.cpp
 * Author: perpetuity
 *
 * Created on 2011年5月21日, 上午8:58
 */

#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        int n,d,g;
        scanf("%d%d%d",&n,&d,&g);
        printf("Case #%d: ",cas);
        if(g==100){
            if(d!=100){
                printf("Broken\n");
                continue;
            }
        }
        if(g==0){
            if(d!=0){
                printf("Broken\n");
                continue;
            }
        }
        if(n>=100) printf("Possible\n");
        else{
            bool flag=false;
            for(int i=1;i<=n;i++){
                if(d*i%100==0){
                    printf("Possible\n");
                    flag=true;
                    break;
                }
            }
            if(!flag){
                printf("Broken\n");
            }
        }
    }
    return 0;
}

