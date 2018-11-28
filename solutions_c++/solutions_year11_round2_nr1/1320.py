#include <cstdio>
#include <cstring>


using namespace std;

int T;
int N;

char a[105][105];
double owp[105];
double oowp[105];
int won[105];
int ops[105];

int main(){
  scanf("%d", &T);
						
  for (int ttt=1; ttt<=T; ttt++){
    scanf("%d ", &N);
    for (int t=0; t<N; t++){
      ops[t] = won[t] = 0; 
      for (int o=0; o<N; o++){
	scanf("%c", a[t]+o);
	if (a[t][o] != '.'){
	  ops[t]++;
	  if (a[t][o] == '1')
	    won[t]++;
	}
      }
      scanf(" ");
    }

    for (int t=0; t<N; t++){
      owp[t]=0;
      for (int o=0; o<N; o++){
	if (a[t][o]!='.')
	  owp[t] += ( won[o] - (a[o][t]=='1') ) / (ops[o]-1.0);
      }
      owp[t] /= ops[t];
    }

    printf("Case #%d:\n", ttt);

    for (int t=0; t<N; t++){
      oowp[t]=0;
      for (int o=0; o<N; o++){
	if (a[t][o]!='.')
	  oowp[t] += owp[o];
      }
      oowp[t]/=ops[t];
      
      printf("%.15lf\n", 0.25*(won[t]/double(ops[t])) + 0.5*(owp[t]) + 0.25*(oowp[t]));
    }
  }
}
