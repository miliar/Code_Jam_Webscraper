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
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 

char buf[100000];
char buf2[100000];

int main()
{
  int i,j,k,l,m,n;
  scanf("%d",&n);
  for(m=1;m<=n;m++)
  {
    scanf("%d",&k);
    scanf("%s",buf); int bestrle=1000000;
    vi p; for(j=0;j<k;j++) p.pb(j);
    do
    {
      char laatst=-1; int rle=0; 
      for(i=0;buf[i];i++)
      {
        int basis=(i/k)*k; int erbij=i%k;
        char nu=buf[basis+p[erbij]];
        if(laatst!=nu) rle++;
        laatst=nu;
      }
      bestrle=min(bestrle,rle);
    } while(next_permutation(p.begin(),p.end()));
    printf("Case #%d: %d\n",m,bestrle);
  }
 
  return 0;
}

