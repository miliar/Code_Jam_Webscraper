
#include <iostream>
#include <string>
#include <set>
using namespace std;

int main(){
	int nn;
	cin>>nn;
	for(int npr=1;npr<=nn;npr++){
		int n;
		cin>>n;
		cin.ignore();
		string str;
		set<string> engine;
		for(int i=0;i<n;i++){
			getline(cin,str);
			engine.insert(str);
		}
		int q;
		int ans=0;
		cin>>q;
		cin.ignore();
		set<string> used;
		for(int i=0;i<q;i++){
			getline(cin,str);
			if(engine.find(str)==engine.end())continue;
			used.insert(str);
			if(used.size()==n){
				ans++;
				used.clear();
				used.insert(str);
			}
		}
		cout<<"Case #"<<npr<<": "<<ans<<endl;
	}
	return 0;
}
