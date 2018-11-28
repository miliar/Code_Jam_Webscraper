#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;


int t,P,Q,x,i,j,res,opt;
bool can[105];
vector<int> tab;

int main()
{
scanf("%d",&t);

for(i=1; i<=t; ++i)
     {
     scanf("%d %d",&P,&Q);
     tab.clear();
     for(j=0; j<Q; ++j)
          {
          scanf("%d",&x);
          tab.push_back(x);
          }
          
     opt=1000000000;
          
     do
          {
          for(j=1; j<=P; ++j) can[j]=true;
          can[0]=can[P+1]=false;
          res=0;
          
          for(j=0; j<tab.size(); ++j)
               {
               int l=tab[j],r=tab[j];
               can[tab[j]]=false;
               while(can[l-1]) --l;
               while(can[r+1]) ++r;
               res+=(r-l);
               }
          opt=min(opt,res);
          }
     while(next_permutation(tab.begin(),tab.end()));
     
     printf("Case #%d: %d\n",i,opt);
     }
     
return 0;
}
