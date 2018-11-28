#include<cstdio>
#include<cstring>
#include<string>
#include<queue>
#include<set>
#include<cmath>
#include<iostream>
using namespace std;
char d[10010][11], dic[26];
int total[10010];
vector<int> dd[10010][26];
bool isEquals(int a, int b, char c) {
	if (dd[a][c - 'a'].size() != dd[b][c - 'a'].size()) return false;
	int i, n = dd[a][c - 'a'].size();
	for (i = 0; i < n; i++) {
		if(dd[a][c - 'a'][i] != dd[b][c - 'a'][i]) return false;
	}
	return true;
}
int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int T, t, i, j, k;
	scanf("%d", &T);

	
	for(t = 1; t <= T; t++){
		int n, m;
		memset(dd, 0, sizeof(dd));
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) {
			scanf("%s", d[i]);
			total[i] = strlen(d[i]);
			for (j = 0; d[i][j]; j++)
				dd[i][d[i][j] - 'a'].push_back(j);
		}
		printf("Case #%d: ", t);
		for (i = 0; i < m; i++) {
			scanf("%s", dic);
			vector<int> list;
			int ans = -1, index = -1;
			for (j = 0; j < n; j++) {
				list.clear();
				for (k = 0; k < n; k++) {
					if (k != j && total[j] == total[k])
						list.push_back(k);
				}
				//cout<<list.size()<<endl;
				int tmp = 0;
				for (k = 0; dic[k] && !list.empty(); k++) {
					vector<int> newList;
					int kk;
					for (kk = 0; kk < list.size(); kk++) {
						if (dd[list[kk]][dic[k] - 'a'].size() != 0)
							break;
					}
					
					if (kk == list.size() && dd[j][dic[k] - 'a'].size() == 0)
						continue;
					else if (kk != list.size() && dd[j][dic[k] - 'a'].size() == 0) {
						tmp++;
					}
					else if (kk == list.size() && dd[j][dic[k] - 'a'].size() != 0)
						break;
					for (kk = 0; kk < list.size(); kk++) {
						if (isEquals(list[kk], j, dic[k]))
							newList.push_back(list[kk]);
					}
					list = newList;
				}
				if (tmp > ans) {
					//cout<<tmp<<endl;
					ans = tmp;
					index = j;
				}
			}
			//cout<<ans<<endl;
			if (i == 0) printf("%s", d[index]);
			else printf(" %s", d[index]);
		}
		printf("\n");
	}
	return 0;
}
