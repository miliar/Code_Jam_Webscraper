#include<iostream>

using namespace std;

int mapp[1000];
bool used[1000];

int main(){

  int T;
  cin>>T;
  for(int test=1;test<=T;test++){
    
    string a;
    cin>>a;
    int base=0;

    for(int i=0;i<1000;i++){
      used[i]=false;
      mapp[i]=-1;
    }
    
    for(int i=0;i<a.size();i++){
      if(!used[a[i]]){
	used[a[i]]=true;
	base++;
      }
    }
    if(base==1)base++;
    //cout<<base<<endl;
    mapp[a[0]]=1;
    int counter=0;
    for(int i=1;i<a.size();i++){
      if(mapp[a[i]]==-1){
	mapp[a[i]]=counter;
	if(counter==0)counter=2;
	else counter++;
      }
    }

    long long ans=0;long long mul=1;
    for(int i=a.size()-1;i>=0;i--){
      ans+=mapp[a[i]]*mul;
      mul*=base;
    }
    cout<<"Case #"<<test<<": "<<ans<<endl;
  }
    

}
