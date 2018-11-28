#include<cstdio>

int T,n,s,p,t[100];
int pt[3];
int cnt;

int main(){
    int i,j;
    scanf("%d",&T);
    for(int lt=1;lt<=T;lt++){
        scanf("%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++)
            scanf("%d",&t[i]);
        cnt=0;
        for(i=0;i<n;i++){
            pt[0]=pt[1]=pt[2]=t[i]/3;
            t[i]%=3;
            for(j=2;j>=0;j--){
                if(t[i]){
                    pt[j]++;
                    t[i]--;
                }
            }
            if(pt[2]>=p){
                cnt++;
            }else if(s){
                if(pt[0]==pt[2] && pt[0]>0){
                    pt[0]--;
                    pt[2]++;
                }else if(pt[1]==pt[2] && pt[1]>1){
                    pt[1]--;
                    pt[2]++;
                }
                if(pt[2]>=p){
                    cnt++;
                    s--;
                }
            }
        }
        printf("Case #%d: %d\n",lt,cnt);
    }
    return 0;
}
