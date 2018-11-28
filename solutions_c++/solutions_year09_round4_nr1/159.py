#include<iostream>
#include <cstring>
#include<algorithm>
#define _clr(x) memset(x, 0xff, sizeof(int) * n)
using namespace std;
int A[100][100],L[100],N;
int main()
{
    int T,CASE,i,j,ans,mk,tmp;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    
    for(CASE=1;CASE<=T;++CASE)
    {
        scanf("%d",&N);
          for(i=0;i<N;++i)
          {  for(L[i]=j=0;j<N;++j)
             { scanf("%1d",&A[i][j]);
               if(A[i][j])
                L[i]=j;
             }
             //printf("%d%c",L[i],i==N-1?'\n':' ');
           }
           ans=0;
          for(i=0;i<N;++i)
           { //printf("%d:",i);
           for(j=i;L[j]>i;++j);
          // printf("j=%d\n",j);
                     
           
          //  printf("%d %d\n",i,j);
            ans+=j-i;
            tmp=L[j];
            while(j!=i)
            {  L[j]=L[j-1];
             --j;
              }
             
           }
      
               
       
      printf("Case #%d: %d\n",CASE,ans);
    }
}
