#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<stdlib.h>
#include<set>
#include<iostream>
#include<math.h>

#define INF 1000000000

using namespace std;

typedef long long lld;


int tree[5005];

struct node{
    int must,ind;
}in[2005];

int cmp(node A,node B){
    return (A.must<B.must);
}

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int P;
    int N;
    int Case,st;
    scanf("%d",&Case);
    for(int test=0;test<Case;test++){
        scanf("%d",&P);
        
        N=(int)pow(2,P);
        
        for(int i=0;i<N;i++){
            scanf("%d",&in[i].must);
            in[i].ind=i;
        }
        for(int i=0;i<5005;i++) tree[i]=0;
        int x=N/2;
        while(x){
            for(int i=0;i<x;i++) scanf("%d",&st);
            x/=2;
        }
        
     
        sort(in,in+N,cmp);
        
        st=(int)ceil(log2(N));
        st=(int)pow(2,st);
          
        int cnt=0;
        
        for(int i=0;i<N;i++){
            
            int pos=st+in[i].ind;
            for(int j=0;j<in[i].must;j++) pos/=2;
            pos/=2;
            while(pos){
                if(tree[pos]==0){
                    tree[pos]++;
                    cnt++;
                }    
                pos/=2;
            }
        }
        printf("Case #%d: %d\n",test+1,cnt);
    }
    return 0;
while(1);
}
