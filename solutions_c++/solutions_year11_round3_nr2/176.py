#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<functional>

using namespace std;

typedef long long int lli;

int main(){
  int tn;
  cin >> tn;

  for(int tc = 1; tc <= tn; tc++){
    lli l,t,n,c;
    cin >> l >> t >> n >> c;
    vector<int> tab(n,0);
    vector<int> tabc(n,0);
    vector<int> cc(c,0);
    vector< pair<int,int> > prc(c,make_pair(0,0));
    for(int i=0; i<c; i++){
      cin >> cc[i];
      prc[i] = make_pair(cc[i],i);
    }
    vector< lli > tab2;
    lli sum = 0;
    int sp = -1;
    int spc = -1;
    for(int i=0,cp = 0; i<n; i++){
      tab[i] = cc[cp];
      tabc[i] = cp;
      if(sp != -1){
	tab2.push_back(tab[i]);
      }
      if(sp == -1 && sum + (tab[i] * 2) >= t){
	lli sz = ((tab[i]*2) - (t - sum))/2;
	tab2.push_back(sz);
	sp = i + 1;
	spc = cp;
      }
      sum += (tab[i]*2);
      cp = (cp + 1) % c;
    }
    sort(tab2.begin(),tab2.end(), greater<lli>() );
    int ln = l;
    for(int i=0; i<tab2.size() && ln>0; ln--,i++){
      sum -= tab2[i];
    }

    cout << "Case #" << tc << ": " << sum << endl;
  }
  return 0;
}
