#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<pair<pair<int,int>,int> > plants;

double answer();

int main(){
  int t;
  cin>>t;
  cout.setf(ios::fixed|ios::showpoint);
  cout.precision(6);
  for(int i=1;i<=t;i++){
    int n;
    cin>>n;
    plants=vector<pair<pair<int,int>,int> >(n);
    for(int j=0;j<n;j++)
      cin>>plants[j].first.first>>plants[j].first.second>>plants[j].second;
    cout<<"Case #"<<i<<": "<<answer()<<'\n';
  }
}

double dist(double dx,double dy){
  return sqrt(dx*dx+dy*dy);
}

double dist(pair<int,int> a,pair<int,int> b){
  return dist(a.first-b.first,b.second-a.second);
}

double answer3(pair<pair<int,int>,int> a,pair<pair<int,int>,int> b,pair<pair<int,int>,int> bb){
  double ret=a.second*2.;
  ret=max(ret,dist(b.first,bb.first)+b.second+bb.second);
  return ret;
}

double answer(){
  if(plants.size()==1)
    return plants[0].second;
  if(plants.size()==2)
    return max(plants[0].second,plants[1].second);
  double a0=answer3(plants[0],plants[1],plants[2]);
  double a1=answer3(plants[1],plants[0],plants[2]);
  double a2=answer3(plants[2],plants[0],plants[1]);
  return min(a0,min(a1,a2))/2.;
}
