#include<iostream>
#include<string>
#include<set>

using namespace std;


int main(){
  int T;
  cin>>T;
  int round=0;
  while(T--){
    round++;
    int N,M;
    cin>>N>>M;
    set<string> P;
    set<string> W;
    // cout<<"path"<<endl;
    for(int i=0;i<N;i++){
      string tmp;
      cin>>tmp;
      string tpath="";
      for(int j=1;j<(int)tmp.size();j++){

	if(tmp[j]=='/'||j==(int)tmp.size()-1){
	  if(j==(int)tmp.size()-1){
	    tpath=tpath+tmp[j];
	  }
	  P.insert(tpath);
	  //  cout<<tpath<<endl;
	}
	tpath=tpath+tmp[j];
      }
    }
    //    cout<<"want"<<endl;
    for(int i=0;i<M;i++){
      string tmp;
      cin>>tmp;
      string tpath="";
      for(int j=1;j<(int)tmp.size();j++){
	
	if(tmp[j]=='/'||j==(int)tmp.size()-1){
	  
	  if(j==(int)tmp.size()-1){
	    tpath=tpath+tmp[j];
	  }
	  W.insert(tpath);
	  //	  if(j==(int)tmp.size())cout<<"end"<<endl;
	  //  cout<<tpath<<endl;
	}
	tpath=tpath+tmp[j];
      }
    }
    set<string>::iterator witr,pitr;
    witr=W.begin();
    pitr=P.begin();
    int ans=0;
    for(set<string>::iterator itr=witr;itr!=W.end();itr++){
      if(P.find(*itr)==P.end()){
	ans++;
      }
    }
    cout<<"Case #"<<round<<": "<<ans<<endl;
  }
  return 0;
}
