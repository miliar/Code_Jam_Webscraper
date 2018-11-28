#include <cstdio>
#include <queue>
using namespace std;

int deck[5005];


int main(){
    int test;
    scanf("%d",&test);
    for(int t=0;t<test;t++){
        int n;
        scanf("%d",&n);
        queue<int> q;
        for(int i=0;i<n;i++)
            q.push(i);
        int c=1,x;    
        while(!q.empty()){
            for(int i=0;i<c-1;i++){
                x=q.front(); q.pop();
                q.push(x);
            }
            x=q.front(); q.pop();
            deck[x]=c;
            c++;    
        }
        printf("Case #%d:",t+1);
        int ind;
        scanf("%d",&ind);
        int tt;
        for(int i=0;i<ind;i++){
            scanf("%d",&tt);
            printf(" %d",deck[tt-1]);
        }
        printf("\n");
    }
    
    return 0;
}
