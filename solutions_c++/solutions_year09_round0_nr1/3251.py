#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <iterator>
#include <fstream>

using namespace std;

bool
check(string s1, string s2, int p){
	for(int i = 0; i < p; i++){
		if(s1[i] != s2[i]) return false;
	}
	return true;
}

int
calc(vector<string>& s, vector<vector<char> >& v, int p, int l, string ss){
	
	if(p >= l){
		for(int i = 0; i < s.size(); i++){
			if(check(s[i], ss, ss.size())) return 1;
		}
		return 0;
	}

	bool f = false;
	int ans = 0;

	for(int i = 0; i < v[p].size(); i++){
		for(int j = 0; j < s.size(); j++){
			//if(v[p][i] == (*itr)[p]) f = true;

			if(check(ss+v[p][i], s[j], p+1)){
				f = true;
				break;
			}

		}
		if(f){
			ans += calc(s, v, p+1, l, ss + v[p][i]);
		}
	}

	return ans;

}

int
main()
{
	int l, d, n;
	string st;
	vector<string> s;
	
	cin>>st;
	ifstream fin(st.c_str());
	cin>>st;
	ofstream fout(st.c_str());


	fin>>l>>d>>n;
	for(int i = 0; i < d; i++){
		fin>>st;
		s.push_back(st);
	}

	for(int i = 0; i < n; i++){
		vector<vector<char> > v(l);
		int p = 0;
		bool flg = false;

		fin>>st;
		for(int j = 0; j < st.size(); j++){
			switch(st[j]){
				case '(':
					flg = true;	break;
				case ')':
					p++; flg = false; break;
				default:
					v[p].push_back(st[j]);
					if(!flg) p++;
					break;
			}
		}

		fout<<"Case #"<<i+1<<": "<<calc(s, v, 0, l, "")<<endl;
	}
	

}