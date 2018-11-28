#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
using namespace std;
int cc[1001];
__int64 dd[1000001];
int main()
{
    freopen("B-large(2).in","r",stdin);
    freopen("b.l.out","w",stdout);
    int Total;
    int i,j;
    scanf("%d",&Total);
    for(int Case=1;Case<=Total;Case++){
        printf("Case #%d: ",Case);
        int l,n,c;__int64 t;
        scanf("%d%I64d%d%d",&l,&t,&n,&c);
        for(i=0;i<c;i++)scanf("%d",cc+i);
        __int64 tc=0;bool f=1;
        int ind=0;
        for(i=1;i<=n;i++){
            int dis=cc[(i-1)%c]; 
            tc+=dis*2;
            if(!f)dd[ind++]=dis;
            if(f&&tc>t){
                dd[ind++]=(tc-t)/2;
                f=0;
            }
        }
        sort(dd,dd+ind);
        for(i=ind-1;i>=0&&i>=ind-l;i--){
            tc-=dd[i];                                
        }
        printf("%I64d\n",tc);
    }
        
}
