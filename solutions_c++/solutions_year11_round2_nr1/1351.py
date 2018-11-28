#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

char v[100][100];
double wp[100][100];
double owp[100];

int main(){

  int T;
  cin >> T;

  for(int t = 1; t <= T; t++){

    int N;
    cin >> N;

    for(int i = 0; i < N; i++){
      for(int j = 0; j < N; j++){
	cin >> v[i][j];
      }
    }

    for(int i = 0; i < N; i++){
      int total = 0, win = 0;
      for(int j = 0; j < N; j++){
	if(v[i][j] != '.') total++;
	if(v[i][j] == '1') win++;
      }
      for(int j = 0; j < N; j++){
	wp[i][j] = (double)(v[i][j] == '1'? win - 1 : win) / (v[i][j] != '.' ? total - 1 : total);
      }
    }

    for(int i = 0; i < N; i++){
      double sum = 0; int total = 0;
      for(int j = 0; j < N; j++){
	if(v[i][j] != '.'){
	  total++;
	  sum += wp[j][i];
	}
      }
      owp[i] = sum / total;
    }

    cout << "Case #" << t << ":" << endl;
    for(int i = 0; i < N; i++){
      double oowp = 0;
      int total = 0;
      for(int j = 0; j < N; j++){
	if(v[i][j] != '.'){
	  oowp += owp[j];
	  total++;
	}
      }
      oowp /= total;

      printf("%.8f\n", wp[i][i]*0.25 + owp[i]*0.5 + oowp*0.25);
    }
  }

  return 0;
}
