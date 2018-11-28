#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define bits(x) __builtin_popcount(x)
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

bool up(char c){
	return 'A'<=c && c<='Z';
}

map<string,int> val;
map<string,vector<string> > adj;

int calc(string a){
	if (val.find(a)!=val.end()) return val[a];
	vector<int> list;
	FOR(it,adj[a]){
		list.push_back(calc(*it));
	}
	sort(all(list)); reverse(all(list));
	int i,res=0,tam=list.size();
	
	for (i=0;i<tam;i++) res=max(res,list[i]+i);
	res=max(res,1+tam);
	return val[a]=res;
}

int main(){
	int i,j,casos,c,n,a;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<c+1<<": ";
		adj.clear(); val.clear();
		cin>>n;
		
		string pri;
		for (i=0;i<n;i++){
			string tmp,cu;
			cin>>cu;
			if (i==0) pri=cu;
			cin>>a;
			
			for (j=0;j<a;j++){
				cin>>tmp;
				
				if (up(tmp[0])){
					adj[cu].push_back(tmp);
				}
			}
		}
		cout<<calc(pri)<<endl;
	}
	
	return 0;
}
