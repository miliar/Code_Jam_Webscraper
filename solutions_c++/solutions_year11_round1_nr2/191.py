#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<sstream>
#include<string>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<numeric>
#include<climits>
using namespace std;
typedef long long ll;
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

double eps = 1e-9;
int cmp(double a, double b = 0){
	return a + eps < b ? -1 : a - eps > b ? 1 : 0;
}
int n, m;
string D[10000];
string L[100];
int best[100];
int res[100];
set<int> esta[26];
vector<int> part[11];
int in[10000];

void cuenta(string& fix, int ind){
	vector<int>& p = part[fix.size()];
	int arr[26];
	int arr2[26];
	int cnt[26];
	int sum[26];
	
	for(int i = 0; i < 26; i++) cnt[i] = 0, esta[i].clear();
	
	for(int i = 0; i < fix.size(); i++)  cnt[fix[i] - 'a']++; 
	;
	for(int i = 0; i < p.size(); i++){
		for(int j = 0; j < 26; j++) arr[j] = arr2[j] = 0;

		for(int j = 0; j < fix.size(); j++){
			arr2[D[p[i]][j] - 'a']++;
			if(fix[j] == D[p[i]][j])
				arr[fix[j] - 'a']++;
		}

		for(int j = 0; j < 26; j++) if(cnt[j] == arr[j] && cnt[j] == arr2[j])
			esta[j].insert(p[i]);
	}

	for(int a = 0; a < m; a++){
		string l = L[a];
		int sz = p.size();
		for(int i = 0; i < 26; i++) sum[i] = 0;
		
		for(int i = 0; i < sz; i++){
			in[i] = p[i];
			for(int j = 0; j < D[in[i]].size(); j++)
				sum[D[in[i]][j] - 'a']++;
		}
		
		int reps = 0;
		for(int i = 0; i < 26; i++)if(sz > 1){
			int c = l[i] - 'a';
			int it = 0;
			if(sum[c] && cnt[c] == 0) reps++;
			for(int j = 0; j < sz; j++)
				if(esta[c].count(in[j]))
					in[it++] = in[j];
				else
				  for(int k = 0; k < D[in[j]].size(); k++)
				  	sum[D[in[j]][k] - 'a']--;
			sz = it;
		} 
		if(reps > best[a]) best[a] = reps, res[a] = ind;
	}
	
}

int main(){
	int tt; cin >> tt;
	for(int caso = 1; caso <= tt; caso++){
		cin >> n >> m;

		cout << "Case #" << caso << ":";
		for(int i = 0; i < 11; i++) part[i].clear();
		
		for(int i = 0; i < n; i++){
			cin >> D[i];
			part[D[i].size()].push_back(i);
		}
		
		for(int i = 0; i < m; i++){
			cin >> L[i];
			best[i] = -1;
		}

		for(int i = 0; i < n; i++)
			cuenta(D[i], i);
			
		for(int i = 0; i < m; i++)
			cout << " " << D[res[i]];
		
		cout << endl;
	}
}
