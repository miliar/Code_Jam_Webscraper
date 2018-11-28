#include <iostream>
#include <vector>
#include <fstream>
#include <iostream>

using namespace std;
double dp[1001];

void fill_dp(){
  dp[1] = 0.0;
  dp[2] = 2.0;
  for(int i=3;i<=1000;i++){
    double tmp = 0.0;
    for(int j=2; j<i; j++)
      tmp += (dp[j] + dp[i-j]);
    tmp += dp[i-1] + 1.0;
    dp[i] = (tmp+1.0)/(i-1);
  }
}

double solve(vector <int>& v){
  double ans = 0.0;
  for(int i=0;i<v.size();i++){
    if(v[i] != -1){
      int cnt = 0;
      int pos = i;
      int tmp;
      do{
	tmp = v[pos]-1;
	v[pos] = -1;
	pos = tmp;
	cnt++;
      }while(v[pos] != -1);
      ans += dp[cnt];
    }
  }
  return ans;
}

int main(){
  fill_dp();

  fstream ifs;
  FILE* ofp;
  int Nprob;

  ofp = fopen("D.out", "w");
  ifs.open("D-large.in", fstream::in);
  ifs >> Nprob;

  int n,m;
  for(int i=0;i<Nprob;i++){
    vector <int> v;
    ifs >> n;
    for(int j=0;j<n;j++){
      ifs >> m;
      v.push_back(m);
    }
    double ans = solve(v);
    fprintf(ofp, "Case #%d: %f\n", i+1, ans);
  }
}
