#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<set>

using namespace std;

vector<long long> x;
vector<long long> y;
set<pair<long long,long long> > ok;

int main()
{
  freopen("a.in","r", stdin);
  freopen("a.out","w",stdout);
  long long t;
  cin >> t;
  long long n,A,B,C,D,x0,y0,M;
  for (int tt = 0; tt < t; tt++)
  {
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    ok.clear();
    x.clear();
    y.clear();
    ok.insert(make_pair(x0,y0));
    x.push_back(x0);
    y.push_back(y0);
    long long X,Y;
    for (int i = 1; i < n; i++)
    {
      X = (A * x[x.size()-1] + B) % M;
      Y = (C * y[y.size()-1] + D) % M;
      if (ok.find(make_pair(X,Y)) == ok.end())
      {
        x.push_back(X);
        y.push_back(Y);
      }  
    }

//    for (int i = 0; i < n; i++)
 //     cout << x[i] << " " << y[i] << endl;


    long long sum = 0;
    long long n = x.size();
    for (int i = 0; i < n; i++)
      for (int j = i+1; j < n; j++)
        for (int k = j+1; k < n; k++)
        {
//          cout << ((x[i]+x[j]+x[k]) / 3.0) << " " << (long long)((x[i]+x[j]+x[k]) / 3.0) << endl;
          if ((x[i]+x[j]+x[k]) / 3.0 == (long long)((x[i]+x[j]+x[k]) / 3))
            if ((y[i]+y[j]+y[k]) / 3.0 == (long long)((y[i]+y[j]+y[k]) / 3))
              sum++;
        }
    cout << "Case #" << tt+1 << ": " << sum << endl;
  
  }



  return 0;
}