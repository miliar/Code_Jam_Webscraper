#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;


int main() 
{
  int ncase = 1;
  int t;
  cin >> t;
  while(t--) 
  {
    int n;
    cin >> n;
    vector<int> x;
    vector<int> y;
    string s;
    int t;
    for(int i=0;i<n;i++) 
    {
      cin >> s;
      stringstream temp(s);
      temp >> t;
      x.push_back(t);
    }
    for(int i=0;i<n;i++) 
    {
      cin >> s;
      stringstream temp(s);
      temp >> t;
      y.push_back(t);
    }
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());
    int tail=n-1;
    int sum =0;
    
    for(int i=0;i<n;i++) 
    {
      sum+=x[i]*y[tail--];
    }
    
    cout << "Case #" << ncase++ <<" "<< sum << endl;
  }
  return 0;
}

    
