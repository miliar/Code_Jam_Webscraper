#include<iostream>
using namespace std;
int a[200],b[200];
int c[200][2];
int p1,p2,i,j,k,l,m,n,xys,ysc,n1,n2,x,y;
int abs(int x){if (x<0) return -x; else return x;}
void mov1(int ll)
{
     if (abs(p1-a[x])<=ll) p1=a[x]; else {if (a[x]<p1) p1-=ll; else p1+=ll;}
}
void mov2(int ll)
{
     if (abs(p2-b[y])<=ll) p2=b[y]; else {if (b[y]<p2) p2-=ll; else p2+=ll;}
}
int main()
{
  
    scanf("%d",&ysc);
    for (xys=1;xys<=ysc;++xys){
        scanf("%d",&n);
        p1=p2=1;
        n1=n2=0;
        char st[2];
        for (i=1;i<=n;++i){
            scanf("%s%d",st,&k);
            if (st[0]=='O'){
               c[i][0]=0;
               a[++n1]=k;
            } else {
               c[i][0]=1;
               b[++n2]=k;
            }
            c[i][1]=k;
        }
        x=1;y=1;int ans=0;
        for (i=1;i<=n;++i){
            int tim;
            if (c[i][0]==0){
               tim=abs(p1-c[i][1]);
               mov1(tim);
               mov2(tim+1);
               ans+=tim+1;
               ++x;
            } else {
               tim=abs(p2-c[i][1]);
               mov1(tim+1);
               mov2(tim);
               ans+=tim+1;
               ++y;
            }
        }
        printf("Case #%d: %d\n",xys,ans);
    }
    return 0;
}
