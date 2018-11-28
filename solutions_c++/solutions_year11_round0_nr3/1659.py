#include<iostream>
#include<vector>
using namespace std;

vector<int> tmp;

void bin(int n){
  tmp.clear();
  while(n){
    tmp.push_back(n%2);
    n/=2;
  }
}

int main(){
  int num[20];
  int t,n,c;
  int i,j,k;
  int flag;
  int ans,min;

  cin >> t;
  for(i=0;i<t;i++){
    cin >> n;
    ans = 0;
    min = 1000001;
    for(j=0;j<20;j++)num[j] = 0;

    for(j=0;j<n;j++){
      cin >> c;
      ans += c;
      if(min > c)min = c;
      bin(c);

      for(k=0;k<tmp.size();k++){
	if(tmp[k])num[k]++;
      }
    }

    flag = 1;
    for(j=0;j<20;j++){
      if(num[j]%2){
	flag=0;
	break;
      }
    }
    cout << "Case #" << i+1 << ": ";
    if(!flag)cout << "NO" << endl;
    else cout << ans-min << endl;
  }
}
