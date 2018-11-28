#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef unsigned long long ULL;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int tests;
	scanf("%d\n",&tests);
	for (int ttt = 0; ttt < tests; ttt++){
		int n = 0,m = 0;
		int mkdirs = 0;
		scanf("%d %d\n",&n,&m);
		//vector<string> roots;
		map<string,bool> roots;
		for (int i = 0; i < n; i++){
			string temp;
			cin >> temp;
			roots[temp] = true;
		}
		vector<string> dirs;
		dirs.resize(m);
		for (int i = 0; i < m; i++)
			cin >> dirs[i];
		sort(dirs.begin(),dirs.end());
		for (int i = 0; i < m; i++){
			string t = dirs[i];
			int l = t.length();
			int count = 0;
			for (int j = 0; j < l; j++){
				if (t[j] == '/')
					count++;
			}
			vector<string> mas;
			mas.resize(count);
			int p = 0;
			int k = 0;
			for (int j = 1; j < l; j++){
				if (t[j]=='/'){
					mas[k++] = t.substr(p,j-p);
					p = j;
				}
			}
			mas[k] = t.substr(p,l-p);
			string temp = mas[0];
			if (roots[temp] == false){
				roots[temp] = true;
				mkdirs++;
			}
			for (int j = 1; j < count; j++){
				temp += mas[j];
				if (roots[temp]==false){
					roots[temp] = true;
					mkdirs++;
				}
			}
		}
		printf("Case #%d: %d\n",ttt+1,mkdirs);
	}
	return 0;
}