#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
int di[10100];
int li[10100];
int md[10100];
inline bool solve(){
    int n,i,j;
    scanf("%d",&n);
    for(i=0;i<n;i++)scanf("%d%d",&di[i],&li[i]);
    int dd;
    scanf("%d",&dd);
    for(i=0;i<n;i++)md[i]=-1;
    md[0]=di[0];
    for(i=0;i<n;i++){
        if(md[i]==-1)continue;
        if(md[i]+di[i]>=dd)return 1;
        for(j=i+1;j<n;j++){
            if(di[j]-di[i]>md[i])break;
            if(md[j]!=-1)continue;
            md[j]=di[j]-di[i];
            if(md[j]>li[j])md[j]=li[j];
        }
    }
    return 0;
}
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        printf("Case #%d: %s\n",cas++,solve()?"YES":"NO");
    }
}

