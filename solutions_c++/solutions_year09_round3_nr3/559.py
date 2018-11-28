#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>

using namespace std;
typedef long long ll;

ll sovle(int p, int q, vector<int> real, vector<int> per)
{
  if (real.size() <= 0)
    return 0;

  ll temp;
  ll result = LLONG_MAX;
  for (int i = 0; i < real.size(); i++) {
    temp = 0;
    vector<int> pert = per;
    pert[real[i]] = 0;
    int monye = 0;
    for (int i1 = real[i] + 1; i1 <= p && pert[i1] ==1;i1++)
      monye++;
    for (int i2 = real[i] - 1; i2 >=1 && pert[i2] ==1; i2--)
      monye++;
    vector<int> tempv = real;
    tempv.erase(tempv.begin() + i);
    temp = monye + sovle(p, q, tempv, pert);

    if (temp < result) {
      result = temp;      
    }     
  }
  return result;
}

int main()
{
  freopen("A-large (1).in","r",stdin);
  freopen("outputl.txt","w",stdout);
  int Test;
  cin >> Test;
  // cin >> 
  
  for (int i = 0; i < Test; i++) {
    int p,q;
    cin >> p >> q;
    vector<int> real;
    for (int j = 0; j < q; ++j) {
      int temp;
      cin >> temp;
      real.push_back(temp);
    }
    vector<int> per(10001);
    for (int k = 0; k < 10001; k++)
      per[k] = 0;
    for (int l = 1; l <= p; l++)
      per[l] = 1;
    int end = real.size();
    long long result = sovle(p,q,real, per);
    cout << "Case #"<< i + 1 <<": " << result << endl;   
  }
  /*set<int> temp;
  is_happy(82, 10, temp);*/
  return 0;

  

}