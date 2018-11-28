#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
struct Node {
	Node(){}
	string name;
	vector<Node> son;
	
};
int ans;
void maketree(Node& root, string s)
{
	if(s.length() == 0) return ;
	int i;
	for(i = 1; i < s.length(); i++) if(s[i] == '/') break;
	string name = s.substr(0, i);
	for(int k = 0; k < root.son.size(); k++)
	{
		if(root.son[k].name == name)
		{
			s = s.substr(i);
			maketree(root.son[k], s);
			return;
		}
	}
	Node tmp;
	ans++;
	tmp.name = name;
	root.son.push_back(tmp);
	s = s.substr(i);
	maketree(root.son[root.son.size()-1], s);
}
bool find(Node& root, string s)
{
	if(s.length() == 0) return true;
	int i;
	for(i = 1; i < s.length(); i++) if(s[i] == '/') break;
	string name = s.substr(i);
	for(int k = 0; k < root.son.size(); k++)
	{
		if(root.son[k].name == name)
		{
			s = s.substr(i);
			return find(root.son[k], s);
		}
	}
	return false;

}
int main()
{
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin>>T;

	int Case;
	for(Case = 1; Case <= T; Case++)
	{
		int N, M;
		cin>>N>>M;
		Node root;
		int i;
		for(i = 0; i < N; i++)
		{
			string s;
			cin>>s;
			maketree(root, s);
		}
		ans = 0;
		for(i = 0; i < M; i++)
		{
			string s;
			cin>>s;
			if(find(root, s))
			{
				continue;
			}
			else
			{
				//ans++;
				maketree(root, s);
			}
		}
		printf("Case #%d: %d\n", Case, ans);
	}
	return 0;
}