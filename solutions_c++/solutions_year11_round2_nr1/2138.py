#include <iostream>
#include <vector>
using namespace std;

double
calcowp( vector<vector<int> >& v, vector<int>& wp, int n, vector<int>& nn)
{
  double t = 0;
  for(int i = 0; i < wp.size(); i++){
    if( v[n][i] < 0 ) continue;

    if( v[n][i] > 0 ){
      t += (double)wp[i] / ( nn[i] - 1 );
    }else{
      t += (double)(wp[i] - 1) / ( nn[i] - 1 );
    }
  }
  return t/(nn[n]);
}

void
calc( int n, vector<vector<int> >& v, vector<int>& nn)
{
  vector<double> owp, oowp(n, 0);
  vector<int> cwp(n, 0);
  for(int i = 0; i < n; i++){
    for(int j = i; j < n; j++){
      if( v[i][j] < 0) continue;
      if( v[i][j] > 0 ) {
	cwp[i]++;
      }
      else{
	cwp[j]++;
      }
    }
  }

  for(int i = 0; i < n; i++){
    owp.push_back( calcowp( v, cwp, i, nn));
  }

  for(int i = 0; i < n; i++){
    for(int j = i; j < n; j++){
      if( v[i][j] < 0 ) continue;
      if( v[i][j] >= 0 ){
	oowp[i] += owp[j];
	oowp[j] += owp[i];
      }
    }
  }

  for(int i = 0; i < n; i++){
    //    cout<<(double)cwp[i]/nn[i]<<endl;
    //    cout<<owp[i]<<endl;
    cout<<0.25*(double)cwp[i]/nn[i] + owp[i] * 0.5 + 0.25 * (double)oowp[i]/nn[i]<<endl;
  }

}

int
main()
{
  int t;
  cin>>t;

  for(int i = 0; i < t; i++){
    int n;
    cin>>n;

    vector<vector<int> > v(n, vector<int>(n, 0));
    vector<int> nn;

    for(int j = 0; j < n; j++){
      string s; cin>>s; int t = 0;
      for(int k = 0; k < n; k++) {
	if( isdigit(s[k]) ) {
	  v[j][k] = s[k]-'0';
	  t++;
	}
	else v[j][k] = -1;
      }
      nn.push_back(t);
    }

    #if 0
    for(int j = 0; j < n; j++){
      for(int k = 0; k < n; k++) cout<<v[j][k];
      cout<<endl;
    }
    #endif
    cout<<"Case #"<<i+1<<":"<<endl;
    calc(n, v, nn);

  }

}
