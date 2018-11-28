#include<iostream>
using namespace std;
main()
{
      long long int i,t,N,K,a[33];
      long long int val;
      cin>>t;
      a[0]=1;
      for(i=1;i<=31;i++)
      {
          a[i]=a[i-1]*2;           
      }
      //printf("%d",sizeof(long int));
      int cnt=0;
      while(t--)
      {  
                
          //printf(" t is : %lld", t);
          cnt++;
          cin>>N>>K;
        //  printf(" N K is : %lld %lld\n", N, K);
          val = K%a[N];
        //  printf(" N K val is : %lld %lld %lld\n", N, K, val);
          if(val != a[N]-1)
            printf("Case #%d: OFF\n",cnt);
          else
            printf("Case #%d: ON\n",cnt);
      
      }
}
