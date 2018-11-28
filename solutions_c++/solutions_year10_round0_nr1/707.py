#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
long long v;
int main(){
  int t;
  cin >> t; int x;
  for(x=0;x<t;x++){
    int n,k;
    bool flg=false;
    cin >> n >> k;
    v=((long long)1<<n)-1;
    while(k>=v){
      k-=v;
      if(k==0)flg=true;
      k--;
    }
    printf("Case #%d: ",x+1);
    if(flg==false)
      cout << "OFF" << endl;
    else
      cout << "ON" << endl;
  }
  return 0;
}
