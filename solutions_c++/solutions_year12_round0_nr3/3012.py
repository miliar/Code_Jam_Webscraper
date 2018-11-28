#include<cstdio>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<algorithm>
#include<iostream>
using namespace std;

int a,b;
int len;
int ppow[10]={0,10,100,1000,10000,100000,1000000};

int dis(int x,int y) {
    int temp1=x,temp2;
    int s=0;
    for(int i=1;i<=len;i++) {
        temp2=ppow[i];
        temp1=x%temp2;
        temp1=x/temp2+temp1*ppow[len-i];
        if(temp1>x&&temp1<=b&&temp1>=a){
                s++;
                //cout<<x<<" "<<temp1<<endl;
        }
    }
    return s;
}

int main() {
freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int Case,h=1;
    scanf("%d",&Case);
    while(Case--) {
        int sum,ans=0;
        scanf("%d%d",&a,&b);
        for(int i=a;i<=b;i++) {
             int temp=i;len=0;
             while(temp) {
                 len++;
                 temp/=10;
             }
             sum=dis(i,len);
             ans+=sum;   
        }
        printf("Case #%d: %d\n",h++,ans);
    }
    return 0;
}
        
