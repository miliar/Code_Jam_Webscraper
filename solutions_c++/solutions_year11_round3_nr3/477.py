#include<iostream>
using namespace std;

#define MAXN 102

int f[MAXN];

int main()
{
//    freopen("C.in","r",stdin);
//    freopen("C.out","w",stdout);
    
    int t;
    cin>>t;
    int num=1;
    while(t--){
        int n,l,h;
        cin>>n>>l>>h;
        int i;
        for(i=0;i<n;i++)
           cin>>f[i];
        int k;
        for(k=l;k<=h;k++){
           int flag=1;
           for(i=0;i<n;i++)
             if(f[i]%k!=0&&k%f[i]!=0){
                flag=0;
                break;
             }
           if(flag) break;
        }
        if(k>h) printf("Case #%d: NO\n",num++);
        else printf("Case #%d: %d\n",num++,k);
    }
}
