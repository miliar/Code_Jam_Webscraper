#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <boost/foreach.hpp>

using namespace std;

std::string getLine()
{
  char line[4096];
  cin.getline(line, 4096);
  return line;
}

// problem can be simplified: chick that won't make it at their top speed
// must be removed


int main()
{
  int NT;
  cin >> NT;
  for (int t=0; t<NT; ++t)
  {
    int N, K, B, D;
    cin >> N >> K >> B >> D;
    vector<int> X;
    vector<int> V;
    for (int i=0; i<N; ++i)
    {
      int t;
      cin >> t;
      X.push_back(t);
    }
    for (int i=0; i<N; ++i)
    {
      int t;
      cin >> t;
      V.push_back(t);
    }
    // pos in increasing order
    vector<bool> makeIt; // make it alone?
    for (int i=0; i<N; ++i)
    {
      int dist = V[i] * D;
      //cerr <<"ach " << dist <<"  tgt " << (B-X[i]) << endl;
      makeIt.push_back(dist >= (B-X[i]));
      //cerr << makeIt.back() << " ";
    }
    //cerr << endl;
    int swap = 0;
    int k = 0;
    int i=0;
    for (int i=N-1; i>=0&& k<K; --i)
    {
      if (makeIt[i])
      { 
	k++;
	// good, now we just need to swap us with the ones before that dont
	for (int j=i+1; j<N; ++j)
	  if (!makeIt[j])
	    swap++;
      }
    }
     cout << "Case #" << (t+1) <<": ";
     if (k<K)
       cout <<  "IMPOSSIBLE";
     else
       cout << swap;
     cout << endl;
  }
}
