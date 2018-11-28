#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

class Tree
{
	public:
	string dir;
	vector<Tree> children;
	
	Tree(string s)
	{
		dir = s;
	}
	
	int add(string str);
};

int Tree::add(string str)
{
//	cout<<"adding "<<str.c_str()<<endl;//testing
	
	if (str.length()==0) return 0;
	if (str[0]!='/') 
	{
		cerr<<"Invalid string"<<endl;
		return 0;
	}
	
	string curr;
	int index = 0;
	for (int i=1;i<str.length();i++)
	{
		if (str[i]=='/') 
		{ 
			index = i;
			break;
		}
		curr.append(1,str[i]);
	}
//	cout<<"curr: "<<curr.c_str()<<"index: "<<index<<endl;//testing 
	
	for (int i=0;i<children.size();i++)
	{
		
		if (curr.compare(children[i].dir)==0)
		{
			if (index == 0) return 0;
			return children[i].add(str.substr(index));
		}
	}
	
	children.push_back(Tree(curr));
	if (index > 0 ) return 1 + children.back().add(str.substr(index));
	else return 1;
	
}


int main()
{
	int T;
	cin>>T;
	for (int tc=0;tc<T;tc++)
	{
//		cout<<"Case "<<tc<<endl;
		int N,M;
		cin>>N>>M;
		
//		string *present = new string[N];
//		string *newdir = new string[M];
		
		Tree *root = new Tree(string("/"));

		string temp;		
		for (int i=0;i<N;i++)		
		{
			cin>>temp;
			root->add(temp);
		}
		
		int ret = 0;
		for (int i=0;i<M;i++)
		{
			cin>>temp;
			ret = ret + root->add(temp);
		}
		
		cout<<"Case #"<<tc+1<<": "<<ret<<endl;
	}
	
}
