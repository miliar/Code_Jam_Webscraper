#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int maxn = 20;
int len,a[maxn],b[maxn],limit,lef,rig,ans;
int use[2000009];

int nex(int x,int n){if (x==n) return 1; return x+1;}
void work(int num)
{
     for (int i=2; i<=len; i++)
     {
         int x = 0;
         for (int j=i; nex(j,len)!=i; j=nex(j,len))
             x = x*10 + a[j];
         x = x*10 + a[i-1];
         if (x > num && x <= rig && x >= lef) {
            ans++ ;use[x] = limit;
                                              }
     }
 }
int main()
{
   // freopen("C.in","r",stdin);
  //  freopen("C.out","w",stdout);
      int data; 
      scanf("%d\n",&data);
      for (int o=1; o<=data; o++)
      {
          scanf("%d %d\n",&lef,&rig);
          ans = 0; limit ++;
          for (int i=lef; i<=rig; i++)
        //   if (use[i]<limit)
           {
              len = 0; int x = i;
              while (x) {
                  b[++len] = x%10; x /= 10;
                         }
              for (int j=1; j<=len; j++)
                  a[j] = b[len-j+1];
              work(i);
           }
          printf("Case #%d: %d\n",o,ans);
      }
    return 0;
}
