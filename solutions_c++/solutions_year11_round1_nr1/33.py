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
    return a<b;
}
int casN,n;
int main(){
    scanf("%d",&casN);
    int n,pg,pd,flag,gcd;
    for(int III=0;III<casN;III++){
        scanf("");
        scanf("%d%d%d",&n,&pd,&pg);
        flag=1;
        if(!pd)gcd=100;
        else gcd=std::__gcd(pd,100);
        if(100/gcd>n)flag=0;
        if(pd>0&&pg==0)flag=0;
        if(pd<100&&pg==100)flag=0;

        printf("Case #%d: %s\n",III+1,flag?"Possible":"Broken");
    }
    scanf(" ");
    return 0;
}

