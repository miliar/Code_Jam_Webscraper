#include<iostream>
#include<set>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int q;
  cin >> q;
  for(int nq=1;nq<=q;nq++){
    int turnt;
    int cnta=0,cntb=0;
    int resa=0,resb=0;
    multiset<pair<int, bool> > trav;
    cin >> turnt;
    int na, nb;
    cin >> na >> nb;
    vector<pair<pair<int, int>, bool> > trains;
    for(int i=0;i<na;i++){
      int h1,m1,h2,m2;
      (cin >> h1).ignore(1); cin >> m1;
      (cin >> h2).ignore(1); cin >> m2;
      trains.push_back(make_pair(make_pair(60*h1+m1, 60*h2+m2), true));
    }
    for(int i=0;i<nb;i++){
      int h1,m1,h2,m2;
      (cin >> h1).ignore(1) >> m1;
      (cin >> h2).ignore(1) >> m2;
      trains.push_back(make_pair(make_pair(60*h1+m1, 60*h2+m2), false));
    }
    sort(trains.begin(),trains.end());
    int i=0;
    while(i<trains.size()){
      if(trav.empty() || trav.begin()->first > trains[i].first.first){
	//	cout<<"$"<<trains[i].first.first<<"->"<<trains[i].second<<endl;
	int readt = trains[i].first.second+turnt;
	bool side = trains[i].second;
	if(trains[i].second){
	  if(resa>0)resa--;
	  else cnta++;
	}else{
	  if(resb>0)resb--;
	  else cntb++;
	}
	trav.insert(make_pair(readt,side));
	i++;
      }else{
	bool side = trav.begin()->second;
	//	cout<<(trav.begin()->first)<<"<-"<<side<<endl;
	trav.erase(trav.begin());
	if(side)resb++;
	else resa++;
      }
    }
    cout<<"Case #"<<nq<<": "<<cnta<<" "<<cntb<<endl;
  }
  return 0;
}
