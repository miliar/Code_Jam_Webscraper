#include <iostream>
#include <sstream>  
#include <cstring>
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 

char V[600][600];


int main()
{
  int i,j,k;
  int a,b,c;

  int run,runs;
  scanf("%d",&runs);

  for(int kees=1;kees<=runs;kees++)
  {
    printf("Case #%d:",kees);

    int R,C,D;
    scanf("%d %d %d",&R,&C,&D);


    int best=-1;
    for(j=0;j<R;j++)
      scanf("%s",V[j]);

    int l,r,o,h,v;
    for(l=0;l<C;l++)
      for(r=l+2;r<C;r++)
        for(b=0;b<R;b++)
          {
            o=b+r-l;
            if(o>=R) continue;

            long long cx=l+r+1; //beoogde centrum
            long long cy=b+o+1;

            long long mx=0;
            long long my=0;

            for(h=l;h<=r;h++)
              for(v=b;v<=o;v++)
              {
                if(h==l&&(v==b||v==o)) continue;
                if(h==r&&(v==b||v==o)) continue;
                mx+=(V[v][h]+D)*(2*h+1-cx);
                my+=(V[v][h]+D)*(2*v+1-cy);
              }
            if(mx==0&&my==0)
            {
              best=max(best,o-b+1);
             // printf("o=%d b=%d l=%d r=%d\n",o,b,l,r);
            }
          }

    if(best==-1) printf(" IMPOSSIBLE\n");
    else printf(" %d\n",best);
  }




  return 0;
}
