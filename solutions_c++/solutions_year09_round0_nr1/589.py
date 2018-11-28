#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

#define POW2(a) ((1) << (a))
#define BIT(a, b) (((a) >> (b)) & (1))

vector <int> get_mask(string s);

int main(void)
{
  int L, D, N;
  cin >> L >> D >> N;
  vector <string> words;
  for(int i = 0; i < D; i++) {
    string s;
    cin >> s;
    words.push_back(s);
  }
  for(int i = 0; i < N; i++) {
    string s;
    cin >> s;
    vector <int> pattern = get_mask(s);
    int cnt = 0;
    if(pattern.size() != L) {
      cnt = 0;
    }
    else {
      for(int j = 0; j < words.size(); j++) {
        int good = 1;
        for(int k = 0; k < L; k++) if(!BIT(pattern[k], words[j][k] - 'a')) good = 0;
        if(good) cnt++;
      }
    }
    printf("Case #%d: %d\n", i + 1, cnt);
  }
    
  return 0;
}

vector <int> get_mask(string s)
{
  vector <int> res;
  
  for(int i = 0; i < s.size(); i++) {
    if(s[i] != '(') { res.push_back(POW2(s[i] - 'a')); continue; }
    i++;
    int mask = 0;
    while(s[i] != ')') { mask |= POW2(s[i] - 'a'); i++; }
    res.push_back(mask);
  }
  
  return res;
}

