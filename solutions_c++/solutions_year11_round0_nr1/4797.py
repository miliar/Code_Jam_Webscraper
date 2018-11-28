#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
struct node
{
       int id;
       int tim;
}r,b;
int main()
{
    int t,ca=0,n;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
         r.id=1,b.id=1,
         r.tim=b.tim=0;
         char ch[5];int x;
         scanf("%d",&n);
         for(int i=0;i<n;i++)
         {
              scanf("%s%d",ch,&x);
              if(ch[0]=='B'){
                               int tmp=abs(b.id-x);
                               b.id=x;
                               if(b.tim+tmp+1>r.tim)b.tim+=tmp+1;
                               else b.tim=r.tim+1;
                             }
              else {
                     int tmp=abs(r.id-x);
                     r.id=x;
                     if(r.tim+tmp+1>b.tim)r.tim+=tmp+1;
                     else r.tim=b.tim+1;
                   }
              
         }
         int Max=max(r.tim,b.tim);
         printf("Case #%d: %d\n",++ca,Max);
    }
    //system("pause");
}
