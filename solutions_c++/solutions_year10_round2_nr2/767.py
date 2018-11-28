#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;
int c,t,D,I,N,M,K,B,T;
char s[200][200];
char w[200];
int vi[60];
int xi[60];
int tp[60];

int main()
{
   cin >> t;
   for(int p=0;p<t;p++)
   {
      cin >> N >> K >> B >> T;
      for(int i=0;i<N;i++)
      {
         cin >> xi[i];
      }
      for(int i=0;i<N;i++)
      {
         cin >> vi[i];
      }
      for(int i=0;i<N;i++)
      {
         tp[i]=(B-xi[i])/vi[i];
         if((B-xi[i])%vi[i])
          tp[i]++;
//          cout << tp[i] << " ";
      }
  //    cout << endl;
      int res=0;
      int i=N-1;
      int kk=0;
      int ok=1;

      for(int i=N-1;i>=0;i--)
      {
         if(tp[i]<=T)
         {
            kk++;
            if(kk==K)
               break;
            continue;
         }
         for(int j=i-1;j>=0;j--)
         {
            if(tp[j]>T)continue;
            for(int e=j;e<i;e++)
            {
               tp[e]=tp[e+1];
               res++;
            }
            kk++;
            break;

         }
         if(kk>=K)
          break;

      }
      if(kk<K)
         printf("Case #%d: IMPOSSIBLE\n",p+1);
      else
         printf("Case #%d: %d\n",p+1,res);
      
   }

   return 0;
}

      /*   cin >> N >> M;
         for(int i=0;i<N;i++)
         {
            cin >>s[i];
         }

         int res=0;
         for(int i=0;i<M;i++)
         {
            cin >> w;
            for(int j=0;j<N;j++)
            {
               for(int k=0;k<strlen(w);k++)
               {

               }
            }
         } */
