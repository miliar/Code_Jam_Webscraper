#include<iostream>
#include<cstdio>
using namespace std;

#define REP(i,i0,in) for(int i=(i0); i<(in); i++)

int N;
int D[100][100];

void compute(){
  int ACC[N];
  int TOT[N];
  double WP[N];
  double OWP[N];
  double OOWP[N];

  // WP
  REP(i,0,N){
    int tot=0;
    int acc=0;
    REP(j,0,N){
      if (D[i][j]==-1) continue;
      tot++;
      if (D[i][j] == 1) acc++;
    }
    ACC[i] = acc;
    TOT[i] = tot;
    WP[i] = 1.0*acc/tot;
  }

  // OWP
  REP(i,0,N){
    int cnt=0;
    double owp = 0;
    REP(j,0,N){
      if (D[i][j]==-1) continue;
      double wp = (ACC[j]-D[j][i])*1.0/(TOT[j]-1);
      owp += wp;
      cnt++;
    }
    OWP[i] = owp/cnt;
  }

  // OOWP
  REP(i,0,N){
    int cnt_oowp=0;
    double oowp = 0;
    REP(j,0,N){
      if (D[i][j]==-1) continue;
      oowp += OWP[j];
      cnt_oowp++;
    }
    oowp /= cnt_oowp;
    OOWP[i] = oowp;
  }
  
  REP(i,0,N){
    double RPI = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
    printf("%.12lg\n", RPI);
  }
}

int main(){
  int T;
  cin >> T;
  REP(t,1,T+1){
    cin >> N;
    char ch;
    REP(j,0,N){
      REP(i,0,N){
	cin >> ch;
	D[j][i] = (ch=='.' ? -1 : (ch=='0' ? 0 : 1));
      }
    }
    printf("Case #%d:\n", t);
    compute();
  }
  return 0;
}
