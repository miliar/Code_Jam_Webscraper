#include<iostream>
#include<vector>

using namespace std;
int main(){
  int tt;
  cin>>tt;
  for(int t=0;t<tt;++t){
	int n; cin>>n;
	vector<int> vi;
	while(n--){
	  int i; cin>>i;
	  vi.push_back(i);
	}
	int m = -1;
	
	for(int i=1;i<(1<<vi.size())-2;++i){
	  //cout<<i<<endl;
	  int sum1=0, sum2=0, sum1b=0, sum2b=0;
	  for(int k=0;k<vi.size();++k){
		if(i&(1<<k)){
		  sum1 += vi[k];
		  sum1b ^= vi[k];
		}else{
		  sum2 += vi[k];
		  sum2b ^= vi[k];
		}
	  }
	  if(sum1b==sum2b){
		m = (sum1>m?sum1:m);
		m = (sum2>m?sum2:m);
	  }
	}
	
	/*
	for(int k=1;k<vi.size()-1;++k){
	  int sum1=0,sum2=0,sum1b=0,sum2b=0;
	  for(int j=0;j<vi.size();++j){
		if(j<k){
		  sum1 += vi[j];
		  sum1b ^= vi[j];
		}else{
		  sum2 += vi[j];
		  sum2b ^= vi[j];
		}
	  }
	  if(sum1b==sum2b){
		m = (sum1>m?sum1:m);
		m = (sum2>m?sum2:m);
	  }
	}
	*/
	cout<<"Case #"<<t+1<<": ";
	if(m==-1) cout<<"NO";
	else cout<<m;
	cout<<endl;
  }
  return 0;
}
