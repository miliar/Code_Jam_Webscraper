#include <iostream>
#include <vector>

#define REP(i,e) for(int i=0;i<(int)(e);i++)

using namespace std;

int compute(vector<int> &d,vector<int> &a,int l){
  sort(d.begin(),d.end());
  sort(a.begin(),a.end());

  REP(i,a.size()) a[i]+=l;

  int result=0;
  REP(i,d.size()){
    vector<int>::iterator it=min_element(a.begin(),a.end());
    if (it==a.end() || d[i]<*it){
      result++;
    }
    else {
      a.erase(it);
    }
  }
  return result;
}

main(){
  int ct;
  cin >> ct;
  REP(c,ct){
    cout << "Case #" << c+1 << ':';
    int l;
    cin >> l;

    vector<int> ad,bd,aa,ba;
    int an,bn;
    cin >> an >> bn;
    while(an--){
      char t;
      int h,m;
      cin >> h >> t >> m;
      ad.push_back(h*60+m);
      cin >> h >> t >> m;
      aa.push_back(h*60+m);

    }
    while(bn--){
      char t;
      int h,m;
      cin >> h >> t >> m;
      bd.push_back(h*60+m);
      cin >> h >> t >> m;
      ba.push_back(h*60+m);
    }

    cout << ' ' << compute(ad,ba,l) 
	 << ' ' << compute(bd,aa,l) << endl;
  }
}
