using namespace std;
#include <cstdio>
#include <cstring>

#define Lmax 64

int N,nn;
int L,i,j,k,r2,r3,r5,r7;
char S[Lmax];

long long R2[Lmax][Lmax],R3[Lmax][Lmax],R5[Lmax][Lmax],R7[Lmax][Lmax];
long long A[Lmax][2][3][5][7],tot; 

int main()
{
 freopen("b.in","r",stdin);
 freopen("b.out","w",stdout);
 scanf("%d\n",&N);
 
 for (nn=1; nn<=N; ++nn)
     {
      fgets(S,Lmax-1,stdin);      
      L=strlen(S);
      if (S[L-1] == '\n') --L;
      memset(A,0,sizeof(A));
      //compute the remainers      
      for (i=0;i<L;++i)
          for (j=i; j<L; ++j)
              {
               R2[i][j] = R3[i][j] = R5[i][j] = R7[i][j] = 0;
               if (j>i)
                {
                    R2[i][j] = (R2[i][j-1] * 10 + S[j]-'0') & 1;
                    R3[i][j] = (R3[i][j-1] * 10 + S[j]-'0') % 3;
                    R5[i][j] = (R5[i][j-1] * 10 + S[j]-'0') % 5;
                    R7[i][j] = (R7[i][j-1] * 10 + S[j]-'0') % 7;
                }
               else {
                    R2[i][j] = (S[i]-'0') & 1;
                    R3[i][j] = (S[i]-'0') % 3;
                    R5[i][j] = (S[i]-'0') % 5;
                    R7[i][j] = (S[i]-'0') % 7;
                   }                   
              }
      //dinamic programming      
      for (i=0;i<L;++i)        
          {
          //if only one number
          A[i][R2[0][i]][R3[0][i]][R5[0][i]][R7[0][i]]=1;
          //add or subtract the number from j+1 to i
          for (j=0;j<i;++j)
              {
               for (r2=0;r2<2;++r2)
                   for (r3=0;r3<3;++r3)
                       for (r5=0;r5<5;++r5)
                           for (r7=0;r7<7;++r7)
                               {
                                A[i][ (r2+R2[j+1][i]) & 1 ][ (r3+R3[j+1][i]) % 3 ][ (r5+R5[j+1][i]) % 5 ][ (r7+R7[j+1][i]) % 7 ] += A[j][r2][r3][r5][r7];
                                A[i][ (10+r2-R2[j+1][i]) & 1 ][ (27+r3-R3[j+1][i]) % 3 ][ (25+r5-R5[j+1][i]) % 5 ][ (49+r7-R7[j+1][i]) % 7 ] += A[j][r2][r3][r5][r7];                                
                               }
              }
          }
      //compute
      tot=0;      
      for (r2=0;r2<2;++r2)
        for (r3=0;r3<3;++r3)
           for (r5=0;r5<5;++r5)
              for (r7=0;r7<7;++r7)
                 if (r2*r3*r5*r7==0) tot+=A[L-1][r2][r3][r5][r7];                  
      //print
      printf("Case #%d: %lld\n",nn,tot);
     }     
 return 0;
}
