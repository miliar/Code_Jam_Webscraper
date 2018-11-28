#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <string>
#include <iostream>


using namespace std;

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

int calculateSwitchesForSingleCase(stringVec &queries,stringVec &engines, 
                                   int currentEngineId,int currentQueryId,int switches, int depth)
{
  if (depth>0)
    switches++;

  for (unsigned int queryId=currentQueryId;queryId<queries.size();queryId++)
  {
    //cout << "Current Query:" << queries[queryId] << "\n";
    //cout << "Current Engine:" << engines[currentEngineId] << "\n";
    if (queries[queryId]==engines[currentEngineId])
    {
      //cout << "Switch:" << switches << "\n";
      unsigned int minSwitches=0x7FFFFFFF;
      unsigned int tempSwitches=0;
			unsigned int saveSwitches=switches;
      for (unsigned int engineId=0;engineId<engines.size();engineId++)
      {
        if (engineId!=currentEngineId)
        {
          MyKey key;
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
          if (minSwitches>tempSwitches)
            minSwitches=tempSwitches;
          //cout << "One branch:" << tempSwitches << "\n";
        }
      }
      switches+=(minSwitches-saveSwitches);
      return switches;
    }
  }
  return switches;
}


int calculateSwitches(stringVec &queries,stringVec &engines)
{
  unsigned int minSwitches=0x7FFFFFFF;
  unsigned int tempSwitches=0;
  for (unsigned int engineId=0;engineId<engines.size();engineId++)
  {
		memory.clear();
    tempSwitches=calculateSwitchesForSingleCase(queries,engines,engineId,0,0,0);
    if (minSwitches>tempSwitches)
            minSwitches=tempSwitches;
  }
  return minSwitches;
}

void main(int argc, char * argv[])
{
  char tempStr[4096];
  int caseCount=0;
  stringVec queries;
  stringVec engines;
  scanf("%d",&caseCount);

  for (int caseId=1;caseId<=caseCount;caseId++)
  {
    int engineCount=0;
    int queryCount=0;
    queries.clear();
    engines.clear();

    scanf("%d",&engineCount);
    engines.resize(engineCount);
    gets(tempStr); // skip first eof
    for (int engineId=0;engineId<engineCount;engineId++)
    {
      gets(tempStr);
      engines[engineId]=tempStr;
    }

    scanf("%d",&queryCount);
    queries.resize(queryCount);
    gets(tempStr); // skip first eof
    for (int queryId=0;queryId<queryCount;queryId++)
    {
      gets(tempStr);
      queries[queryId]=tempStr;
    }

    int result=calculateSwitches(queries,engines);
    printf("Case #%d: %d\n",caseId,result);
  }
  //fclose(f);
}
