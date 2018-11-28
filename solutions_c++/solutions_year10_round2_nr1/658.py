#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
using namespace std;

int check( map<string , bool> &already , string s)
{
	string temp = "/";
	int ret = 0;

	for (int i = 1; i < s.length() ; i++)
	{
		if(s[i] == '/' || i == s.length()-1)
		{
			if(i== s.length()-1)
				temp+=s[i];
			if(already[temp] == false)
			{
				ret += 1;
				already[temp] = true;
			}
			if(s[i] == '/')
				temp += s[i];
		}
		else
		{
			temp += s[i];
		}
	}

	return ret;
}

/*
struct tree
{
	string s;
	tree *firstch;
	tree *next;
};

tree *root = NULL;

tree * createnewnode(string s)
{
	tree *np  = new tree;
	np->firstch = NULL;
	np ->next = NULL;
	np ->s = s;
	return np;
}

bool checkChild( string s , tree *&root , tree * &node)
{
	if( root == NULL)
	{
		root = createnewnode(s);
		node = root;
		return false;
	}

	while(root->next)
	{
		if(root -> s != s)
			root = root -> next;
		else
		{
			node = root;
			return true;
		}
	}

	if(root->s != s){
		root ->next = createnewnode(s);
		node = root ->next;
	}
	else
		return true;
	return false;
}

int insertbranch( vector<string> v , tree *root , bool already)
{
	int ret = 0;
	for (int i = 0; i < v.size() ; i++)
	{
		tree * node = NULL;

		cout<<i<<" "<<v[i]<<endl;
		bool flag;

		if(root == NULL)
			flag = checkChild(v[i] , root , node);
		else
			flag = checkChild(v[i] , node->firstch , node);

		if(root==NULL)
			cout<<"null";
		else 
			cout<<root->s<<" "<<root->firstch<<" "<<node->s<<" "<<node->firstch <<endl;

		if(node == NULL)
			cout<<":P";

		if(!flag && already)
			ret += 1;

		//root = node->firstch;
	}

	return ret;
}


vector<string> format( string s )
{
	vector<string> v;
	string temp = "";
	for (int i = 1; i < s.length() ; i++)
	{
		
		if(s[i]=='/' || i == s.length()-1)
		{
			cout<<temp<<endl;
			v.push_back(temp);
			temp = "";
		}
		else
			temp += s[i];
	}
	return v;
}*/

void insert(  string s , map<string , bool> &m)
{
	string temp = "/";

	for (int i = 1; i < s.length() ; i++)
	{
		if( s[i] == '/' || i == s.length()-1)
		{
			if(i == s.length()-1)
				temp += s[i];
			m[temp] = true;
			temp += s[i];
		}
		else
			temp += s[i];
	}
}

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("output.txt" , "w" , stdout);
	int t;
	cin>>t;

	for (int caseID = 1; caseID <= t ; caseID++)
	{
		int n,m;
		cin>>n>>m;
		map<string,bool> already;
		for (int i = 0; i < n ; i++)
		{
			string s;
			cin>>s;
			//vector<string> v = format(s);
			//insertbranch(v , root , false);
			insert(s , already);
		}

		//for(map<string,bool>::iterator it = already.begin() ; it != already.end() ; it++ )
		//	cout<<(*it).first <<" ";
		//cout<<endl;
		int ans = 0;
		for (int i = 0; i < m ; i++)
		{
			string s;
			cin>>s;
			//vector<string> v = format(s);
			//ans += insertbranch(v , root , true);
			//if(root==NULL){
			//	cout<<"askjaskd";
			//	exit(0);
			//}
			//else cout<<"here: "<<root->s<<endl;
			ans += check(already , s);
		}
		cout<<"Case #"<<caseID<<": "<<ans<<endl;
	}
	return 0;
}