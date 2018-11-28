#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<string> stringVec;

struct MyKey
{
  int vals[4];
  bool operator()(const MyKey& s1, const MyKey& s2) const
  {
    return memcmp(s1.vals,s2.vals,sizeof(vals)) < 0;
  }
};

map<MyKey, int, MyKey> memory;

/*MyKey key;
          key.vals[0]=engineId;
          key.vals[1]=queryId;
          key.vals[2]=switches;
          key.vals[3]=depth+1;
          map<MyKey, int, MyKey>::iterator cur  = memory.find(key);
          if (cur!=memory.end())
          {
            tempSwitches=cur->second;
          }
          else
          {
            tempSwitches=calculateSwitchesForSingleCase(queries,engines,engineId,queryId,switches,depth+1);
            memory[key]=tempSwitches;
          }		
    sort(array1.begin(), array1.end());
		sort(array2.begin(), array2.end(), greater<long long>());
          */

int getPerfectDec(int K,vi &cardIdx)
{
  list <int> deck;
  vi deckVec;
  int cnt=K;
  deck.push_back(K);
  for (int card=(K-1);card>=1;card--)
  {
    while(cnt>1)
    {
      int temp=deck.back();
      deck.pop_back();
      deck.push_front(temp);
      cnt--;
    }
    deck.push_front(card);
    cnt=card;
  }
  
  deckVec.resize(deck.size());
  int size=deck.size();
  for (int i=0;i<size;i++)
  {
    deckVec[i]=deck.front();
    deck.pop_front();
  }

  for (int i=0;i<cardIdx.size();i++)
  {
    printf(" %d",deckVec[cardIdx[i]-1]);
  }
  return 0;
}

void main(int argc, char * argv[])
{
  char tempStr[4096];
  int caseCount=0;
  scanf("%d",&caseCount);
  vi cardIdx;

  for (int caseId=1;caseId<=caseCount;caseId++)
  {
    int K=0;
    cardIdx.clear();
    scanf("%d",&K);
    int idxCount;
    scanf("%d",&idxCount);
    for (int idx=0;idx<idxCount;idx++)
    {
      int gotIdx;
      scanf("%d",&gotIdx);
      cardIdx.push_back(gotIdx);
    }
    printf("Case #%d: ",caseId);
    int result=getPerfectDec(K,cardIdx);
    printf("\n",caseId,result);
  }
  //fclose(f);
}
