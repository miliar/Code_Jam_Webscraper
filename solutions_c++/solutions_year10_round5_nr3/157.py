#include<string.h>
#include<math.h>
#include<vector>
#include<map>
#include<iostream>
using namespace std;
int main(){
	int times;
	cin>>times;
	for(int tm=1;tm<=times;tm++){
		cout<<"Case #"<<tm<<": ";
		int n,a,b;
		cin>>n;
		map<int,int> M;
		for(int i=0;i<n;i++){
			cin>>a>>b;
			M[a]=b;
		}
		int ans=0;
		bool done=0;
		while(!done){
			done=1;
			for(map<int,int>::iterator it=M.begin();
					it!=M.end();it++){
				if(it->second>1){
					a=it->first;
					b=it->second;
					ans+=b/2;
					M[a-1]+=b/2;
					M[a+1]+=b/2;
					it->second=b%2;
					done=0;
				}
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
