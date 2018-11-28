#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
using namespace std;
typedef long long ll;
int ans=INT_MAX;
map<vector<int> , int> memo;
bool ok(vector<int>& v){
	for(int i=0 ; i<v.size() ; i++){
		if(v[i]>i) return false;
	}
	return true;
}
int rec(vector<int> vl){
	set<vector<int> > vset;
	vector<vector<int> > v1,v2;
	if(ok(vl)) return 0;
	vset.insert(vl);
	v1.push_back(vl);
	for(int i=0 ; ; i++){
		//cout << "step:"<<i << endl;
		for(int j=0 ; j<v1.size() ; j++){
			for(int k=1 ; k<v1[j].size() ; k++){

				//for(int l=0 ; l<v1[j].size() ; l++) cout <<"["<<v1[j][l]<<"]";
				//cout << endl;
				swap(v1[j][k],v1[j][k-1]);
				if(ok(v1[j])) return i+1;
				if(vset.find(v1[j])==vset.end()){
					v2.push_back(v1[j]);
					vset.insert(v1[j]);
				}
				swap(v1[j][k],v1[j][k-1]);
			}
		}
		v1.clear();
		swap(v1,v2);
	}
}
int main(){
	int n;
	cin >> n;
	for(int i=0 ; i<n ; i++){
		vector<int> vl;
		int k;	cin >> k;
		for(int j=0 ; j<k ; j++){
			string s;
			cin >> s;
			int one=-1;
			for(int u=s.length()-1 ; u>=0; u--){
				if(s[u]=='1') {
					one=u;
					break;
				}
			}
			
			vl.push_back(one);
			
		}
		
		cout <<"Case #"<<i+1<<": "<<rec(vl)<<endl;
	}

}