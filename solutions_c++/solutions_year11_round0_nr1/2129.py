#include<cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
struct P
{
    int id,pos;
}a[210];
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--){
        int n;
        char op[5];
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%s%d",op,&a[i].pos);
            if(op[0]=='O') a[i].id=0;
            else a[i].id=1;
            //printf("%d %d %d\n",i,a[i].id,a[i].pos);
        }
        int pos[2],time[2],tol=0;
        pos[0]=pos[1]=1;
        time[0]=time[1]=0;
        for(int i=0;i<n;i++){
            tol++;
            int tmp=abs(pos[a[i].id]-a[i].pos)+1+time[a[i].id];
            if(tol<tmp) tol=tmp;
            time[a[i].id]=tol;
            pos[a[i].id]=a[i].pos;
        }
        printf("Case #%d: %d\n",++ca,tol);
    }
}
