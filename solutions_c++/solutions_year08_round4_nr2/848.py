#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<int,int> pointPair;
typedef vector<pointPair> pointVec;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<string> stringVec;

struct MyKey
{
  int vals[3];
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

int calculateTriangles(pointVec &trees, int MyA)
{
  int res=0;
  memory.clear();
  vector<int> tri;
  tri.resize(3);
  int n=trees.size();
  int rA=-1,rB=-1,rC=-1;

  //for (int A=0;A<trees.size();A++)
  int A=0;
    for (int B=A+1;B<trees.size();B++)
      for (int C=B+1;C<trees.size();C++)
        {
        if (A!=B && B!=C && A!=C)
          {
            //abs((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3)) 
            long long area =abs(
            (trees[A].first-trees[B].first)*(trees[A].second-trees[C].second)-
            (trees[A].second-trees[B].second)*(trees[A].first-trees[C].first));
            if (area==(MyA))
            {
              rA=A;
              rB=B;
              rC=C;
              A=trees.size()+1;
              B=trees.size()+1;
              C=trees.size()+1;
              break;
            }
          }
      }
  
  if (rA==-1)
     printf("IMPOSSIBLE\n");
  else
    printf("%d %d %d %d %d %d\n",trees[rA].first,trees[rA].second,trees[rB].first,trees[rB].second,trees[rC].first,trees[rC].second);
  return res;
}

void main(int argc, char * argv[])
{
  char tempStr[4096];
  int caseCount=0;
  pointVec points;
  long long N,M,A;
  cin>>caseCount;
  for (int caseId=1;caseId<=caseCount;caseId++)
  {
    cin >> N >> M >> A;
    points.clear();
    for (int i=0;i<=N; i++)
      for (int j=0;j<=M; j++)
        points.push_back(pointPair(i,j));
    printf("Case #%d: ",caseId);
    int result=calculateTriangles(points,A);
  }
  //fclose(f);
}
