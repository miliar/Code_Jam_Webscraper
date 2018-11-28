#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  int T,tt=1;
  cin>>T;
  while(T--){
    int C,D,p1,v1;
    cin>>C>>D;
    vector<int> pos;
    for (int i=0;i<C;i++){
      cin>>p1>>v1;
      for (int j=0;j<v1;j++){
	pos.push_back(p1);
      }
    }
    sort(pos.begin(),pos.end());
    double mintime=0;
    int curpos=pos[0];
    for (int i=1;i<pos.size();i++){
      mintime = max(mintime,(curpos+D-pos[i])/2.0);
      curpos = max(pos[i],curpos+D);
    }
    cout<<"Case #"<<tt++<<": "<<mintime<<endl;
  }
}
      

      
