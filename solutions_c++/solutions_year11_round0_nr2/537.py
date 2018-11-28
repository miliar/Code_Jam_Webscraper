#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#define FOR(x,y,z) for(int x=y;x<z;x++)
#define FORD(x,y,z) for(int x=y; x>=z;x--)
#define max3(a,b,c) max(a,max(b,c))
#define PB push_back
#define F first
#define K(x) ((x)*(x))
#define mabs(x) max(x,-x)
#define S second
#define MP make_pair
#define inf 2000000000
using namespace std;

vector<pair<int,int> > OP,NB;
char S[110];
vector<char> OUT;
int main()
{
   int Z;
   scanf("%d",&Z);
   for(int z=1;z<=Z;z++)
   {
      int C,D,N;
      scanf("%d",&C);
      FOR(i,0,C)
      {
         scanf("%s",S);
         char c=S[2];
         NB.PB(MP(S[0]*1000+S[1],c));
         NB.PB(MP(S[1]*1000+S[0],c));
         S[0]=S[1]=S[2]='\0';
      }
      scanf("%d",&D);
      FOR(i,0,D)
      {
         scanf("%s",S);
         OP.PB(MP(S[0]*1000+S[1],inf));
         OP.PB(MP(S[1]*1000+S[0],inf));
         S[0]=S[1]=S[2]='\0';
      }
      sort(OP.begin(),OP.end());
      sort(NB.begin(),NB.end());
      OP.PB(MP(inf,'D'));
      NB.PB(MP(inf,'D'));
      scanf("%d",&N);
      scanf("%s",S);
      FOR(i,0,N)
      {
         OUT.PB(S[i]);
         if(OUT.size()>1)
         {
            pair<int,char> T=*(lower_bound(NB.begin(),NB.end(),MP(OUT[OUT.size()-1]*1000+OUT[OUT.size()-2],-255)));
            if(T.F==OUT[OUT.size()-1]*1000+OUT[OUT.size()-2])
            {
               OUT.pop_back();
               OUT.pop_back();
               OUT.PB(T.S);
            }
            FOR(q,0,OUT.size())
            {
               T=*(lower_bound(OP.begin(),OP.end(),MP(OUT.back()*1000+OUT[q],-255)));
               if(T.F==OUT.back()*1000+OUT[q])
               {
                  OUT.clear();
                  break;
               }
            }
         }
      }
      printf("Case #%d: [",z);
      FOR(i,0,OUT.size())
      {
         printf("%c",OUT[i]);
         if(i<OUT.size()-1)printf(", ");
      }
      printf("]\n");
      OP.clear();
      NB.clear();
      OUT.clear();
      FOR(i,0,N+4)S[i]='\0';
   }
   return 0;
}
