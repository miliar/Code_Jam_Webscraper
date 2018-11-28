#include <iostream>
using namespace std;
int N;
int T;
long long K;
long long devices[1001];
long long offset[1001];
int main()
{
    int i;
    devices[0] = 1;
    devices[1] = 1;
    offset[1] = 4;
    for(i = 2; i <= 30; i++) 
    {
     devices[i] = devices[i - 1] + ((long long)(1) << (long long)(i - 1));
     offset[i] = offset[i-1]*(long long)(2);
   //  cout<<devices[i]<<" "<<offset[i]<<endl;
    }
    //powered[0] = 1;
    scanf("%d",&T);
    int tests;
    for(tests = 1; tests <= T; tests++)
    {
     //scanf("%d %d",&N,&K);
     cin>>N>>K;
     bool status = 0;
     for(int j = N; j <= 30; j++)
     {
     if(((K) - devices[j])%offset[j] == 0 && (K) >= devices[j]) {status = 1; printf("Case #%d: ON\n",tests); break;}
     }
     if(status == 0)
     printf("Case #%d: OFF\n",tests);
     
     /* for(i = 1; i <= K; i++)
      {
       int j;
       //memset(powered,0,sizeof(powered));
        int last = 1;
        for(j = 1; j <= N; j++)
         {
          if(devices[j] == 1)
           {
            devices[j] = 0;
        //    powered[j + 1] = 1;
            last = j + 1;
           }
           else 
            {
             break;
            }
         }
         devices[last] = 1;
     /*  for(j = 1; j <= N; j++)
        {
         cout<<devices[j]<<" ";
        }
        cout<<endl;
       */
       /*for(j = 1; j <= N; j++)
        {
         cout<<powered[j]<<" ";
        }
        cout<<endl;
       *       last = 0;
       for(j = 1; j <= N; j++)
        {
         if(devices[j] == 1) 
          last = j;
          else break;
        }  
       bla = last; 
       // cout<<i<<" ----> "<<last<<endl; 
      }
      if(bla == N) printf("Case #%d: ON\n",tests);
       else printf("Case #%d: OFF\n",tests);
     */
     }
    return 0;
}
