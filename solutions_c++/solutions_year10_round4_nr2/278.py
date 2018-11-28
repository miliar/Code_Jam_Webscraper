#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

const int imax=1000000000;
vector<vector<int> > cost;
vector<int> canmiss;
int maxdepth;
int best[11][1024][11];

int calc()
{
  int i,depth,missed;
  for(i=0;i<(1<<maxdepth);++i) for(missed=0;missed<=maxdepth;++missed)
    best[0][i][missed]=(missed>canmiss[i]?imax:0);
  for(depth=1;depth<=maxdepth;++depth)
    for(i=0;i<cost[depth-1].size();++i)
      for(missed=0;missed<=maxdepth-depth;++missed)
  {
    if(best[depth-1][i*2][missed]>=imax||best[depth-1][i*2+1][missed]>=imax)
    { best[depth][i][missed]=imax;
      continue;
    }
    else best[depth][i][missed]=cost[depth-1][i]+
      best[depth-1][i*2][missed]+best[depth-1][i*2+1][missed];
    if(best[depth-1][i*2][missed+1]>=imax||best[depth-1][i*2+1][missed+1]>=imax)
      continue;
    int r=best[depth-1][i*2][missed+1]+best[depth-1][i*2+1][missed+1];
    if(r<best[depth][i][missed]) best[depth][i][missed]=r;
  }
  return best[maxdepth][0][0];
}

int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  {
    int i,j;
    cin>>maxdepth;
    canmiss.resize(1<<maxdepth);
    for(i=0;i<canmiss.size();++i) cin>>canmiss[i];
    cost.resize(maxdepth);
    for(i=0;i<maxdepth;++i) 
    { cost[i].resize(1<<maxdepth-i-1);
      for(j=0;j<cost[i].size();++j) cin>>cost[i][j];
    }
    cout<<"Case #"<<ci<<": "<<calc()<<endl;
  }
}
