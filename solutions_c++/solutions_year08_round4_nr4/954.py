#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

string permute(string s, vector<int> perm, int k);
int encode(string s);

int main(){
  int test = 1, c, min, k, x;
  string s;

  cin >> c;

  while(c--){

    cin >> k >> s;

    vector<int> p;

    for(int i = 0 ; i < k ; i++)
      p.push_back(i);

    min = s.size();

    do{

      x = encode(permute(s, p, k));

      if(x < min)
	min = x;
    }while(next_permutation(p.begin(), p.end()));

    p.clear();

    cout << "Case #" << test++ << ": " << min << endl;
  }
}

string permute(string s, vector<int> perm, int k){
  
  string x = "";

  for(int i = 0 ; i < s.size() ; i++)
    x += s[perm[i % k] + (i / k) * k];

  return x;
}

int encode(string s){

  int c = 1;

  for(int i = 1 ; i < s.size() ; i++)
    if(s[i] != s[i - 1])
      c++;

  return c;
}
