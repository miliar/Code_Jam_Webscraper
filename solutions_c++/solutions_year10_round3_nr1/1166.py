#include "iostream"

using namespace std;
struct wind{
       int a;
       int b;
}s[1001];
int cmp(const void *p1 , const void *p2)
{
    struct wind *pp1 = (wind *)p1;
    struct wind *pp2 = (wind *)p2; 
    return pp1->a - pp2->a;
}
int main()
{
     freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);
     int test , n;
     scanf("%d",&test);
     for(int t = 1 ;t <= test ; t++)
     {
         int cunt = 0;
         scanf("%d",&n);
         for(int i = 0 ; i < n ;i++)
         {
              scanf("%d%d",&s[i].a,&s[i].b);
             //  printf("%d %d\n",s[i].a,s[i].b);
         }
         qsort(s , n , sizeof(s[0]),cmp);
      //   for(int i = 0 ; i < n ;i++)
       //    printf("%d %d\n",s[i].a,s[i].b);
         for(int i = 0 ; i < n ;i++)
         {
             for(int j = i + 1; j < n ;j++)
             {
                   if(s[j].b < s[i].b)
                      cunt++;
             }
         }
         printf("Case #%d: %d\n",t , cunt);
     }
  //   while(1);
     return 0;
}           
