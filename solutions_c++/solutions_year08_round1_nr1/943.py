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

using namespace std;

int main()
{
    int N;
    string s;
    getline(cin,s);
    sscanf(s.c_str(),"%i\n",&N);
    vector<int> v[2];
    
    for(int i=0;i<N;i++)
    {
       long long ret=0;
       int n;
       v[0].clear(),v[1].clear();
       getline(cin,s);
       sscanf(s.c_str(),"%i\n",&n);
       for(int j=0;j<2;j++)
       {
             int tmp;
             getline(cin,s);
             istringstream iss(s,istringstream::in);
             for(int k=0;k<n;k++)
             {
             iss >> tmp;
             v[j].push_back(tmp);
             }
          }
       sort(v[0].begin(),v[0].end());
       reverse(v[0].begin(),v[0].end());
       sort(v[1].begin(),v[1].end());
       for(int j=0;j<n;j++)
          ret += v[0][j]*v[1][j];
       cout <<"Case #" << i+1 << ": " << ret << endl;
    }
    return 0;
}
