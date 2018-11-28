/* 
 * File:   main.cpp
 * Author: perpetuity
 *
 * Created on 2011年5月7日, 上午7:13
 */

#include <cstdio>
#include <cstdlib>

using namespace std;

/*
 * 
 */
struct Node{
    char who;
    int where;
};

int main(int argc, char** argv) {
    int T;
    scanf("%d",&T);
    Node node[100];
    for(int cas=1;cas<=T;cas++){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            char str[2];
            int tmp;
            scanf("%s%d",str,&tmp);
            node[i].who=str[0];
            node[i].where=tmp;
        }
        int x=1,y=1,xt=0,yt=0,time=0;
        for(int i=0;i<n;i++){
            if(node[i].who=='O'){
                if(xt+abs(x-node[i].where)>=time) time=xt+abs(x-node[i].where);
                time++;
                xt=time;
                x=node[i].where;
            }
            else{
                if(yt+abs(y-node[i].where)>=time) time=yt+abs(y-node[i].where);
                time++;
                yt=time;
                y=node[i].where;
            }
        }
        printf("Case #%d: %d\n",cas,time);
    }
    return 0;
}
