#include<iostream>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,n,k,r;
    char col;
    scanf("%d\n",&tc);
    for(int t=1;t<=tc;t++){
        int p[2]={1,1},res[2]={0,0};
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf(" %c %d",&col,&k);
            r=(col=='B'?1:0);
            res[r]=max(res[r]+abs(k-p[r]),res[r^1])+1;
            p[r]=k;
        }
        printf("Case #%d: %d\n",t,max(res[0],res[1]));
    }
    return 0;
}
