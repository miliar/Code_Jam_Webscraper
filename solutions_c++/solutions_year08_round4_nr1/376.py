#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;

int best[40001][2];
int ch[40001], type[40001];

int T, m, v, t1;

int get(int node, int val) {
    if(best[node][val] >= 0) return best[node][val];
    if(node >= (m-1)/2) {        
        return 1000000;
    }       
    
    int r0 = min(get(node*2+1,1)+get(node*2+2,0),get(node*2+1,0)+get(node*2+2,1));
    int r1 = get(node*2+1,1)+get(node*2+2,1);
    int r2 = get(node*2+1,0)+get(node*2+2,0);
    
    int res;
    if(val == 1) {
        if(type[node] == 0) {
            res = min(r0,r1);            
        }
        else {
            res = r1;
            if(ch[node]) res = min(res,1+r0);
        }
    }
    else {
        if(type[node] == 0) {
            res = r2;
            if(ch[node]) res = min(res,1+r0);
        }
        else {
            res = min(r0,r2);            
        }
    }        
    return best[node][val] = res;
} 
    

int main() {
    scanf("%d",&T);
    for(int z=0;z<T;z++) {
        scanf("%d %d",&m,&v);
        memset(best,-1,sizeof(best));
        memset(ch,0,sizeof(ch));        
        for(int i=0;i<(m-1)/2;i++) scanf("%d %d",&type[i],&ch[i]);
        for(int i=(m-1)/2;i<m;i++) {
            scanf("%d",&t1);
            best[i][t1] = 0;
        }        
        int ret = get(0,v);
        printf("Case #%d: ",z+1);
        if(ret >= 1000000) printf("IMPOSSIBLE\n");
        else printf("%d\n",ret);
    }
    return 0;
} 
            
        
