#include<iostream>
#include<vector>
#include<set>

using namespace std;

int main(){
	int cases; cin>>cases;
	for(int num=1;num<=cases;num++){
		int S; cin>>S;
		cin.get();
		
		vector<string> es(S);
		for(int i=0;i<S;i++){
			getline(cin,es[i]);
		}
	//	for(int i=0;i<S;i++) cerr<<es[i]<<'#';
	//	cerr<<endl;
		
		int Q; cin>>Q;
		cin.get();
		
		set<string> ap;
		int res=0;
		for(int i=0;i<Q;i++){
			string s; getline(cin,s);
			
			ap.insert(s);
			if(ap.size()==S){
				res++;
				ap.clear();
				ap.insert(s);
			}
		}
		
		cout<<"Case #"<<num<<": "<<res<<endl;
	}
	
	return 0;
}
