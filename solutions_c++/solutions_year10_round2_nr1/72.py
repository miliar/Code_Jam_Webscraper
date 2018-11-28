#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <iostream>

using namespace std;

typedef vector<int> vi;
map<string,int> msi;
map<vi,int> mvi;

int main()
{
	int cases;
	cin >> cases;
	for(int iii=1; iii<=cases; ++iii){
		mvi.clear();
		msi.clear();
		mvi[vector<int>()] = 0;
		int isi = 0;
		int n, m;
		cin >> n >> m;
		int res = 0;
		for(int i=0; i<n; ++i){
			string s, t;
			cin >> s;
			vi v;
			int j = 0;
			while(j < s.size()){
				if(s[j] == '/') j++;
				t = "";
				while(j < s.size() && s[j] != '/'){
					t += s[j];
					++j;
				}
				if(msi.find(t) == msi.end()){
					msi[t] = isi++;
				}
				v.push_back(msi[t]);
			}
			mvi[v] = 0;
		}
		for(int i=0; i<m; ++i){
			string s, t;
			cin >> s;
			vi v;
			int j = 0;
			while(j < s.size()){
				if(s[j] == '/') j++;
				t = "";
				while(j < s.size() && s[j] != '/'){
					t += s[j];
					++j;
				}
				if(msi.find(t) == msi.end()){
					msi[t] = isi++;
				}
				v.push_back(msi[t]);
				if(mvi.find(v) == mvi.end()) res++;
				mvi[v] = 0;
			}
		}
		cout << "Case #" << iii << ": " << res << endl;
	}
	return 0;
}
