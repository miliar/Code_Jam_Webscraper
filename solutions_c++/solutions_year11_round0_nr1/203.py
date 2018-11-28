#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
int n;
char s[10];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ca=1;ca<=cas;ca++){
        scanf("%d",&n);
        int lo=0,lb=0,po=1,pb=1,a;
        int res=0;
        for(int i=0;i<n;i++){
            scanf("%s%d",&s,&a);
            int tmp;
            if(s[0]=='O'){
                tmp = abs(a-po);
                res=max(res+1,tmp+lo+1);
                lo=res;
                po=a;
            }else{
                tmp = abs(a-pb);
                res=max(res+1,tmp+lb+1);
                lb=res;
                pb=a;
            }
        }
        printf("Case #%d: %d\n",ca,res);
    }
    return 0;
}
