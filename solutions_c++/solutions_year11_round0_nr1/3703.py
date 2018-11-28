#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    int t,cnt,n,i,to,tb,pos,poso,posb,tmp;
    char ch[3];
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++){
        to=tb=0;
        poso=posb=1;
        scanf("%d",&n   );
        for(i=0;i<n;i++){
            scanf("%s%d",ch,&pos);
            if(ch[0]=='O'){
                tmp=to+abs(pos-poso)+1;
                if(tmp>tb)to=tmp;
                else to=tb+1;
                poso=pos;
            }
            else{
                tmp=tb+abs(pos-posb)+1;
                if(tmp>to)tb=tmp;
                else tb=to+1;
                posb=pos;
            }
        }
        printf("Case #%d: ",cnt);
        if(ch[0]=='O')printf("%d\n",to);
        else printf("%d\n",tb);
    }
    return 0;
}