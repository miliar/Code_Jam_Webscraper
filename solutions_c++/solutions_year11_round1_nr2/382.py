#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

#define infile "1.in"
#define outfile "1.out"

#define maxn 10100

int n, m;
string l;
vector<string> d;
bool can[maxn];
int num;

int solvecase2(string s){
	int ans = 0;	
	for(int i=0; i<n; i++){
		can[i] = s.length()==d[i].length();
	}
	for(int i=0; i<26; i++){
		char c = l[i];
		bool f = false;
		for(int j=0; j<n; j++)if(can[j] && d[j].find(c)!=string::npos)
			f = true;
		if(!f) continue;
		if(s.find(c)==string::npos){
			ans++;
			for(int j=0; j<n; j++)if(can[j] && d[j].find(c)!=string::npos)
				can[j] = false;
		}else{
			for(int j=0; j<s.length(); j++){
				if(s[j]==c){
					for(int k=0; k<n; k++)if(can[k]){
						can[k] = d[k][j]==c;
					}
				}
				else{
					for(int k=0; k<n; k++)if(can[k] && d[k][j]==c){
						can[k] = false;
					}
				}
			}
		}
	}	
	return ans;	
}

string solvecase(){
	int max = -1;
	string ans;
	for(int i=0; i<n; i++){
		int p = solvecase2(d[i]);
		if(max < p){
			max = p;
			ans = d[i];
		}
	}
	return ans;
}

void solve(){
	int t;
	cin >> t;
	for(int i=0; i<t; i++){
		cout << "Case #" << i+1 << ": ";
		cin >> n >>  m;
		d.clear();
		for(int j=0; j<n; j++){
			string s;
			cin >> s;
			d.push_back(s);
		}
		for(int j=0; j<m; j++){
			cin >> l;
			if(j!=0) cout << " ";
			cout << solvecase();
		}	
		cout << endl;
	}
}

int main(){
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);
	solve();
	return 0;
}