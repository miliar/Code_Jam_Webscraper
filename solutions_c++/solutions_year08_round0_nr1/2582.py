#include<iostream>
#include<vector>
#include<string>

using namespace std;
int s,q;
string test;

int main(){
	int tc;
	cin>>tc;
	for(int p=0;p<tc;p++){
		cin>>s;
		getline(cin,test);
		vector<string> S = vector<string>(100);
		for(int i=0;i<s;i++) {
			getline(cin,S[i]);
		}
		string temp;
		vector<int> P = vector<int>(1000);
		cin>>q;
		getline(cin,test);
		for(int i=0;i<q;i++){
			getline(cin,temp);
			int j=0;
			for(j=0;j<s;j++){
				if(temp.compare(S[j])==0) {
					P[i]=j;
					break;
				}
			}
		}
		int ret = 0;
		int seen = 0;
		vector<bool> Q = vector<bool>(100,false);
		for(int i=0;i<q;i++){
			if(Q[P[i]]) continue;
			Q[P[i]]=true;
			seen++;
			if(seen==s){
				ret++;
				seen=1;
				for(int j=0;j<s;j++) Q[j]=false;
				Q[P[i]]=true;
			}
		}
		cout<<"Case #"<<(p+1)<<": "<<ret<<endl;
	}
	return 0;
}



