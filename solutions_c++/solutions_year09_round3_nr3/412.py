#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int simulate_one(int total, vector<int> & rel)
{
  vector<bool> cells(total, true);
  
  //cerr << "cells is " ;  for (int q=0;q<cells.size();q++) { cerr << cells[q] << ", "; } cerr << endl;
  
  int cost = 0;
  for (int i=0; i < rel.size(); i++)
  {
    int tor = rel[i];
    
    cells[tor] = false;
    
    int j=tor-1;
    
    while(j >= 0 && cells[j])
    {
      cost++;
      j--;
    }
    
    j = tor+1;
    
    while(j < total && cells[j])
    {
      cost++;
      j++;
    }
    
    //  cerr << "cells is " ;  for (int q=0;q<cells.size();q++) { cerr << cells[q] << ", "; } cerr << endl;
  }
  
  return cost;
}

int simulate(int total, vector<int> & rel)
{
  int min_coins = 10000*100+5;
  do
  {
    int n;
    
    //cerr << "Calling simulate_1 with: " << endl;for (int i=0;i<rel.size();i++) { cerr << rel[i] <<", ";}    cerr << endl;
    
    n = simulate_one(total, rel);
    
    //cerr << "got " << n << endl;
    
    if (n < min_coins)
    {
      min_coins = n;
    }
  } while(next_permutation(rel.begin(), rel.end()));
  
  return min_coins;
}

int main()
{

  int N; cin >>N;
  
  for (int outloop=0;outloop<N; outloop++)
  {
    int P,Q;
    cin >> P >> Q;
    
    vector<int> release;
    for (int inloop=0;inloop<Q;inloop++)
    {
      int tmp;
      cin >> tmp;
      release.push_back(tmp-1);
    }
    
    //cerr << "calling simulate" << endl;
    int r = simulate(P,release);
    
    cout << "Case #" << outloop+1 << ": " << r << endl;
  }
}
