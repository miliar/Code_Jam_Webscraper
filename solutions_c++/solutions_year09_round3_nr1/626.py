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

ll sovle(string input)
{
  map<char, int> map_num;
  int count = 1;
  ll  result = 0;
  
  for (int i = 0; i < input.length(); ++i) {
    map<char, int>::iterator itr = map_num.find(input[i]);
    
    if (itr != map_num.end())
      continue;
    
    if (map_num.size() == 1 && itr == map_num.end())
      map_num[input[i]] = 0;
    else if (itr == map_num.end())
      map_num[input[i]] = count++;
      
  }
  int jinzhi = map_num.size();
  if (jinzhi == 1)
    jinzhi = 2;
  for (int i = 0; i < input.length(); ++i) {
    result *= jinzhi;
    result += map_num[input[i]]; 
  }

  return result;
}
int main()
{
  freopen("A-large (1).in","r",stdin);
  freopen("outputl.txt","w",stdout);
  int Test;
  string input;
  getline(cin, input);
  stringstream strs;
  strs << input;
  strs >> Test;
  // cin >> 
  
  for (int i = 0; i < Test; i++) {
    getline(cin, input);
    long long result = sovle(input);
    cout << "Case #"<< i + 1 <<": " << result << endl;   
  }
  /*set<int> temp;
  is_happy(82, 10, temp);*/
  return 0;

  

}