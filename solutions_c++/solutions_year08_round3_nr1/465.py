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

using namespace std;

int main()
{
    int C;
    string s;
    getline(cin,s);
    sscanf(s.c_str(),"%i",&C);
    for(int _i=0;_i<C;_i++)
    {
       vector<long long> a;
       a.clear();
       int P,K,L;
       getline(cin,s);
       sscanf(s.c_str(),"%i %i %i",&P,&K,&L);
       getline(cin,s);
       istringstream iss(s,istringstream::in);
       for(int i=0;i<L;i++)
       {
          long long  tmp;
          iss >> tmp;
          a.push_back(tmp);
       }
       sort(a.begin(),a.end());
       reverse(a.begin(),a.end());
       int c=1;
       int b=1;
       long long ret=0;
       while(a.size()!=0)
       {
          if(c > K)
          {
              b++;
              c=1;
          }
          ret += a.front()*b;
          a.erase(a.begin());
          c++;
          if(b>P)
             break;
       }
       if(a.size()!=0)
          cout << "Case #" << _i+1 << ": " <<"Impossible" << endl;
       else cout << "Case #" << _i+1 << ": " << ret << endl;
    }
    return 0;
}

// Powered by FileEdit
