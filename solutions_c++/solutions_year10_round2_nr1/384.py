/**
#include<iostream>
#include<vector>
#include<string>

using namespace std;

struct Node {
	vector<Node> children;
	string name;
};

int N, M;
Node root;
vector<string> dirList;
int count;

Node * addChildNode(Node * fatherNode, string childName)
{
	for(int i = 0; i < fatherNode->children.size(); i ++) {
		if(fatherNode->children[i].name == childName) return &(fatherNode->children[i]);
	}

	count ++;
	Node newChild = Node();
	newChild.name = childName;
	fatherNode->children.push_back(newChild);
	
	return &(fatherNode->children[fatherNode->children.size()-1]);
}

int addDirs()
{
	Node *currentRoot = &root;

	for(int i = 0; i < dirList.size(); i ++) {
		currentRoot = addChildNode(currentRoot, dirList[i]);
	}
	
	return count;
}

int splitDirs(string path)
{
	int count = 0;
	int level = 0;
	string dir = "";
	int i = 1;
	while(i < path.length()){
		dir = "";
		for(; i < path.length(); i ++) {
			if(path[i] == '/') { i ++; break; }
			dir = dir + path[i];
		}
		if (dir != "") dirList.push_back(dir);
	}

	return addDirs();
}

int main()
{
	int T;
	cin>>T;
	int cases;
	for (cases = 1; cases <= T; cases ++){

		cin>>N>>M;
		dirList.clear();
		root.name = "root"; 
		root.children.clear();

		int i, result = 0;
		string path;
		for(i = 0; i < N; i ++) {
			cin>>path;
			splitDirs(path);
		}

		
		count = 0;
		for(i = 0; i < M; i ++) {
			cin>>path;
			dirList.clear();
			splitDirs(path);
		}
		cout<<"Case #"<<cases<<": "<<count<<endl;
	}
	return 0;
}
*/


#include <iostream>
#include <string>
#include <set>
#include <string>
using namespace std;

int testID;
set<string> dirs;

void deal()
{
	dirs.clear();
	dirs.insert("/");
  int N, M;
  cin >> N >> M;
  string line;

  getline(cin, line);

  for (int i = 0; i < N; ++i)
  {
    getline(cin, line);
    if (line[line.size() - 1] != '/')
      line += "/";
    for (int j = 0; j < line.size(); ++j)
      if (line[j] == '/')
      {
        string path = line.substr(0, j + 1);
        dirs.insert(path);
      }
  }

  int ans = 0;
  for (int i = 0; i < M; ++i)
  {
    getline(cin, line);
    if (line[line.size() - 1] != '/')
      line += "/";
    for (int j = 0; j < line.size(); ++j)
      if (line[j] == '/')
      {
        string path = line.substr(0, j + 1);
        if (dirs.find(path) != dirs.end())
          ;
        else
        {
          dirs.insert(path);
          ans++;
        }
      }
  }

  cout << "Case #" << testID << ": " << ans << endl;
}

int main()
{
  int T;
  cin >> T;
  for (testID = 1; testID <= T; ++testID)
    deal();
  return 0;
}

