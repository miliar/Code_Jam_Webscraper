#include<iostream>
#include<string>
#include<algorithm>
#include<bitset>
#include<vector>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int q;
  cin >> q;
  for(int mu=1;mu<=q;mu++){
    int n;
    cin >> n;
    cin.ignore(1);
    vector<string> sch(n,"");
    for(int i=0;i<n;i++){
      getline(cin,sch[i]);
    }
    sort(sch.begin(),sch.end());
    int nq;
    cin >> nq;
    cin.ignore(1);
    vector<int> srs;
    for(int i=0;i<nq;i++){
      string t;
      getline(cin,t);
      int ind = lower_bound(sch.begin(),sch.end(),t) - sch.begin();
      if(sch[ind]==t){
	srs.push_back(ind);
      }
    }
    bitset<110> bts(0);
    int cnt=0;
    for(int i=0;i<srs.size();i++){
      bts.set(srs[i]);
      if(bts.count()==n){
	cnt++;
	bts.reset();
	bts.set(srs[i]);
      }
    }
    cout<<"Case #"<<mu<<": "<<cnt<<endl;
  }
  return 0;
}
