#include<iostream>
#include<vector>
#include<string>
#include<map>
#define INF 100000000

using namespace std;

vector<string> se(0);
map<string,int> se_map;
vector<int> que(0);
int lr[2000][2000];
int main() {
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int n;
	cin >> n;
	for(int i=0;i<n;++i) {
		se.clear();
		se_map.clear();
		que.clear();
		int s,q;
		cin >> s;
		string tmp;
		getline(cin, tmp);
		for(int j=0;j<s;++j) {
			string word;
			getline(cin, word);
			se.push_back(word);
			se_map[word]=j;
		}
		cin >> q;
		getline(cin, tmp);
		for(int j=0;j<q;++j) {
			string word;
			getline(cin, word);
			que.push_back(se_map[word]);
		}
		
		if (q==0) {
			cout << "Case #" << (i+1) << ": " << 0 << "\n";
			continue;
		}
		
		for(int j=0;j<s;++j)
			if (que[0]==j) lr[0][j]=INF;
			else lr[0][j]=0;
		
		for (int j=1;j<q;++j) {
			for(int k=0;k<s;++k) {
				lr[j][k]=INF;
				if (que[j]!=k) {
					for(int l=0;l<s;++l) {
						if (l==k) lr[j][k]=min(lr[j][k],lr[j-1][l]);
						else lr[j][k]=min(lr[j][k],lr[j-1][l]+1);
					}
				}
			}
		}
		
		int res=INF;
		for(int j=0;j<s;++j) {
			res=min(res,lr[que.size()-1][j]);
		}
		
		cout << "Case #" << (i+1) << ": " << res << "\n";
	}
}