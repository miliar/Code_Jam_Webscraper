#include <iostream>
#include <string>
#include <vector>
using namespace std;
const int MAXN = 11000;
struct node{
	string str;
	vector<int> child;
} data[MAXN];

int ans, total;
void insert(const vector<string>& vec, int from, int root, bool add){
	if (from == vec.size()) return;
	vector<int>& children = data[root].child;
	int pos = -1;
	for (int i = 0; i < children.size(); ++i){
		if (data[children[i]].str == vec[from]){
			pos = children[i];
			break;
		}
	}
	if (pos == -1){
		data[++total].str = vec[from];
		children.push_back(total);
		if (add) ++ans;
		insert(vec, from + 1, total, add);
	} else {
		insert(vec, from + 1, pos, add);
	}
}
vector<string> split(string str){
	str = str.substr(1);
	int pos;
	vector<string> ret;
	while ((pos = str.find('/')) != string::npos){
		ret.push_back(str.substr(0, pos));
		str = str.substr(pos + 1);
	}
	ret.push_back(str);
	return ret;
	
}
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0;  tt < cases; ++tt){
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < MAXN; ++i) data[i].child.clear();
		ans = total = 0;
		for (int i = 0; i < n; ++i){
			string str;
			cin >> str;
			vector<string> name = split(str);
			insert(name, 0, 0, false);
		}
		for (int i = 0; i < m; ++i){
			string str;
			cin >> str;
			vector<string> name = split(str);
			insert(name, 0, 0, true);
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
}