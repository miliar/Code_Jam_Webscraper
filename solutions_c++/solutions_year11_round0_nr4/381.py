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
  int i,j,k;
  char buf[200];
  int run,runs;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++)
  {
    printf("Case #%d: ",run);

    int n; 
    scanf("%d",&n); int q=n;
    for(i=1;i<=n;i++)
    {
      scanf("%d",&k);
      if(i==k) q--;
    }    
    printf("%d\n",q);
  }
}






