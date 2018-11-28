#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

int fq[10001];

int main(int argc,char **args)
{
  freopen("C-small-attempt2.in","r",stdin);
  freopen("C-small-attempt2.out","w",stdout);
  int testcase;
  cin>>testcase;
  for (int caseId=1;caseId<=testcase; caseId++)
  {
    printf("Case #%d: ",caseId);
    int N, L, H;
    cin>>N>>L>>H;
    for(int i=0; i<N; ++i)
    {
      cin>>fq[i];
    }
    /*for(int i=0; i<N; ++i)
      cerr<<fq[i]<<" ";
    cerr<<endl;*/
    
    bool found;
    int result = -1;
    for(int i=L; i<=H; ++i)
    {
      //cerr<<i<<" ";
      found = true;
      int j = 0;
      for(; j<N; ++j)
      {
        if(max(i, fq[j]) % min(i, fq[j]) != 0)
        {
          found = false;
        }
      }
      if(found)
      {
        result = i;
        break;
      }
    }
    
    if(result == -1)
    {
      cerr<<"NO"<<endl;
      cout<<"NO"<<endl;
    }
    else
    {
      cerr<<result<<endl;
      cout<<result<<endl;
    }
    fflush(stdout);
  }
  return 0;
}