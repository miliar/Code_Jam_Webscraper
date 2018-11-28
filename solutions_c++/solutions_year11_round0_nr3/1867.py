#include<cstdio>
#include<iostream>
using namespace std;
int main(){
    int T;
      //freopen ("C-large.in","r",stdin);
      //freopen ("CC.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        int n;
        scanf("%d",&n);
        int minn=2000000000;
        int num;
        int sum=0;
        int ans=0;
        for(int i=0;i<n;i++){
            scanf("%d",&num);
            sum=sum^num;
            ans+=num;
            minn=min(num,minn);
        }
        if(sum!=0){
            printf("Case #%d: NO\n",cas);
        }
        else {
            printf("Case #%d: %d\n",cas,ans-minn);
        }
     //   if(cas>130)break;
    }
    
}

            
