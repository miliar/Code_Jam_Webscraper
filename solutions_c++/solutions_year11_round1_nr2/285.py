#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <list>
#include <algorithm>

using namespace std;
typedef long long ll;
typedef vector<int> VI;
typedef vector<string> VS;

int dp[100][100][26], vis[100][300];
VS dict;
VI tmp[100];

void init(){
	memset(dp, 0, sizeof(dp));
	int n = dict.size();
	for(int i = 0; i < 26; ++i){
		for(int j = 0; j < n; ++j){
			tmp[j].clear();
			for(int k = 0; k < dict[j].size(); ++k){
				if(dict[j][k] == 'a' + i)
					tmp[j].push_back(k);
			}
		}
		for(int j = 0; j < n; ++j)
			for(int k = j + 1; k < n; ++k)
				if(tmp[j] == tmp[k])
					dp[j][k][i] = dp[k][j][i] = 1;
	}
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < dict[i].length(); ++j)
			vis[i][dict[i][j]] = 1;
}

int ls[200], N;
int calc(int id, string perm){
	int n, cnt = 0, sz = 0;
	
	for(int i = 0; i < N; ++i)
		if(i != id && dict[i].length() == dict[id].length()){
			ls[sz++] = i;
		}
	int posp[26];
	memset(posp, 0, sizeof(posp));
	//memset(vis, 0, sizeof(vis));
	for(int i = 0; i < perm.size(); ++i){
		posp[perm[i] - 'a'] = i;
	}
	n = posp[dict[id][0] - 'a'];
	for(int i = 0; i < dict[id].length(); ++i){
		if(n < posp[dict[id][i] - 'a']){
			n = posp[dict[id][i] - 'a'];
		}
	}
	for(int i = 0; i < n; ++i){
		if(sz == 0)break;
		if(!vis[id][perm[i]]){
			int flag = 1;
			for(int j = 0; j < sz; ++j)
				if(vis[ls[j]][perm[i]])flag = 0;
			if(flag)continue;
			++cnt;	//
			for(int j = 0; j < sz; ++j){
				if(vis[ls[j]][perm[i]]){
					ls[j] = ls[--sz];
					--j;
				}
			}
		}else {
			for(int j = 0; j < sz; ++j){
				if(!dp[id][ls[j]][perm[i] - 'a']){
					ls[j] = ls[--sz];
					--j;
				}
			}
		}
	}
	return cnt;
}

VS p;

int main()
{
	int T, n, m, id, wr;
	cin>>T;
	string str, perm;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n>>m;
		N = n;
		dict.clear();
		for(int i = 0; i < n; ++i){
			cin>>str;
			dict.push_back(str);
		}
		init();
		cout<<"Case #"<<tt<<":";
		for(int i = 0; i < m; ++i){
			cin>>perm;
			id = wr = 0;
			for(int j = 0; j < n; ++j){
				int t = calc(j, perm);
				//cout<<"j = "<<j<<' '<<t<<endl;
				if(t > wr){
					wr = t;
					id = j;
				}
			}
			cout<<' '<<dict[id];
		}
		cout<<endl;
	}
	return 0;
}


		
