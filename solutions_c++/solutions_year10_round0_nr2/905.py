#include <iostream>
const int maxn=1000;
typedef int list[maxn];
list a[2000],r,s1,s2,s0;
int n;
char s[maxn];
void get(list &s0)
{
     scanf("%s",s);
     s0[0]=strlen(s);
     for (int i=1;i<=s0[0];i++) s0[i]=s[s0[0]-i]-'0';
     memset(s,0,s0[0]);
}
int cmp(int l,list const &x,list const &y)
{
    int i;
    if (x[0]>y[0]+l) return 1;
    if (x[0]<y[0]+l) return -1;
    for (i=y[0];i>0;i--)
    if (x[i+l]!=y[i]) break;
    if (!i) return 0;
    if (x[i+l]>y[i]) return 1;
    if (x[i+l]<y[i]) return -1;
}
void dec(int l,list const &x,list const &y,list &z)
{
     int i;
     if (cmp(l,x,y)==-1)
     {
           memmove(s2,x,(x[0]+1)<<2);
           memmove(s1,y,(y[0]+1)<<2);
     } else
     {
           memmove(s1,x,(x[0]+1)<<2);
           memmove(s2,y,(y[0]+1)<<2);
     }
     memmove(s0,s1,(s1[0]+1)<<2);
     for (i=1;i<=s2[0];i++)
     {
         s0[i+l]-=s2[i];
         if (s0[i+l]<0)
         {
                     s0[i+l]+=10;
                     s0[i+1+l]--;
         }
     }
     while (s0[i+l]<0)
     {
           s0[i+l]+=10;
           s0[(++i)+l]--;
     }
     s0[0]=s1[0];
     while ((!s0[s0[0]])&&(s0[0]>0)) s0[0]--;
     memset(z,0,sizeof(z));
     memmove(z,s0,(s0[0]+1)<<2);
}
void mod(list const &x,list const &y,list &z)
{
     int l;
     memmove(s1,x,(x[0]+1)<<2);
     memmove(s2,y,(y[0]+1)<<2);
     l=s1[0]-s2[0];
     while ((l>0)||(((cmp(l,s1,s2))>=0)&&(l==0)))
           if (cmp(l,s1,s2)>=0) dec(l,s1,s2,s1);
                           else l--;
     memset(z,0,sizeof(z));
     memmove(z,s1,(s1[0]+1)<<2);
}
int main()
{
    int cc,i,ci;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&cc);
    for (ci=1;ci<=cc;ci++)
    {
        scanf("%d",&n);
        for (i=1;i<=n;i++) get(a[i]);
        dec(0,a[1],a[2],a[0]);
        if (!a[0][0])
        {
                     for (i=3;i<=n;i++)
                     {
                         dec(0,a[i],a[1],a[0]);
                         if (a[0][0]) break;
                     }
                     if (!a[0][0]) 
                     {
                                   printf("Case #%d: 0\n",ci);
                                   continue;
                     }
        }
        for (i=2;i<n;i++)
        {
            dec(0,a[i],a[i+1],a[i]);
            for (mod(a[i],a[0],r);r[0];mod(a[i],a[0],r))
            {
                  memmove(a[i],a[0],(a[0][0]+1)<<2);
                  memmove(a[0],r,(r[0]+1)<<2);
            }
        }
        mod(a[1],a[0],r);
        if (r[0]) dec(0,a[0],r,r);
        printf("Case #%d: ",ci);
        if (!r[0]) printf("0\n");
        else
        {
            for (i=r[0];i>0;i--) printf("%d",r[i]);
            printf("\n");
        }
    }
}
