#include <iostream>
#include <fstream>
#include <cmath>
#include <map>
#include <string>

using namespace std;

const int TEST_NUM = 20;
const int NAME_LEN = 256;
const int SEARCH_NUM = 100;
const int QUERY_NUM = 1000;

int main(int argc, char ** argv)
{
  if(argc!=2)
  {
    cout<<"Usage ./<program> inFilePath"<<endl<<endl;
    return 0;
  }

  char inPath[256];
  strcpy(inPath, argv[1]);

  /* INPUT */
  ifstream in(inPath, ios::in);
  int num=0;
  char ch;
  in>>num;
  in.get(ch);
  while(in.good() && ch!='\n') { in.get(ch); }

  for(int casei=0; casei<num; casei++)
  {
    map<string,int> mymap;
    map<string,int>::iterator it;
    int snum=0;
    in>>snum;
    in.get(ch);
    while(in.good() && ch!='\n') { in.get(ch); }
    for(int i=0; i<snum; i++)
    {
      char tmpChs[NAME_LEN];
      in.getline(tmpChs, NAME_LEN);
      string tmpstr=tmpChs;
      mymap[tmpstr]=i;
    }

    int query[QUERY_NUM]={0};
    int qnum=0;
    in>>qnum;
    in.get(ch);
    while(in.good() && ch!='\n') { in.get(ch); }
    if(qnum==0) {
      cout<<"Case #"<<(casei+1)<<": 0"<<endl;
      continue;
    }
    for(int i=0; i<qnum; i++)
    {
      char tmpChs[NAME_LEN];
      in.getline(tmpChs, NAME_LEN);
      string tmpstr=tmpChs;
      query[i]=mymap.find(tmpstr)->second;
    }

    /* CODING */
    int i=0;
    int swit=0;
    while(i<qnum)
    {
      int j;
      for(j=i; j<qnum; j++)
      {
        //cout<<j<<endl;
        int idx[SEARCH_NUM]={0}; 
        for(int n=i; n<=j; n++) idx[query[n]]++;
        int m;
        for(m=0; m<snum; m++) 
          if(idx[m]==0) { 
            break;
          }
        if(m==snum) {
          swit++;
          i=j;
          break;
        }
      }
      if(j==qnum) break;
    }
    
    cout<<"Case #"<<(casei+1)<<": "<<swit<<endl;
  }
  in.close();

  return 1;
}


