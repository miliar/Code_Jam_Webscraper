// using107@gmail.com

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int nCaseCnt = 0;
int nEngineCnt = 0;
char szEngineName[100][100];
char szQuery[100];
bool bEngineEnable[100];
int nQueryCnt;
int nLeftEngineCnt;

void resetEngine()
{
  for(int i = 0; i < nEngineCnt; i++)
    bEngineEnable[i] = true;
  nLeftEngineCnt = nEngineCnt;
}

int checkEngine()
{
  for(int i = 0; i < nEngineCnt; i ++)
  {
    if(bEngineEnable[i] == true){
    if(strcmp(szQuery, szEngineName[i]) == 0)
    {
      bEngineEnable[i] = false;
      nLeftEngineCnt--;
      return i;
    }}
  }
  return -1;
}

int result(ifstream& fin)
{
  int reset = 0;

  fin >> nEngineCnt;

  fin.get();

  for(int i = 0; i<nEngineCnt ; i ++)
  {
    fin.getline(szEngineName[i],100);
  }

  fin >> nQueryCnt;
  fin.get();

  // init reset
  resetEngine();

  for(int i = 0; i < nQueryCnt; i++)
  {
    // get Query
    fin.getline(szQuery,100);
    int curEngineIdx = checkEngine();
    if(nLeftEngineCnt == 0)
    {
      reset ++;
      resetEngine();
      nLeftEngineCnt--;
      bEngineEnable[curEngineIdx] = false;
    }
  }

  return reset;
}

int main(int argc, char* argv[])
{
  ifstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open("savingUniverse.out");
  
  if(!fin.is_open())
  {
    cout << " file is not opened" << endl;
    return 0;
  }

  fin >> nCaseCnt;

  for(int i = 0; i < nCaseCnt;i++)
  {
    fout << "Case #" << i+1 << ": " << result(fin) << endl;
  }

  fin.close();
  fout.close();
  return 0;
}