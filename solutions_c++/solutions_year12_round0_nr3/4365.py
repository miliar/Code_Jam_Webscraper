#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<set>
using namespace std;

int check(int num,int lowr,int uppr){
    int num1=num,num2=num,mul=1,ret=0;
    map <int,bool> mp;
    while(num1){
        mul*=10;
        num1/=10;
    }
    num1=num;
    mul/=10;
    while(num1){
        num2=(num1%10)*mul+(num2/10);
        if(num1%10 && num2>num && num2>lowr && num2<=uppr && mp[num2]==0){
            ++ret;
            mp[num2]=1;
        }
        num1/=10;
    }
    return ret;
}

main(){
    int t,Kase=1;
    scanf("%d",&t);
    while(t--){
        int a,b,ans=0;
        scanf("%d %d",&a,&b);
        for(int i=a;i<b;++i)
            ans+=check(i,a,b);
        printf("Case #%d: %d\n",Kase++,ans);
    }
    //system("pause");
    return 0;
}

