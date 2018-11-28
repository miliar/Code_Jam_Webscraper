#include<iostream>
#include<vector>
#include<string>

using namespace std;

bool thc(char a1,char a2,char b1,char b2){
	if(a1==b1&&a2==b2)return true;
	if(a1==b2&&a2==b1)return true;
	return false;
}

int main(){
	int T;
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		int C,D,N;
		cin>>C;
		vector<string> combine(C);
		for(int i=0;i<C;i++)
			cin>>combine[i];
		cin>>D;
		vector<string> opposed(D);
		for(int i=0;i<D;i++)
			cin>>opposed[i];
		cin>>N;
		string invoke;
		cin>>invoke;
		
		vector<char> ans;
		
		for(int i=0;i<N;i++){
			if(ans.size()==0){
				ans.push_back(invoke[i]);
			}else{
				
				bool flag=true;
				
				for(int j=0;j<C&&flag;j++){
					if(thc(ans.back(),invoke[i],combine[j][0],combine[j][1])){
						//cheak
						ans.back()=combine[j][2];
						flag=false;
					}
				}
				
				if(flag){
					bool flag2=true;
					for(int k=0;k<ans.size()&&flag2;k++){
						for(int j=0;j<D&&flag2;j++){
							if(thc(ans[k],invoke[i],opposed[j][0],opposed[j][1])){
								ans.clear();
								flag2=false;
							}
						}
					}
					
					if(flag2)
						ans.push_back(invoke[i]);
					
				}
			}
		}
		
		cout<<"Case #"<<tc<<": [";
		for(int i=0;i<ans.size();i++){
			if(i!=0)cout<<", ";
			cout<<ans[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
