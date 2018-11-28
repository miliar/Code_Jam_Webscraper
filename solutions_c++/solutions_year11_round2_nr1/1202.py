#include <iostream>
#include <queue>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long LL;


string A[101];
double WP[101][2];
double OWP[101];
double OOWP[101];

int main(){

  string ln;
  int N,T;

  getline(cin,ln);
  istringstream(ln)>>T;


  for(int test=1;test<=T;test++){
    getline(cin,ln);
    istringstream(ln)>>N;

    for(int i=0;i<N;i++){
      getline(cin,A[i]);
    }



    for(int i=0;i<N;i++){
      double w=0;
      double n=0;

      for(int k=0;k<N;k++){
        if(A[i][k]=='.') continue;
        if(A[i][k]=='1') w+=1;
        n+=1;
      }

      WP[i][0]=w;
      WP[i][1]=n;
    }

    for(int i=0;i<N;i++){
      double wp=0;
      double n=0;

      for(int k=0;k<N;k++){
        if(A[i][k]=='.') continue;

        wp+=(WP[k][0]-(A[k][i]-'0'))/(WP[k][1]-1);
        n+=1;
      }

      OWP[i]=wp/n;
    }

    for(int i=0;i<N;i++){
      double owp=0;
      int n=0;

      for(int k=0;k<N;k++){
        if(A[i][k]=='.') continue;

        owp+=OWP[k];
        n+=1;
      }

      OOWP[i]=owp/n;
    }

    cout<<"Case #"<<test<<":"<<endl;

    for(int i=0;i<N;i++){
      cout<<fixed<<setprecision(10)<<( ((double)WP[i][0]/WP[i][1])/4 + OWP[i]/2 + OOWP[i]/4 )<<endl;
    }

  }




  return 0;
}
