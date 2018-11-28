#include <iostream>
#include <vector>
#include <string>


using namespace std;

typedef long long ll;

string w[200];
int N;

vector<double> WP()
{
  vector<double> res(N,0.0);
  double count, win, lose;
  for(int i=0; i<N; i++)
    {
      count = win = lose = 0.0;
      res[i] = 0.0;
      for(int j=0; j<N; j++)
	{
	  switch(w[i][j])
	    {
	    case '.': break;
	    case '1': win++,  count++; break;
	    case '0': lose++, count++; break;
	    }
	}
      res[i] = win / count;
    }
  return res;
}

double OWP(int team, int ignore, vector<double>& WP )
{
  double count, res, win, lose;
  count = res = win = lose = 0.0;

  for(int i=0; i<N; i++)
    {
      if(i==ignore)
	continue;
      switch(w[team][i])
	{
	case '.': break;
	case '1': win++,  count++; break;
	case '0': lose++, count++; break;
	}
    }
  res = win / count;
  
  return res;
}


vector<double> OWP( vector<double>& wp )
{
  vector<double> res(N,0.0);
  double count;
  
  for(int i=0; i<N; i++)
    {
      count = res[i] = 0.0;

      for(int j=0; j<N; j++)
	  {
	    if(w[i][j]!='.')
	      {
		res[i] += OWP(j, i, wp);
		count++;
	      }
	  }
      res[i] = res[i] / count;
    }
  return res;
}

vector<double> OOWP( vector<double>& owp )
{
  vector<double> res(N,0.0);
  double count;
  
  for(int i=0; i<N; i++)
    {
      count = res[i] = 0.0;

      for(int j=0; j<N; j++)
	  {
	    if(w[i][j]!='.')
	      {
		res[i] += owp[j];
		count++;
	      }
	  }
      res[i] = res[i] / count;
    }
  return res;
}

void print(vector<double> v)
{
  for(int i=0; i<v.size(); i++)
    cout<<v[i]<<endl;
  cout<<endl;
}


int main()
{
  int tc;
  cin>>tc;
  for(int T=1; T<=tc; T++)
    {
      cin>>N;
      for(int i=0; i<N; i++)
	  cin>>w[i];

      cout<<"Case #"<<T<<":"<<endl;
      vector<double> wp = WP();
      //      print(wp);
      vector<double> owp = OWP(wp);
      //      print(owp);
      vector<double> oowp = OOWP(owp);

      for(int i=0; i<wp.size(); i++)
	cout<< ( 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] ) <<endl;
      
      
    }  
  return 0;
}
