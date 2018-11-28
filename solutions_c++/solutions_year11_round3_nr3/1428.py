#include <fstream>
#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int gcd(int a, int b){
  while(b != 0){
    int t = b;
    b = a % b;
    a = t;
  }

  return a;
}

int lcm(int a, int b){
  if(a == 1)
    return b;

  if(b == 1)
    return a;

  return (a * b) / gcd(a, b);
}

int lcm(vector<int>& freqs){
  int n = freqs.size();
  if(freqs.size() == 1)
    return freqs[0];

  int result = 1;
  for(int i = 0; i < n; ++i){
    result = lcm(freqs[i], result);
  }

  return result;
}

bool in_harmony(int a, int b){
  return (a % b == 0) || (b % a == 0);
}

bool in_harmony(int f, vector<int>& freqs, int n){
  for(int i = 0; i < n; ++i)
    if(!in_harmony(f, freqs[i]))
      return false;

  return true;
}

void run(istream& input){
  int ncases;

  input >> ncases;

  for(int icase = 0; icase < ncases; ++icase){
    int n, l, h;
    input >> n >> l >> h;
    //fprintf(stderr, "%d: %d,%d,%d\n", icase, n, l, h);
    int fjeff = l;
    vector<int> freqs;
    for(int ifreq = 0; ifreq < n; ++ifreq){
      
      int freq;
      input >> freq;
      freqs.push_back(freq);
    }

    for(int ifreq = 0; ifreq < n && fjeff <= h; ++ifreq){
      int freq = freqs[ifreq];
      //fprintf(stderr, "\t%d,%d\n", ifreq, freq);
      while(!in_harmony(fjeff, freqs, ifreq + 1) && fjeff <= h)
        fjeff++;

      if(fjeff > h)
        break;
    }

    if(fjeff > h)
      printf("Case #%d: NO\n", icase + 1);
    else
      printf("Case #%d: %d\n", icase + 1, fjeff);
  }
}

int main(int argc, char *argv[]){
  if(argc > 1)
    run(ifstream(argv[1]));
  else
    run(cin);
  return 0;
}