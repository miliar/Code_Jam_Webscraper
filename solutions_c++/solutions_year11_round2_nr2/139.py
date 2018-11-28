#include<iostream>
#include<algorithm>
#include<cmath>
#include<iomanip>
using namespace std;
struct node
{
       int x,y;
}s[1<<20];
bool operator<(const node&a,const node&b)
{
     return a.x<b.x;
}
//int a[1000000],b[1000000];
inline bool check(long double x,int m,int n)
{
         long double left = s[0].x-x;
         long double right = left+(s[0].y-1.0)*n;
         if(right>s[0].x+x)return 0;
         for(int i=1;i<m;i++){
                 left = right +n;
                 long double l = s[i].x-x;
                 if(l>left )left = l;
                 if(left>s[i].x+x)return 0;
                 right = left+(s[i].y-1.0)*n;
                 if(right>s[i].x+x)return 0;
                 }
return 1;
}
int sta[1000];
void out(long double x)
{
     if(x>=1e6)
     {
               int y = (int)(x/1e6);
               printf("%d",y);
               double z=x-y*1e6L;
               if(z<100000)printf("0");
               if(z<10000)printf("0");
               if(z<1000)printf("0");
               if(z<100)printf("0");
               if(z<10)printf("0");
               printf("%.7lf\n",z);
     }else
     {
          
          printf("%.6lf\n",(double)x);}
}
int main()
{
    freopen("b1.txt","r",stdin);
    freopen("b2.txt","w",stdout);
    //out(1e12+1e3);
    int cas;
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++)
    {
      //      cout<<cas<<endl;
      int m,n;
      scanf("%d%d",&m,&n);
    //  cout<<m<<" "<<n<<endl;
      for(int i=0;i<m;i++)
      {
              scanf("%d%d",&s[i].x,&s[i].y);
         //     cout<<s[i].x<<" "<<s[i].y<<endl;
      }
      sort(s,s+m);
    long double head = 0,tail = 1e12;
      while(fabs(tail-head)>1e-7)
      {
         long double  mid = (tail+head)/2;
        // cout<<head<<" "<<tail<<endl;
         if(check(mid,m,n))
         tail = mid;
         else
         head = mid;
      }
      //   cout<<head<<" "<<tail<<endl;
      printf("Case #%d: ",ii);
      out((head+tail)/2);
      
    }
    
    return 0;
}
