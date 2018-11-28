#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
  int T; cin >> T;
  for(int t=0;t<T;++t){
	int R,C;cin>>R>>C;
	vector<string> pict(R);
	for(int i=0;i<R;++i) cin>>pict[i];
	
	for(int i=0;i<R-1;++i)
	  for(int j=0;j<C-1;++j){
		if(pict[i][j]!='#') continue;
		bool f=true;
		if(pict[i][j+1]!='#') f=false;
		if(pict[i+1][j]!='#') f=false;
		if(pict[i+1][j+1]!='#') f=false;
		if(f){
		  pict[i][j] = pict[i+1][j+1] = '/';
		  pict[i+1][j] = pict[i][j+1] = '\\';
		}
	  }

	bool flag=true;
	for(int i=0;i<R;++i)
	  for(int j=0;j<C;++j)
		if(pict[i][j]=='#'){
		  flag=false;
		  break;
		}
	cout<<"Case #"<<t+1<<":"<<endl;
	if(!flag){
	  cout<<"Impossible"<<endl;
	}else{
	  for(int i=0;i<R;++i){
		cout<<pict[i]<<endl;
	  }
	}
  }
  return 0;
}

