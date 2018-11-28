#include<cstdio>
#include<cstring>
#define max(x,y) (((x)>(y))?(x):(y))
#define abs(x) (((x)>(0))?(x):(-(x)))

int t,n,pos1,pos2,t1,t2;

int main(){
    scanf("%d",&t);
    for (int ca=1;ca<=t;++ca){
        pos1=pos2=1;
        t1=t2=0;
        scanf("%d",&n);
        for (int i=0;i<n;++i){
            char tar[10]; int to;
            scanf("%s%d",tar,&to);
            
            if (tar[0] == 'O'){
                int tmp = t1 + abs(pos1-to);
                pos1 = to;
                t1 = max(tmp, t2) +1;
            }
            else{
                int tmp = t2 + abs(pos2-to);
                pos2 = to;
                t2 = max(tmp, t1) +1;
            }
        }
        printf("Case #%d: %d\n",ca,max(t1,t2));
    }
    return 0;
}
