#include<iostream>
int main( int argc, char* argv[])
{
    int N, T, flag, i, j, sean, pat, max, up, sum, candy[20];
    scanf("%d",&T);
    for( int tc=1;tc<=T;++tc)
    {
         scanf("%d",&N);
         for( i=0;i<N;++i)
              scanf("%d",&candy[i]);
         
         up=(1<<N);
         max=flag=0;
         for( i=1;i<up-1;++i)
         {
              sean=pat=sum=0;
              for( j=0;j<N;++j)
              {
                   if( i&(1<<j))
                   {
                       sean^=candy[j];
                       sum+=candy[j];
                   }
                   else
                       pat^=candy[j];
              }
              if( sean==pat && sum>max)
              {
                  flag=1;
                  max=sum;
              }
         }
         printf("Case #%d: ",tc);
         if( flag)
             printf("%d\n",max);
         else
             printf("NO\n");
    }
    return 0;
}
