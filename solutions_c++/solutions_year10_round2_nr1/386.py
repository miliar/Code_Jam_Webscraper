#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct Directory
{
	string name;
	vector<Directory*> children;
	
	Directory(string str)
	{
		name = str;
	}
	~Directory()
	{
		for(int i = 0; i < children.size(); i++)
		{
			delete children[i];
		}
	}
	
	int Add(string path)
	{
		string::size_type pos = path.find('/');
		if(pos == string::npos)
			return 0;
		for(int i = 0; i < children.size(); i++)
		{
			if(children[i]->name == path.substr(0, pos))
			{
				return children[i]->Add(path.substr(pos+1));
			}
		}
		children.push_back(new Directory(path.substr(0, pos)));
		return children.back()->Add(path.substr(pos+1)) + 1;
	}
};

int main()
{
	int T;
	cin >> T;
	for(int No = 1; No <= T; No++)
	{
		int N, M;
		cin >> N >> M;
		Directory* root = new Directory("");
		for(int i = 0; i < N; i++)
		{
			string str;
			cin >> str;
			str = str.substr(1) + "/";
			root->Add(str);
		}
		int ans = 0;
		for(int i = 0; i < M; i++)
		{
			string str;
			cin >> str;
			str = str.substr(1) + "/";
			ans += root->Add(str);
		}
		cout << "Case #" << No << ": " << ans << endl;
	}
	return 0;
}
