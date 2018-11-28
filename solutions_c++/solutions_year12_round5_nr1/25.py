#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<assert.h>
#include<stdarg.h>
#include<time.h>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;
struct XD{
    int l,p,i;
    bool operator<(const XD& b)const{
        int a1=l*b.p;
        int a2=b.l*p;
        return a1==a2?i<b.i:a1<a2;
    }
}in[1010];
int main(){
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        int n,i;
        scanf("%d",&n);
        for(i=0;i<n;i++)in[i].i=i;
        for(i=0;i<n;i++)scanf("%d",&in[i].l);
        for(i=0;i<n;i++)scanf("%d",&in[i].p);
        sort(in,in+n);
        printf("Case #%d:",cas++);
        for(i=0;i<n;i++)printf(" %d",in[i].i);
        puts("");
    }
}

