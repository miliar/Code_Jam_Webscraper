#include<iostream>
using namespace std;
int A[100][100],S[10000],N,M;
char mk[100][100];
int find(int k)
{
    if(S[k]==k)
      return k;
      return S[k]=find(S[k]);
}
void uni(int i,int j)
{
    i=find(i);
    j=find(j);
    if(i<j)
      S[j]=i;
    else if(j<i)
      S[i]=j;
}
bool valid(int i,int j)
{
  return i>=0&&i<N&&j>=0&&j<M;     
}
int main()
{  int T,CASE,i,j,c,down,pi,pj,tmp;
   int di[4]={-1,0,0,1};
   int dj[4]={0,-1,1,0};
   freopen("B.in","r",stdin);
   freopen("B.out","w",stdout);
    scanf("%d",&T);    
    for(CASE = 1 ;CASE <=T; ++CASE)
    {   printf("Case #%d:\n",CASE);
        scanf("%d%d",&N,&M);
        for(i=0;i<N;++i)
          for(j=0;j<M;++j)
           {  scanf("%d",&A[i][j]);
            S[i*M+j]=i*M+j;
           }
        for(i=0;i<N;++i)
          for(j=0;j<M;++j)
           { pi=pj=-1;down=1000000;
           
           for(c=0;c<4;++c)
             if(valid(i+di[c],j+dj[c])
             &&A[i+di[c]][j+dj[c]]<A[i][j])
             {  
             if(A[i+di[c]][j+dj[c]]<down)
                 {
                   down=A[i+di[c]][j+dj[c]];
                       pi=i+di[c];
                       pj=j+dj[c];                  
                 }
                                           
             }
             if(down<1000000)
             uni(i*M+j,pi*M+pj);
           }     
           char now='a';
          for(i=0;i<N;++i)
          for(j=0;j<M;++j)
           { tmp=find(i*M+j);
            pi=tmp/M;
            pj=tmp%M;
             if(pi==i&&pj==j)
               mk[i][j]=now++;
             else
              mk[i][j]=mk[pi][pj];
             printf("%c%c",mk[i][j],j==M-1?'\n':' ');
                          
           }     
    
    }
}
