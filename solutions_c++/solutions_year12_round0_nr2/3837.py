#include <iostream>
#include <vector>

using namespace std;

int main()
{
  int T, N, S, p, cnt=0, ts, as, s, ns;
  vector <int> r;

  cin>>T;
  for (int i=1; i<=T; ++i)
  {
    r.clear();
    cnt=0;
    cin>>N>>S>>p;

    for (int j=0; j<N; ++j)
    {
      cin>>ts; 
      as = ts/3;

      if (ts == 0)
      {
        if (ts >= p)
          ++cnt;
        continue;
      }

      if (ts == 1)
      {
        if (ts >= p)
          ++cnt;
        continue;
      }

      if (ts == 29)
      {
        if (10 >= p)
          ++cnt;
        continue;
      }

      if (ts == 30)
      {
        if (10 >= p)
          ++cnt;
        continue;
      }

      if (ts % 3 == 0)
      {
        s = as+1;
        ns = as;
      }
      else if (ts %3 == 1)
      {
        s = as+1;
        ns = as+1;
      }
      else if (ts % 3 == 2)
      {
        s = as+2;
        ns = as+1;
      }

      if (ns >= p)
      {
        ++cnt;
      }
      else
      {
        r.push_back(s);
      }
    }


    sort(r.begin(), r.end(), greater<int>());

    for (int j=0; j<r.size() && j<S; ++j)
    {
      if(r[j] >= p)
        ++cnt;
    }

    cout<<"Case #"<<i<<": "<<cnt<<"\n";
    
  }
}

