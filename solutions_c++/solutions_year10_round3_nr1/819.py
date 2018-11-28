#include <stdio.h>
int x[1001], y[1001];

void solve(int cases){
    int n, cnt=0;
    scanf("%d",&n);
    for(int i=0;i!=n;++i)scanf("%d%d",x+i,y+i);
    for(int i=0;i!=n;++i)
        for(int j=i+1;j!=n;++j)
            if((x[i]>x[j]) ^ (y[i]>y[j])) cnt++ ;
        
    printf("Case #%d: %d\n",cases,cnt);

}

int main(){
    int cases;
    scanf("%d",&cases);
    for(int i=1;i<=cases;++i)solve(i);
    return 0;
}
