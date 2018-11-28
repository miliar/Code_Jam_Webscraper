#include <stdio.h>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <algorithm>

using namespace std;

typedef pair<int,int>PII;
typedef pair<PII,int>PII2;



struct node{
    int val;
    int in[30];
}NODE[1005];

int sum[30];

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int Test;
    int n;
    int sum1=0;
    scanf("%d",&Test);
    for(int t=0;t<Test;t++){
        int MIN=2000000000;
        sum1=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            for(int j=0;j<30;j++) NODE[i].in[j] = 0;
            
        for(int i=0;i<n;i++){
            scanf("%d",&NODE[i].val);
            sum1+=NODE[i].val;
            MIN=min(MIN,NODE[i].val);
            int temp=NODE[i].val,x=0;
            while(temp){
                NODE[i].in[x++]=temp%2;
                temp/=2;
            }
        }
        for(int i=0;i<30;i++) sum[i]=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<30;j++) sum[j] = (sum[j]+NODE[i].in[j])%2;
        int ch=1;
        for(int i=0;i<30;i++) if(sum[i]) ch=0;
        if(ch==0) printf("Case #%d: NO\n",t+1);
        else printf("Case #%d: %d\n",t+1,sum1-MIN);

    }
return 0;
}
