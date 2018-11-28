#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

char CArray[30][30];
char DArray[30][30];

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N,C,D;
    string tmps;
    memset(CArray,0,sizeof(CArray));
    memset(DArray,0,sizeof(DArray));
    cin>>C;
    REP(i,C)
    {
      cin>>tmps;
      int c0 = tmps[0] - 'A';
      int c1 = tmps[1] - 'A';
      CArray[c0][c1] = CArray[c1][c0] = tmps[2];
    }
    cin>>D;
    REP(i,D)
    {
      cin>>tmps;
      int c0 = tmps[0] - 'A';
      int c1 = tmps[1] - 'A';
      DArray[c0][c1] = DArray[c1][c0] = 1;
    }
    cin>>N;
    vector<int > outst;
    cin>>tmps;
    int L = tmps.length();
    int c0;
    int c1;
    int index = 0;
    while(index < L)
    {
      outst.push_back(tmps[index] - 'A');
      index++;
      if(outst.size()==1)
      {
        if(index < L)
        {
          outst.push_back(tmps[index] - 'A');
          index++;
        }
        else break;
      }

      int size = outst.size();
      c1 = outst[size-1];
      c0 = outst[size-2];
      if(CArray[c0][c1]!=0)
      {
        outst.pop_back();
        outst.pop_back();
        outst.push_back(CArray[c0][c1] - 'A');
      }
      else
      {
        int cflag = 0;
        REP(i,outst.size())
        {
          if(DArray[outst[i]][c1]==1)
          {
            outst.clear();
            cflag = 1;
            break;
          }
        }
      }
    }
    string so = "[";
    REP(i,outst.size())
    {
      so += outst[i] + 'A';
      if(i<(int)outst.size() -1)so += ", ";
    }
    so += "]";

    cout<<"Case #"<<t<<": "<<so<<endl;
  }
  return 0;
}

