#include<iostream>
#include<queue>
#include<set>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
using namespace std;
#define eps 1e-8
#define QQ system("pause");
#define zero(x) (((x)>0?(x):-(x))<eps)
#define pi acos(-1.0)
int a[1008];
int main(){
   // freopen("C-small-attempt0.in","r",stdin);
    int t,n,w=0;
    cin>>t;
    while(t--){
        cin>>n;
        int s=0;
        int ans=0;
        int maxn=10000008;
        for(int i=1;i<=n;i++){
           cin>>a[i]; 
           s=s^a[i];
           ans+=a[i];
           if(a[i]<maxn) maxn=a[i];
        }
        if(s!=0) printf("Case #%d: NO\n",++w);
        else{
            printf("Case #%d: %d\n",++w,ans-maxn);
        }
    }
   // while(1);
}
