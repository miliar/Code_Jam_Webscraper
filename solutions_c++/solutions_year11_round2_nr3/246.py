#include <vector>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
#define max(a,b)    (((a) > (b)) ? (a) : (b))
#define min(a,b)    (((a) < (b)) ? (a) : (b))
#define sqr(a)    ((a)*(a))

void main()
{
  ifstream is("a.in");
  ofstream os("a.out");

  int t;
  is>>t;
  for (int ti=0;ti<t;++ti)
  {
    int n,m;
    is>>n>>m;

    int u[5];
    int v[5];

    for (int i=0;i<m;++i)
      is>>u[i];
    for (int i=0;i<m;++i)
      is>>v[i];

    vector<set<int> > rooms;
    rooms.resize(1);
    for (int i=0;i<n;++i)
      rooms[0].insert(i);

    for (int i=0;i<m;++i)
    {
      int j0=u[i]-1;
      int j1=v[i]-1;
      if (j0>j1)
        swap(j0,j1);
      for (int j=0;j<rooms.size();++j)
        if (rooms[j].find(j0)!=rooms[j].end()&&rooms[j].find(j1)!=rooms[j].end())
        {
          rooms.resize(rooms.size()+1);
          bool second=false;
          for (set<int>::iterator it=rooms[j].begin();it!=rooms[j].end();)
          {
            if (*it==j0)
            {
              rooms.back().insert(*it);
              second=true;
              ++it;
            }
            else if (*it==j1)
            {
              rooms.back().insert(*it);
              break;;
            }
            else if (second)
            {
              rooms.back().insert(*it);
              rooms[j].erase(it++);
            }
            else
              ++it;
          }
          break;
        }
    }

    vector<int> c;
    vector<int> best;
    int best_num=1;
    c.resize(9,0);
    best=c;

    vector<vector<bool> > rooms_c;
    rooms_c.resize(rooms.size());
      
    for (;;)
    {
      c[0]++;
      for (int i=0;c[i]==5;++i)
      {
        c[i]=0;
        c[i+1]++;
      }

      if (c[n]==1)
        break;

      //check
      bool success=true;
      for (int i=0;i<rooms.size();++i)
      {
        rooms_c[i].clear();
        rooms_c[i].resize(5,false);
      }
      for (int i=0;i<rooms.size();++i)
      {
        for (set<int>::iterator it=rooms[i].begin();it!=rooms[i].end();++it)
        {
          rooms_c[i][c[*it]]=true;
        }
        if (i>0 && rooms_c[i-1]!=rooms_c[i])
        {
          success=false;
          break;
        }
      }
      if (success)
      {
        int nums=0;
        for (int i=0;i<5;++i)
          if (rooms_c[0][i])
            ++nums;

        if (nums>best_num)
        {
best_num=nums;
best=c;
        }
      }

    }

    
    //int c;

    os << "Case #"<<ti+1<<": "<<best_num<<"\n";
    for (int i=0;i<n;++i)
      os <<best[i]+1<<" ";
    os <<'\n';
  }
}

//void main()
//{
//  ifstream is("a.in");
//  ofstream os("a.out");
//
//  int t;
//  is>>t;
//  for (int ti=0;ti<t;++ti)
//  {
//    int n;
//    is>>n;
//    for (int i=0;i<n;++i)
//    {
//    }
//
//    os << "Case #"<<ti+1<<": "<<time<<"\n";
//  }
//}