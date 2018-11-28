#include <cstdio>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <map>
#include <vector>
#include <queue>

using namespace std;

#define FOR(i, x) for (int i = 0; i < x; i++)
#define FORI(i,a, x) for (int i = a; i < x; i++)
#define ALL(x) (x).begin(), (x).end()
#define FORE(i, x) for (__typeof__((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define INF 0x3F3F3F3F

#define MAX 500

int matches[MAX+1][21];

int main()
{
   freopen("in/C-large.in","r",stdin);
   freopen("out/C-large.out","w",stdout);
   
   int N, cnt;
   string text, find;
   
   find = "welcome to code jam@";
   
   getline(cin,text);
   sscanf(text.c_str(),"%d",&N);
   
   FOR(n,N)
   {      
      // Initialize
      cnt = 0;
      memset(matches,0,sizeof(matches));
      
      // Input
      getline(cin,text);
      text += "@";
      //cout << text << endl;

      FOR(i,SZ(text)) if(text[i]=='w') matches[i][1] = 1;

      // Process
      FOR(i,SZ(find)-1)
      {
         FOR(j,SZ(text))
         {
            //printf("%c (%d) = %c (%d)\n",find[i],i,text[j],j);
            if((text[j] == find[i]) && (matches[j][i+1]))
            {
               FORI(k,j+1,SZ(text))
               {
                  if(text[k] == find[i+1])
                  {
                     //printf("%c (%d) -> %c (%d)\n",text[j],j,text[k],k);
                     matches[k][i+2] = (matches[k][i+2]+matches[j][i+1])%10000;
                  }
               }
            }
         }
      }
      printf("Case #%d: %04d\n",n+1,matches[SZ(text)-1][20]);
   }
   
   return 0;
}
