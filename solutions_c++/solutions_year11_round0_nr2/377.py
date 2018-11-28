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
    printf("Case #%d: [",run);
    int C,D,N;
    scanf("%d",&C);
    map<pair<char,char>,char> combis;
    for(i=0;i<C;i++)
    {
      scanf("%s",buf);
      combis[make_pair(buf[0],buf[1])]=buf[2];
      combis[make_pair(buf[1],buf[0])]=buf[2];
    }
    vector<string> opposed(26);
    scanf("%d",&D);
    for(i=0;i<D;i++)
    {
      scanf("%s",buf);
      opposed[buf[0]-'A']+=buf[1];
      opposed[buf[1]-'A']+=buf[0];
    }
    scanf("%d",&N);
    scanf("%s",buf);

    vector<char> R;
    for(i=0;i<N;i++)
    {
      R.pb(buf[i]);


      while(sz(R)>=2)
      {
        pair<char,char> x;
        x.first=R[sz(R)-2]; x.second=R[sz(R)-1];
        if(combis.find(x)==combis.end())
          break;
        R.pop_back(); R.pop_back();
        R.pb(combis[x]); 
      }

      char L=R[sz(R)-1];
      for(int c=0;c<sz(opposed[L-'A']);c++)
      {
        char q = opposed[L-'A'][c];
        if(find(R.begin(),R.end(),q)!=R.end())
          R.clear();
      }
    }

    for(i=0;i<sz(R);i++)
      printf("%c%c%c",R[i],(i!=sz(R)-1)?',':']',(i!=sz(R)-1)?' ':'\n');
    if(sz(R)==0) printf("]\n");

  }
}






