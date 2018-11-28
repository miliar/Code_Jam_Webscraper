#include<iostream>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    int t;
    cin>>t;
    int num=1;
    while(t--){
        int n,p1,p2;
        cin>>n>>p1>>p2;
        int res=0;
        if(p2==100){
           if(p1==100){
              printf("Case #%d: Possible\n",num++);
              continue;
           }
           else{
              printf("Case #%d: Broken\n",num++);
              continue;
           }
        }
        else if(p2==0){
                 if(p1==0){
                       printf("Case #%d: Possible\n",num++);
                       continue;
                 }
                 else{
                      printf("Case #%d: Broken\n",num++);
                      continue;
                 }
             }
             else{
                    int i;
                    for(i=1;i<=n;i++){
                        if(i*p1%100==0){
                           int m=i*p1/100;
                           if(p2>=m){res=1;break;}
                           else{
                              if(m*100%p2==0){res=1;break;}
                           }
                        }
                    }
                    if(res) printf("Case #%d: Possible\n",num++);
                    else printf("Case #%d: Broken\n",num++);
             }
    }
}
