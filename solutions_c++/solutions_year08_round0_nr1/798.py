#include<iostream>
using namespace std;

int main()
{
    
    freopen("input2.txt","r",stdin);
    freopen("output3.txt","w",stdout);
    int N,S,Q,FLAG[110],ctr,C,i,j,k,Counter=0;
    char strS[110][110],strQ[1010][110];
    scanf("%d",&N);
    while (N)
    {
          C=0;
          Counter++;
          scanf("%d\n",&S);
          for (i=0;i<S;i++)
          {
              gets(strS[i]);
              scanf("\n");
          }
          for (k=0;k<S;k++)
              FLAG[k]=0;
          scanf("%d\n",&Q);
          for (i=0;i<Q;i++)
          {
              gets(strQ[i]);
              scanf("\n");
          }
          ctr=0;
          for (i=0;i<Q;i++)
          {
              for (j=0;j<S;j++)
              {
                  if(strcmp(strS[j],strQ[i])==0 && FLAG[j]==0)
                  {  
                                             ctr++;
                                             FLAG[j]=1;
                  }
                  if (ctr==S)
                  {
                               ctr=1;
                               C++;
                               for (k=0;k<S;k++)
                                   FLAG[k]=0;
                               FLAG[j]=1;
                  }
              }
          }       
          printf("Case #%d: %d\n",Counter,C);
          N--;  
    }
}
