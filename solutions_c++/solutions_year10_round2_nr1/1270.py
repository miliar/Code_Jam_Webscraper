#include<iostream>
#include <string>
#include <vector>
using namespace std;
int cnt = 0;
struct TreeNode
{
	TreeNode *FirstChild;
	TreeNode *Next;
	string val;
	//TreeNode *Parent;
	TreeNode()
	{
		this->FirstChild = NULL;
		this->Next = NULL;
		//this->Parent = NULL;
		this->val = "BBBBB";
	};
};

vector<string> chg(string path)
{
	int h = 0,e = 0;
	int L = path.length();
	vector<string> ret;
	for(int i = 1; i< L; ++i)
	{
		e = i; h = i;
		while(path[i] != '/')
		{
			e ++;
			i++;
		}
		ret.push_back(path.substr(h,e-h));
		if(i == L-1) break;
		else  
		{
			
		}
	}
	return ret;
}

void AddNodeNoSearch(TreeNode *node,vector<string> path,int H)
{
	bool add = false;
	TreeNode *R = node;
	bool find = false;
	if(node->val == path[H]) 
	{
		find = true;
	}
	else 
	{
		while(node->Next != NULL && node->Next->val != path[H])
		{
			node = node->Next;
		}
		if(node->Next != NULL) 
		{
			find = true;
		}
	}
	if(!find)
	{
		TreeNode *New = new TreeNode(); cnt ++;
		New->val = path[H];
		node->Next = New;
		for(int i = H+1; i< path.size(); ++i)
		{
			TreeNode *N = new TreeNode();cnt ++;
			N->val = path[i];
			New->FirstChild = N;
			New = N;
		}
	}
	else 
	{
		node = R;
		while(node->val != path[H])
		{
			node = node->Next;
		}
		if(node->FirstChild != NULL)
		{
			AddNodeNoSearch(node->FirstChild,path,H+1);
		}
		else 
		{
			for(int i = H+1; i< path.size(); ++i)
			{
				TreeNode *N = new TreeNode();cnt ++;
				N->val = path[i];
				node->FirstChild = N;
				node = N;
			}
		}
	}
}

bool Have(TreeNode *node, vector<string> path,int H)
{
	bool add = false;
	TreeNode *R = node;
	bool find = false;
	if(node->val == path[H]) 
	{
		find = true;
	}
	else 
	{
		while(node->Next != NULL && node->Next->val != path[H])
		{
			node = node->Next;
		}
		if(node->Next != NULL) 
		{
			find = true;
		}
	}
	if(!find)
	{
		return false;
	}
	else 
	{
		node = R;
		while(node->val != path[H])
		{
			node = node->Next;
		}
		if(node->FirstChild != NULL)
		{
			if(H+1==path.size()) return true;
			else return Have(node->FirstChild,path,H+1);
		}
		else 
		{
			if(H+1==path.size()) return true;
			else return false;
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for(int caseT = 1; caseT <= T; ++caseT)
	{
		int N,M;
		cin >> N >> M;
		string str;
		TreeNode *Root = new TreeNode();
		Root->val = "BDRoot";
		for(int i = 0; i< N; ++i)
		{
			cin >> str;
			str = "/BDRoot" + str + "/";
			vector<string> paths = chg(str);
			if(Have(Root,paths,0)) continue;
			AddNodeNoSearch(Root,paths,0);
		}
		cnt = 0;
		for(int i = 0; i< M; ++i)
		{
			cin >> str;
			str = "/BDRoot" + str + "/";
			vector<string> paths = chg(str);
			if(Have(Root,paths,0)) continue;
			AddNodeNoSearch(Root,paths,0);
		}
		cout << "Case #" << caseT << ": " << cnt << endl;
	}
	return 0;
}