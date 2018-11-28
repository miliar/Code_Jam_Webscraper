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
    long long type;
    long long num;
}in[105], in1[105];

long long DP[105][105];
int n, m;
long long opt(int p, int x, int y){
    if(x > n) return 0;
    if(y > m) return 0;
    if(DP[x][y] != -1 && p == 1)
        return DP[x][y];
    long long temp = 0;
    if(in[x].type != in1[y].type)
        temp = max(temp, max(opt(p & 1, x, y+1), opt(p & 1, x+1, y)));
    else {
        // loop box
        long long a = in[x].num;
        long long b = 0;
        for(int i=y;i<=m;i++){
            if(in[x].type == in1[i].type){
                if(a >= in1[i].num){
                    a -= in1[i].num;
                    b += in1[i].num;
                    temp = max(temp, b + opt(p & 1, x + 1, i + 1));
                } else {
                    b += a;
                    temp = max(temp, b + opt(p & 1, x + 1, i + 1));
                    in1[i].num -= a;
                    if(in1[i].num){
                        temp = max(temp, b + opt(0, x + 1, i));
                    }
                    in1[i].num += a;
                    
                    break;
                }
            }
        }
        // loop toy
        a = in1[y].num;
        b = 0;
        for(int i=x;i<=n;i++){
            if(in1[y].type == in[i].type){
                if(a >= in[i].num){
                    a -= in[i].num;
                    b += in[i].num;
                    temp = max(temp, b + opt(p & 1, i + 1, y + 1));
                } else {
                    b += a;
                    temp = max(temp, b + opt(p & 1, i + 1, y + 1));
                    in[i].num -= a;
                    if(in[i].num){
                        temp = max(temp, b + opt(0, i, y + 1));
                    }
                    in[i].num += a;
                    
                    break;
                }
            }
        }
    }
    if(p)
        DP[x][y] = temp;
    return temp;
}


class Solve {

    public:
    void main2(){
        scanf("%d %d",&n, &m);
        for(int i=1;i<=n;i++){
            scanf("%lld %lld",&in[i].num, &in[i].type);
        }
        for(int i=1;i<=m;i++){
            scanf("%lld %lld",&in1[i].num, &in1[i].type);
        }
        for(int i=0;i<=n;i++)
            for(int j=0;j<=m;j++)
                DP[i][j] = -1;
        printf("%lld\n",opt(1, 1, 1));
    }
};

int main(){
    freopen("C-small-attempt4.in","r",stdin);
    freopen("C-small-attempt4.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for(int t=1;t<=Test;t++){
        Solve ___test;
        printf("Case #%d: ", t);
        ___test.main2();
    }
    
return 0;
}
