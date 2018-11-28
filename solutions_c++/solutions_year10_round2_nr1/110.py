#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;


struct Ch{
	int u;
	string ss;
	Ch(){}
	Ch(int uu, string s){
		u = uu, ss = s;
	}
	int operator<(const Ch &t) const{
		if (u == t.u)return ss < t.ss;
		return u < t.u;
	}
};

map<Ch, int> mp;
map<Ch, int>::iterator it;

char cstr[110];
string str;

int main(){
	freopen("/home/liang/桌面/A-large.in", "r", stdin);
	freopen("ans.out", "w", stdout);
	int n, m, T, cas = 1;
	int i, j;
	int u, v, ncnt;
	int len;
	scanf("%d", &T);
	while (T--){
		scanf("%d %d", &n, &m);
		mp.clear();
		ncnt = 1;
		
		for (i = 0; i < n; i++){
			scanf("%s", cstr);
			len = strlen(cstr);
			str = "";
			j = 1;
			u = 0;
			while (j < len){
				while (j < len && cstr[j] != '/'){
					str += cstr[j];
					j++;
				}
				it = mp.find(Ch(u, str));
				if (it == mp.end()){
					v = mp[Ch(u, str)] = ncnt++;
				}
				else v = it->second;

				u = v;
				j++;
			}
		}

		int ans = 0;
		for (i = 0; i < m; i++){
			scanf("%s", cstr);
			len = strlen(cstr);
			str = "";
			j = 1;
			u = 0;
			while (j < len){
				while (j < len && cstr[j] != '/'){
					str += cstr[j];
					j++;
				}
				it = mp.find(Ch(u, str));
				if (it == mp.end()){
					v = mp[Ch(u, str)] = ncnt++;
					ans++;
				}
				else v = it->second;

				u = v;
				j++;
			}
		}

		printf("Case #%d: %d\n", cas++, ans);
	}
	return 0;
}



