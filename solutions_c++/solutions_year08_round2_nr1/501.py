#include<iostream>
#include<vector>
using namespace std;

int tab[5][5];

int main(){
  int N;
  ios::sync_with_stdio(false);
  cin >> N;
  for(int q=1;q<=N;q++){
    memset(tab,0,sizeof(tab));
    int n;
    long long A,B,C,D,x0,y0,M;
    long long x,y;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    x=x0;
    y=y0;
    tab[x%3][y%3]++;
    for(int i=1;i<n;i++){
      x = (A*x+B)%M;
      y = (C*y+D)%M;
      tab[x%3][y%3]++;
    }
    long long sum=0;
    for(int i=0;i<3;i++){
      for(int j=0;j<3;j++){
	sum+=tab[i][j]*(tab[i][j]-1)*(tab[i][j]-2)/6;
      }
      sum+=tab[i][0]*tab[i][1]*tab[i][2];
      sum+=tab[0][i]*tab[1][i]*tab[2][i];
    }
    vector<int> t,tt;
    t.push_back(0);
    t.push_back(1);
    t.push_back(2);
    tt.push_back(0);
    tt.push_back(1);
    tt.push_back(2);
    long long ns=0;
    do{
      do{
	ns+=tab[t[0]][tt[0]]*tab[t[1]][tt[1]]*tab[t[2]][tt[2]];
      }while(next_permutation(tt.begin(),tt.end()));
    }while(next_permutation(t.begin(),t.end()));
    ns/=6;
    cout<<"Case #"<<q<<": "<<sum+ns<<endl;
  }
  return 0;
}
