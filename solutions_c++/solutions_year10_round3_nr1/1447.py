#include <iostream>
#include <vector>
using namespace std;

int
check(int a, int b, int c, int d)
{
  if( a < c && b > d) return 1;
  if( a > c && d > b) return 1;
  return 0;
}

int
inter(vector<pair<int, int> > &v)
{
  int a = 0;
  for(int i = 0; i < v.size(); i++){
    for(int j = 0; j < v.size(); j++){
      if( i > j) break;

      a += check(v[i].first, v[i].second, v[j].first, v[j].second);

    }
  }

  return a;
}

int
main()
{
  int t;
  cin>>t;
  for(int i = 0; i < t; i++){
    int n;
    int ans = 0;
    vector<pair<int,int> > v;
    cin>>n;

    for(int j = 0; j < n; j++){
      int a, b;
      cin>>a>>b;
      v.push_back(make_pair(a, b));
    }

    ans = inter(v);

    cout<<"Case #"<<i+1<<": "<<ans<<endl;

  }
}
