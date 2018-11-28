#include <iostream>
#include <vector>
using namespace std;

int main(){
  int cases;
  cin >> cases;
  int temp = 0;
  while(cases--){
    cout << "Case #" << ++temp << ": ";
    int p,k,l;
    cin >> p >> k >> l;
    vector<long long> data(l);
    for(int i=0;i<l;i++){
      cin >> data[i];
    }
    sort(data.begin() ,data.end(), greater<long long>());
    long long ret = 0;
    if(p*k<l){
      cout << "Impossible" << endl;
    }else{
      long long cur = 1;
      int num = 0;
      for(int i=0;i<l;i++){
	num++;
	ret += data[i]*cur;
	if(num==k){
	  num=0;
	  cur++;
	}
      }
      cout << ret << endl;
    }     
  }
  return 0;
}
