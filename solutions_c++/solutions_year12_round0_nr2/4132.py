#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int t,N,P,S,res;
	vector<int> v;
	cin>>t;
	for(int T=1;T<=t;T++){
		v.clear();
		cin>>N>>S>>P;
		while(N--){
			cin>>res;
			v.push_back(res);
		}
		res=0;
		sort(v.begin(),v.end(),greater<int>());
		for(int i=0;i<v.size();i++){
			if((v[i]-3*P+2)>=0){
				res++;
				continue;
			}
			if(P>1&&(v[i]-3*P+4)>=0 && S>0){
				res++;
				S--;
				continue;
			}
			break;
		}
		cout<<"Case #"<<T<<": "<<res<<endl;
	}
	return 0;
}