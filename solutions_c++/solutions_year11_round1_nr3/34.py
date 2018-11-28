#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<map>
//using namespace std;
typedef long long LL;
inline LL Min(LL a,LL b){
    return a<b?a:b;
}
inline LL Max(LL a,LL b){
    return a>b?a:b;
}
inline LL Abs(LL a){
    return a>0?a:-a;
}
bool cmp(LL a,LL b){
    return a>b;
}
int casN,n,m,car[200][3],ans,c,t,s,pla[200],tmp,sor[200],sos;
int main(){
    scanf("%d",&casN);
    for(int III=0;III<casN;III++){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d%d%d",&car[i][0],&car[i][1],&car[i][2]);
        }
        scanf("%d",&m);
        for(int i=n;i<n+m;i++){
            scanf("%d%d%d",&car[i][0],&car[i][1],&car[i][2]);
        }
        c=n;
        t=1;
        s=0;
        n=n+m;
        ans=0;
        memset(pla,0,sizeof(pla));
        while(t>0){
            for(int i=0;i<c&&i<n;i++){
                if(!pla[i]&&car[i][2]!=0){
                    t+=car[i][2]-1;
                    c+=car[i][0];
                    s+=car[i][1];
                    pla[i]=1;
                    goto NEXT;
                }
            }
            tmp=s;
            sos=0;
            for(int i=0;i<c&&i<n;i++){
                if(!pla[i]&&car[i][0]==0){
                    sor[sos++]=car[i][1];
                }
            }
            std::sort(sor,sor+sos,cmp);
            for(int i=0;i<t&&i<sos;i++)tmp+=sor[i];
            if(tmp>ans)ans=tmp;
            
            tmp=-1;
            for(int i=0;i<c&&i<n;i++){
                if(!pla[i]&&car[i][0]==1&&(tmp==-1||car[i][1]>car[tmp][1])){
                    tmp=i;
                }
            }
            if(tmp==-1)break;
            c+=car[tmp][0];
            s+=car[tmp][1];
            t+=car[tmp][2]-1;
            pla[tmp]=1;
            if(s>ans)ans=s;
            
            NEXT:;
        }
        printf("Case #%d: %d\n",III+1,ans);
    }
    scanf(" ");
    return 0;
}

