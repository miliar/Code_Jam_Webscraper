#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>

using namespace std;

int N; // max 100
char m[100][100];
int won[100];
int played[100];
double WP[100];
double OWP[100];
double OOWP[100];

int run() {
  int i,k;
  for (i=0;i<N;++i) {
    int pplayed=0;
    int wwon=0;
    for (k=0;k<N;++k) { 
      if (m[i][k]=='1')
	wwon++;
      if (m[i][k]!='.')
	pplayed++;
    }
    won[i] = wwon;
    played[i] = pplayed;
    WP[i] = float(wwon)/float(pplayed);
    //    cerr<<"WP["<<i<<"]="<<WP[i]<<" "<<pplayed<<" "<<wwon<<endl;
  }
  
  for (i=0;i<N;++i) {
    float sum=0;
    int count=0;
    for (k=0;k<N;++k) {
      if (k==i) continue;
      if (m[k][i]=='.') continue;
      int wwon=won[k];
      int pplayed=played[k];
      if (m[k][i]=='1') {
	wwon--;
	pplayed--;
      } else {
	pplayed--;
      }
      //      cerr<<k<<" "<<wwon<<" "<<pplayed<<endl;
      sum += float(wwon)/float(pplayed);
      count++;
    }
    assert(count>0);
    OWP[i] = sum/float(count);
    //   cerr<<"OWP["<<i<<"]="<<OWP[i]<<endl;
  }

  for (i=0;i<N;++i) {
    float sum=0;
    int count=0;
    for (k=0; k<N; ++k) {
      if (m[k][i]=='.') continue;
      sum += OWP[k];
      count ++;
    }
    OOWP[i] = sum/float(count);
    //    cerr<<"OOWP["<<i<<"]="<<OOWP[i]<<endl;
  }
  
  for (i=0;i<N;++i) {
    cout<<endl;
    cout<< 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
  }
  
}

main() {
  int T;
  cin>>T;
  for (int Ti=1; Ti <= T; ++Ti) {
    cerr<<"Computing test: "<<Ti<<endl;
    cin>>N;
    for (int i=0;i<N; ++i) {
      string s;
      cin>>s;
      for (int k=0;k<N;++k) {
	m[i][k] = s[k];
	assert(strchr("01.",m[i][k]));
      }
    }

    cout.precision(10);
    cout<<"Case #"<<Ti<<": ";
    run();
    cout<<endl;
  }
}
