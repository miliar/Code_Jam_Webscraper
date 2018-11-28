#include<iostream>
using namespace std;

int cas;
int n;

struct p
{
       int x,y;
       bool operator<(const p &b)const
       {
            return b.x>x;
       }
}a[1005];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    for(int cnt=1;cnt<=cas;cnt++)
    {
         printf("Case #%d: ",cnt);
         
         int res=0;
         scanf("%d",&n);
         for(int i=0;i<n;i++) scanf("%d%d",&a[i].x,&a[i].y);
         sort(a,a+n);
     //    for(int i=0;i<n;i++) printf("%d %d\n",a[i].x,a[i].y);
         
         for(int i=0;i<n;i++)
         {
             for(int j=i+1;j<n;j++) 
                if(a[i].y>a[j].y) res++; 
         }
         printf("%d\n",res);
    }
    
    
    return 0;
} 
