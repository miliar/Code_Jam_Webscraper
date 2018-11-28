#include <stdio.h>
#include <memory.h> 
#include <map>
using namespace std;
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout); 
    map<long,char> mp;
    long i,j,a,b,p,r;
    long test,order,total,num,res;
    long cnt[1005]={0},fac[10]={1,10,100,1000,10000,100000,1000000};
    scanf("%ld",&test);
    for(order=1;order<=test;order++){
        mp.clear();
        scanf("%ld%ld",&a,&b);
        total=0;
        for(i=a;i<=b;i++){
            num=i,p=0;
            while(num!=0){
                num/=10;
                p++;
            }
            for(j=1;j<=p;j++){//3?
                num=i;
                r=num%fac[j];
                num/=fac[j];
                num+=r*fac[p-j];
                if(num>i&&num<=b){
                    res=i+num*fac[p];
                    if(mp[res]==0)
                        mp[res]++;
                    else{
                        //printf("res %ld\n",res);
                        continue;
                    }
                    total++;
                }
            }//for j
        }//for i
        printf("Case #%ld: %ld\n",order,total);
    }
    return 0;
}
