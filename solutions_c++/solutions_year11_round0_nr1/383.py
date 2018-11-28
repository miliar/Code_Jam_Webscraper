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
    int n; scanf("%d",&n);
    int Bpos=1,Opos=1;
    int Btijd=0,Otijd=0;
    int tijd=0;
    for(j=0;j<n;j++)
    {
      scanf("%s",buf); scanf("%d",&k);
      char r=buf[0];
      if(r=='O')
      {
        Otijd=tijd=1+max(tijd,Otijd+abs(Opos-k));
        Opos=k;
      }
      else
      {
        Btijd=tijd=1+max(tijd,Btijd+abs(Bpos-k));
        Bpos=k;
      }

    }
    printf("%d\n",tijd);

  }
}






