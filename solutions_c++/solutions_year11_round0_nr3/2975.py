// candy_splitting.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cassert>
#include <cstdio>
#include <tchar.h>
#include <vector>
#include <fstream>

using namespace std;

int patrick(int a, int b){
  int sum = 0;
  int n = 0;

  while((a != 0) || (b != 0)){
    int bita = (a & 1);
    int bitb = (b & 1);

    if(bita != bitb)
      sum |= (bita | bitb) << n;

    a >>= 1;
    b >>= 1;
    n++;
  }

  return sum;
}

bool next_combination(vector<bool>& flags){

  int size = flags.size();
  bool carry = false;
  if(flags[0]){
    carry = true;
    flags[0] = false;
  }
  else
    flags[0] = true;

  int i = 1;
  while(carry && i < size){
    if(flags[i])
      flags[i] = false;
    else {
      flags[i] = true;
      carry = false;
    }

    i++;
  }

  for(vector<bool>::iterator itr = flags.begin(); itr != flags.end(); ++itr)
    if(!*itr)
      return true;  // indicates a zero bit was found

  return false;
}

void find_sums(vector<int>& vcandy, vector<bool>& flags, int& max_total){
  int ssean = 0;
  int sean_value = 0;
  int spatrick = 0;

  for(int iflag = 0, nflag = flags.size(); iflag < nflag; ++iflag){
    if(flags[iflag]){
      ssean = patrick(ssean, vcandy[iflag]);
      sean_value += vcandy[iflag];
    }
    else
      spatrick = patrick(spatrick, vcandy[iflag]);
  }

  if(ssean == spatrick){
    if(sean_value > max_total)
      max_total = sean_value;
  }
}

void run(istream& input){

  int ncase;
  input >> ncase;

  for(int icase = 0; icase < ncase; ++icase){
    int n;
    input >> n;

    vector<int> vcandy;

    for(int i = 0; i < n; ++i){
      int candy;
      input >> candy;
      vcandy.push_back(candy);
    }

    int max_total = -1;

    vector<bool> flags;
    for(int i = 0; i < n; ++i)
      flags.push_back(false);

    flags[0] = true;
    while(next_combination(flags)){
      find_sums(vcandy, flags, max_total);
    }

    if(max_total == -1)
      printf("Case #%d: NO\n", icase + 1);
    else
      printf("Case #%d: %d\n", icase + 1, max_total);

  }

}

int _tmain(int argc, _TCHAR* argv[])
{
  assert(patrick(5, 4) == 1);
  assert(patrick(7, 9) == 14);
  assert(patrick(50, 10) == 56);

  if(argc > 1){
    ifstream input(argv[1]);
    run(input);
  }
  else
    run(cin);

	return 0;
}

