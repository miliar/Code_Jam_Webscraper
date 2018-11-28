#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>
#include <map>

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;

struct node{
    int size;
    vector<int>adj;
    int start;
    int num;
}NODE[1005];
int n;

int dfs(int x){
    for(int i=0;i<NODE[x].size;i++){
        NODE[NODE[x].adj[i]].num += NODE[x].num;
        dfs(NODE[x].adj[i]);
    }
}

class Solve {

    public:
    void main2(){
        scanf("%d",&n);
        int num;
        for(int i=1;i<=n;i++){
            scanf("%d",&NODE[i].size);
            for(int j=0;j<NODE[i].size;j++){
                scanf("%d",&num);
                NODE[i].adj.push_back(num);
                NODE[num].start = 1;
            }
        }
        int solve = 0;
        for(int i=1;i<=n;i++){
            if(NODE[i].start == 0){
                NODE[i].num = 1;
                dfs(i);
                for(int j=1;j<=n;j++){
                    if(NODE[j].num >= 2){
                        solve = 1;
                        break;
                    }
                }
                for(int j=1;j<=n;j++){
                    NODE[j].num = 0;
                }
            }
        }
        if(solve) printf("Yes\n");
        else printf("No\n");
        
        for(int i=1;i<=n;i++){
            NODE[i].size = NODE[i].num = NODE[i].start = 0;
            NODE[i].adj.clear();
        }
    }
};

int main(){
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        Solve ___test;
        printf("Case #%d: ", t);
        ___test.main2();
    }
return 0;
}
