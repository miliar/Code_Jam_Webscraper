#include <vector>
#include <iostream>


#define pb push_back

using namespace std;

int main() {
  __int64 T,i,j,result,L,P,K,tmp,m;
  vector<__int64>::iterator p,maxpos;
  vector<__int64> keys,och;
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  cin >> T;
  for(i=0;i<T;i++) {
    cin >> P;
    cin >> K;
    cin >> L;
    keys.clear();
    result=0;
    for(j=0;j<L;j++) {
      cin >> tmp;
      keys.pb(tmp);
    }
    tmp=0;
    while(!keys.empty()) {
      tmp++;
      och.clear();
      for(j=0;j<K;j++) {
        m = keys[0];
		maxpos=keys.begin();
		for(p=keys.begin();p!=keys.end();p++) {
			if(*p > m) {
				m=*p;
				maxpos=p;
			}
		}
		keys.erase(maxpos);
		och.push_back(m);
        if(keys.empty()) break;
      }
      for(j=0;j<och.size();j++) {
        result += och[j]*tmp;
      }
    }
    cout << "Case #"<<i+1<<": "<<result<<endl;
  }
  return 0;
}
