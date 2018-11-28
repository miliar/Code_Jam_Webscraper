#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

typedef long long ll;

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=0;t<T;t++){
    string input;
    cin >> input;
    vector<char> symbols;
    for(int i=0;i<input.length();i++){
      if(find(symbols.begin(), symbols.end(), input.at(i))==symbols.end()) symbols.push_back(input.at(i));
    }
    ll base = symbols.size();
    if(base==1){
      base=2;
      symbols.push_back(0);
    }
    
    swap(*(symbols.begin()), *(symbols.begin()+1));
    //for(int i=0;i<symbols.size();i++)cout << symbols.at(i) << " ";
    //cout << endl;
    ll ans = 0;
    for(int i=0;i<input.length();i++){
      // find symbol position
      int j=0;
      bool found = false;
      while(j<symbols.size()&&!found){
	if(symbols.at(j)==input.at(i))found = true;
	else j++;
      }
      ans += ((ll)pow((double)base, (double)(input.length()-i-1)) * (ll)(j));
    }
    cout << "Case #" << t+1 << ": " << ans << endl;
  }
  return 0;
}
