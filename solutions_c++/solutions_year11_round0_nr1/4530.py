#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){

  int n,t;
  while(cin >> n){
    for(int i=0;i<n;i++){
      cin >> t;
      vector<pair<int,int> > blue,orange;
      blue.clear(),orange.clear();
      string tmp;
      int tmp2;
      for(int j=0;j<t;j++){
        cin >> tmp >> tmp2;
        if(tmp[0]=='B')
          blue.push_back(make_pair(j,tmp2-1));
        else
          orange.push_back(make_pair(j,tmp2-1));
      }
      blue.push_back(make_pair(-1,-1));
      orange.push_back(make_pair(-1,-1));
      int bnow=0,onow=0,bflag=0,oflag=0;
      int bcounter=0,ocounter=0,counter=0;
      int ans=0;
      while(counter!=t){
        bflag=0,oflag=0;
        if(blue[bcounter].second>bnow)
          bnow++;
        else if(blue[bcounter].second<bnow)
          bnow--;
        else {
          if(counter==blue[bcounter].first){
            bcounter++;
            counter++;
            bflag=1;
            //      cout << "bpush ";
          }
        }

        if(orange[ocounter].second>onow)
          onow++;
        else if(orange[ocounter].second<onow)
          onow--;
        else {
          if(!bflag)
            if(counter==orange[ocounter].first){
              ocounter++;
              counter++;
              //cout << "opush ";
            }
        }
        //      cout << bnow+1 << " " << onow+1  << endl;
        ans++;
      }
      cout << "Case #" << i+1 << ": " << ans << endl;
    }
  }
  return 0;
}
