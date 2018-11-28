#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

bool solve(vector< vector<double> > left,vector<double> right){
/*FOR(i,left.size()){
  FOR(j,left[i].size())cout<<left[i][j]<<" ";
  cout<<": "<<right[i]<<endl;
}
cout<<endl;*/
  if(!left.size())return true;
  int N=left[0].size();
#define EPS 1e-8  
  if(!N){FOR(i,right.size())if(right[i]<-EPS)return false; return true;}
  vector< vector<double> > left_neg,left_pos,left_zero,left_all;
  vector<double> right_neg,right_pos,right_zero,right_all;
  FOR(i,left.size())if(left[i].back()<-EPS){
    double m=-left[i].back();
    left_neg.push_back(left[i]);
    left_neg.back().pop_back();
    FOR(j,N-1)left_neg.back()[j]/=m;
    right_neg.push_back(right[i]/m);
  } else if (left[i].back()>EPS){
    double m=left[i].back();
    left_pos.push_back(left[i]);
    left_pos.back().pop_back();
    FOR(j,N-1)left_pos.back()[j]/=m;
    right_pos.push_back(right[i]/m);  
  } else {
    left_all.push_back(left[i]);
    left_all.back().pop_back();
    right_all.push_back(right[i]);
  }
  FOR(i,left_neg.size())FOR(j,left_pos.size()){
    left_all.push_back(vector<double>(N-1));
    right_all.push_back(right_neg[i]+right_pos[j]);
    FOR(k,N-1)left_all.back()[k]=left_neg[i][k]+left_pos[j][k];
  }  
  return solve(left_all,right_all);
}
int N;
double x[1010],y[1010],z[1010],p[1010];
bool ok(double bound){
  double min[2][2][2];
  FOR(i,2)FOR(j,2)FOR(k,2)min[i][j][k]=1e20;
  FOR(a,N)FOR(i,2)FOR(j,2)FOR(k,2){
    double s=p[a]*bound;
    if(i)s-=x[a]; else s+=x[a];
    if(j)s-=y[a]; else s+=y[a];
    if(k)s-=z[a]; else s+=z[a];
    min[i][j][k]<?=s;
  }
  vector< vector<double> > left;
  vector<double> right;
  FOR(i,2)FOR(j,2)FOR(k,2){
    left.push_back(vector<double>());
    left.back().push_back(i?-1:1);
    left.back().push_back(j?-1:1);
    left.back().push_back(k?-1:1);
    right.push_back(min[i][j][k]);
  }
  return solve(left,right);
}
main(){
  int C;cin>>C;
  for(int c=1;c<=C;c++){
    double from=0,to=1e20;
    cin>>N;
    FOR(i,N)cin>>x[i]>>y[i]>>z[i]>>p[i];
    FOR(z,100)if(ok((from+to)/2))to=(from+to)/2; else from=(from+to)/2;
    cout<<"Case #"<<c<<": ";
    printf("%.6lf\n",from);
  }
}
