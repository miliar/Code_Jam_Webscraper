//B

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

bool vis[5000];
int M[5000];
int base;

bool Insert(int i,int dis)
{
    int index = (base + i)>>1;
    
    //if(dis==0 && vis[index])return true;

    do{
        if( vis[index] )return false;
        
        if(dis==0)break;
        
        index >>=1;

    }while(dis--);
    
    while(index){
        vis[index]  = true;
        index >>= 1;
    }
    
    return true;
}



int main()
{
    
    int c,cs;
    scanf("%d",&c);
    cs=0;
    while(++cs<=c){
        int P;
        scanf("%d",&P);
        base  = 1<<P;
        for(int i=0;i<base;++i)scanf("%d",M+i);
        
        int ans=0;
        memset(vis,0,sizeof(vis));
        for(int i=0;i<base;++i){
            Insert(i,M[i]);
        }
        for(int i=P-1;i>=0;i--){
            int num = 1<<i;
            int nothing;
            while(num--)scanf("%d",&nothing);
        }
    
        for(int i=0;i<base;++i){
            if(vis[i]) ans++;
        }
        
        printf("Case #%d: %d\n",cs,ans);
    }
    
    
    
    return 0;    
}
/*
3
2
1 1 0 1
1 1
1

3
1 2 3 2 1 0 1 3 
1 1 1 1 
1 1 
1 
*/
