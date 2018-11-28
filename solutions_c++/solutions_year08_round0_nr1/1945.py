#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <strstream> 

using namespace std;

int ImplodeTheEngines(int SearchEngineNum, string SearchEngines[], int QueryNum, string Querys[]) ;
int DieSearchEngine(int SearchEngineNum, string SearchEngines[], string Query, int alivedEngine[]);
bool allDied(int alivedEngine[], int SearchEngineNum);
void rebirth(int alivedEngine[], int SearchEngineNum);
void rebirthbut(int* alivedEngine, int SearchEngineNum, int but);

int main(int argc, char *argv[])
{
  ifstream filein("A-small-attempt5.in");
  ofstream oFile( "a.out" );
  string casesin, SearchEngineNumin, QueryNumin;
  int cases, SearchEngineNum, QueryNum;
  getline(filein, casesin);
  cases = atoi(casesin.c_str());
//  cout << cases << endl;
  for (int i = 0; i < cases; i++)
  {
    getline(filein, SearchEngineNumin);
    SearchEngineNum = atoi(SearchEngineNumin.c_str());
//    cout << SearchEngineNum << endl;
    string *SearchEngines =  new string[SearchEngineNum];
    for(int j = 0; j < SearchEngineNum; j++)
    {
        getline(filein, SearchEngines[j]);
//        cout << SearchEngines[j] << endl;
    }
    getline(filein, QueryNumin);
    QueryNum = atoi(QueryNumin.c_str());
//   cout << QueryNum << endl;
    string* Querys=  new string[QueryNum];
    for(int j = 0; j < QueryNum; j++)
    {        
        getline(filein, Querys[j]);
//        cout << Querys[j] << endl;
    }
    int times = ImplodeTheEngines(SearchEngineNum, SearchEngines, QueryNum, Querys);
    oFile << "Case #"<< i + 1 << ": "<<times << endl;
  }
  filein.close();
  system("PAUSE");	
  return 0;
}

int ImplodeTheEngines(int SearchEngineNum, string SearchEngines[], int QueryNum, string Querys[]) 
{
    int alivedEngine[SearchEngineNum];// = new int [SearchEngineNum];
    int switchcount = 0;
    for(int i = 0; i< SearchEngineNum;i++)
        alivedEngine[i] = 0;
    for(int i = 0;i < QueryNum; i++)
    {
        int pos = DieSearchEngine(SearchEngineNum, SearchEngines, Querys[i],alivedEngine);
        if(pos >= 0)
                alivedEngine[pos] = -1;
       /* if(allDied(alivedEngine, SearchEngineNum))
        {
           rebirth(alivedEngine, SearchEngineNum);
           switchcount++;
        }*/
        if(allDied(alivedEngine, SearchEngineNum))
        {
           rebirthbut(alivedEngine, SearchEngineNum, pos);
           switchcount++;
        }
    }
    return switchcount;
}

int DieSearchEngine(int SearchEngineNum, string SearchEngines[], string Query, int alivedEngine[])
{
    for(int i = 0; i< SearchEngineNum; i++)
    {
        if(alivedEngine[i] == -1)
                continue;
        if(SearchEngines[i] == Query)
                return i;
    }
    return -1;
}

bool allDied(int alivedEngine[], int SearchEngineNum)
{
    for(int i = 0; i< SearchEngineNum; i++)
    {
        if(alivedEngine[i] == 0)
                return false;
    }
    return true;
}

void rebirth(int* alivedEngine, int SearchEngineNum)
{
    for(int i = 0; i< SearchEngineNum; i++)
    {
       alivedEngine[i] = 0;
    }
}

void rebirthbut(int* alivedEngine, int SearchEngineNum, int but)
{
    for(int i = 0; i< SearchEngineNum; i++)
    {
       alivedEngine[i] = 0;
    }
    alivedEngine[but] = -1;
}

