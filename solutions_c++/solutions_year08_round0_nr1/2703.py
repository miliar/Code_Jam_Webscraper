#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

struct search
{
  vector<int> start;
  vector<int> end;
};

int main(void)
{
  struct search engine[102];
  int tcs;
  int ns, nq;
  vector<string> e;
  string name;
  int cases=0;

  ifstream fin("A-small-attempt4.in");
  ofstream fout("A-small-attempt4.txt");

  fin>>tcs;

  while(tcs--)
  {
    fin>>ns;
    fin.get();

    e.clear();
    for(int i=0; i<ns; ++i)
    {
      engine[i].start.clear();
      engine[i].end.clear();
      getline(fin,name,'\n');
      e.push_back(name);
    }

    fin>>nq;
    fin.get();
/*
    for(int i=0; i<ns; ++i)
    {
      engine[i].start.push_back(0);
      engine[i].end.push_back(0);
    }
*/
    for(int i=1; i<=nq; ++i)
    {
      getline(fin,name,'\n');

      for(int j=0; j<ns; ++j)
      {
        if(name.compare(e[j])==0)
        {
          int size1=engine[j].start.size();
          int size2=engine[j].end.size();
          if((size1-1)>=0&&size1==size2+1)
            engine[j].end.push_back(i-1);
        }
        else
        {
          int size1=engine[j].start.size();
          int size2=engine[j].end.size();
          if(size1==size2)
            engine[j].start.push_back(i);
        }
      }
    }
    for(int i=0; i<ns; ++i)
    {
      int size1=engine[i].start.size();
      int size2=engine[i].end.size();
      if(size1!=size2)
        engine[i].end.push_back(nq);
    }
/*
    for(int i=0; i<ns; ++i)
    {
      int size=engine[i].start.size();
      for(int j=0; j<size; ++j)
        cout<<engine[i].start[j]<<" "<<engine[i].end[j]<<endl;
      cout<<endl;
    }
*/
    int index, max=0;
    int count=-1;
    int start=1, end=1;
    while(start<=nq)
    {
      for(int i=0; i<ns; ++i)
      {
        int size=engine[i].start.size();
        for(int j=0; j<size; ++j)
          if(start>=engine[i].start[j]&&end<=engine[i].end[j])
          {
            if(max<engine[i].end[j])
            {
              index=i;
              max=engine[i].end[j];
            }
            break;
          }
      }
      start=end=max+1;
      ++count;
    }
    if(count==-1)  count=0;
    fout<<"Case #"<<++cases<<": "<<count<<endl;

  }

  return 0;
}
