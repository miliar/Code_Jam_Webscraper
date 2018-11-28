#include<iostream>
#include<vector>
using namespace std;

int main(){
  int cnt;
  cin>>cnt;

  for(int i=0;i<cnt;i++){
    vector<int> v;int ans=0;
    int N,S,P;
    cin>>N>>S>>P;
    for(int j=0;j<N;j++){
      int a;cin>>a;v.push_back(a);
    }
    for(int k=0;k<v.size();k++){
      if(v[k]==0 && P!=0){continue;}
      else if(v[k]==0 && P==0){ans++;continue;}

      if(v[k]/3>=P){ans++;}
      else{
	if(v[k]%3==0 && v[k]/3+1>=P && S>0){ans++;S--;}
	else if(v[k]%3==1 && v[k]/3+1>=P){ans++;}
	else if(v[k]%3==2 && v[k]/3+1>=P){ans++;}
	else if(v[k]%3==2 && v[k]/3+2>=P && S>0){ans++;S--;}
      }
    }
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }

  return 0;
}
