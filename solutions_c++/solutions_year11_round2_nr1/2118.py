#include <iostream>
#include <vector>
using namespace std;

double calcWP(int N, int j, char** a, vector<int>& opponents, int k ) 
{
  double curOwp = 0;
  int c = 0;
  for (int i = 0; i<N; i++)
  {
    if (i == j) continue;
    if (a[opponents[k]][i] != '.')
    {
      curOwp += a[opponents[k]][i] - 48;
      c++;
    }
  }
  curOwp /= c;
  return curOwp;
}

double calcOWP( vector<int> &opponents, int N, int j, char** a ) 
{
  double owp = 0;
  for (int k = 0; k < opponents.size(); k++)
  {
    owp += calcWP(N, j, a, opponents, k);
  }
  owp /= opponents.size();

  return owp;
}

int main()
{
  int T;
  cin>>T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #"<<t<<":"<<endl;
    int N;
    cin>>N;
    char** a = new char*[N];
    for (int j = 0; j < N; j++)
    {
      a[j]=new char[N];
      for (int k = 0; k < N; k++)
      {
        cin >> a[j][k];
      }
    }

    double* wp = new double[N];
    for (int j = 0; j < N; j++)
    {
      wp[j] = 0;
      int c = 0;
      for (int k = 0; k < N; k++)
      {
        if (a[j][k] != '.')
        {
          c++;
          wp[j] += a[j][k] - 48;
        }
      }
      wp[j] /= c;
    }

    double* owp = new double[N];
    for (int j = 0; j < N; j++)
    {
      owp[j] = 0;
      vector<int> opponents;
      for (int k = 0; k < N; k++)
      {
        if (a[j][k] != '.')
        {
          opponents.push_back(k);
        }
      }
      owp[j] = calcOWP(opponents, N, j, a);
    }
    double* oowp = new double[N];
    for (int j = 0; j< N; j++)
    {
      oowp[j] = 0;
      //vector<int> opponents;
      int c = 0;
      for (int k = 0; k < N; k++)
      {
        if (a[j][k] != '.')
        {
          oowp[j]+=owp[k];
          c++;
        }
      }
      oowp[j] /= c;
    }
       
    cout.precision(7);
    for (int j = 0; j < N; j++)
    {
      //cout<<"wp for "<<j <<" is "<<wp[j]<<". Owp is "<<owp[j]<<". OOwp is "<<oowp[j]<<endl;
      //cout << "RPI for "<<j<<" =" << (0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j])<<endl;
      cout << (0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j])<<endl;
    }
  }

  return 0;
}