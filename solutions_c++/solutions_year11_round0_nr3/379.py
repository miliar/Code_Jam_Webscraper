#include <iostream> 
#include <sstream> 
#include <string> 
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
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 


int main()
{
  int run,runs;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++)
  {
    int n; printf("Case #%d: ",run);
    scanf("%d",&n);
    int laag=1000000000,som=0,x=0;
    for(int i=0;i<n;i++)
    {
      int j=0;
      scanf("%d",&j);
      laag = min(laag,j);
      som+=j; x^=j;
    }
    if(x==0)
      printf("%d\n",som-laag);
    else printf("NO\n");
    
  }



}






