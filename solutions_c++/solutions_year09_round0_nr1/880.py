#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
int main() {
	int n,l,d;
	cin >> l >> d >> n;
	vector<string> v,vv;

	for(int i =0 ; i < d ; ++i) {
		string s;
		cin>>s;
		vv.push_back(s);
	}

	for(int i = 0 ; i < n ; ++i) {
		v.clear();
		for(int j = 0 ; j < vv.size(); ++j) {
			v.push_back(vv[j]);
		}
		string pat;
		cin>>pat;
		int state = 0;
		int ar[300] = {};
		int cnt = 0;
		for(int j = 0 ; j < pat.size(); ++j) {
			if(pat[j] == '(') {
				state = 1;
			} else if(pat[j] == ')'){
				state = 0;
			} else {
				ar[pat[j]] = 1;
			}
			if(!state) {
				vector<string> naya;
				for(int x = 0 ; x< v.size(); x++){
					if(ar[v[x][cnt]])naya.push_back(v[x]);
				}
				cnt++;
				v.clear();
				for(int x = 0 ; x < naya.size() ; ++x){
					v.push_back(naya[x]);
				}
				memset(ar,0,sizeof(ar));
			}

		}
		cout << "Case #" << i+1<<": "<<v.size()<<endl;
	}
	return 0;
}
