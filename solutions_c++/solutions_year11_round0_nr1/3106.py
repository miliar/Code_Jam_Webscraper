#include <iostream>
using namespace std;

int a[2][121];

int main(){
  int t,x, n, size[2],time[2];
  char c;
  cin >> t;
  int mp[256], mode,sum,last;
  mp['O'] = 0;
  mp['B'] = 1;
  int kase = 1;
  while(t--){
    cin >> n;        
    sum=0;
    a[0][0] = a[1][0] = 1;   
    size[0]=size[1]=1;
    time[0]=time[1]=0,last;
    for(int i =0; i < n; i++){
      cin >> c >> x;
      mode = mp[c];
      a[mode][size[mode]] = x;
      if(i!=0 && last != mode){
        sum = max(abs(x-a[mode][size[mode]-1])+1+time[mode], sum+1);
      }
      else{
        sum += abs(x-a[mode][size[mode]-1])+1;   
      }
      time[mode] = sum;
      size[mode]++;
      last = mode;
    }
    cout << "Case #" << kase++ << ": " << sum << endl;
  }
  return 0;    
}
