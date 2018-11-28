#include <iostream>
#include <vector>
#include <set>
using namespace std;

int ans[205];
int ind;

class Item
{
public:
	string file;
	set<Item> *children;
	
	Item(string s)
	{
		file = s;
		children = new set<Item>;
	}
	
	friend bool operator <(Item A,Item B)
	{
		return A.file<B.file;
	}
};

class TrieTree
{
public:
	set<Item> *root;
	
	TrieTree()
	{
		root = new set<Item>;
	}
	
	void processFiles(vector<string> vs)
	{
		int k;
		set<Item>::iterator it;
		set<Item> *item = root;
		
		k=0;
		for(int i = 0;i<vs.size();i++){
			if((it = item->find(Item(vs[i]))) == item->end()){
				it = item->insert(Item(vs[i])).first;
				k++;
			}
			item = it->children;
		}
		ans[ind] = k;
	}
};
	
int main(){
	int T,t;
	int n,m;
	int i,j,k;
	string s;
	
	cin>>T;
	t=1;
	while(T--){
		cin>>n>>m;
		vector<string> files;
		TrieTree *tree;
		ind = 0;
		
		for(i=0;i<(n+m);i++){
			cin>>s;
			files.push_back(s);
			ans[i] = 0;
		}
		
		tree = new TrieTree();
		for(i=0;i<files.size();i++){
			vector<string> vs;
			s = "";
			for(j=1;j<files[i].size();j++){
				if(files[i][j] == '/'){
					vs.push_back(s);
					s = "";
				}
				else
					s += files[i][j];
			}
			if(s.size()>0)
				vs.push_back(s);
			tree->processFiles(vs);
			ind++;
		}
		
		int fans = 0;
		for(i=n;i<(n+m);i++)
			fans += ans[i];
			
		printf("Case #%d: %d\n",t,fans);
		t++;
	}
	return 0;
}
	
	