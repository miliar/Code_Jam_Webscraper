#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int getSlashNum(string n)
{
	int ret = 0;
	for(int i = 0; i < (int)n.size(); i++)
	{
		if(n[i] == '/')
			ret++;
	}
	return ret;
}
int res;
class treenode
{
public:
	string name;
	vector <treenode*> child;
	treenode(string n)
	{
		name = n;
//		child.size(1000);
//		child.resize(1000);
	}
	void addChild(string n)
	{
		child.push_back(new treenode(n));
	}
	void addChildByName(string n)
	{
		if(getSlashNum(n) == 0)
		{
			addChild(n);
		}
		else
		{
			int wheres;
			for(int i = 0; i < (int)n.size(); i++)
			{
				if(n[i] == '/')
				{
					wheres = i;
					break;
				}
			}
			findChild(n.substr(0,wheres))->addChildByName(n.substr(wheres+1,(int)n.size()-wheres-1));
		}
	}
	void createChildByName(string n)
	{
		if(getSlashNum(n) == 0)	{
			if(findChild(n) == NULL){
				addChild(n);
				res++;	}	}
		else
		{
			int wheres;
			for(int i = 0; i < (int)n.size(); i++)
			{
				if(n[i] == '/')
				{
					wheres = i;
					break;
				}
			}
			if(findChild(n.substr(0,wheres)) == NULL)
			{
				addChild(n.substr(0,wheres));
				res++;
				findChild(n.substr(0,wheres))->createChildByName(n.substr(wheres+1,(int)n.size()-wheres-1));
			}
			else
				findChild(n.substr(0,wheres))->createChildByName(n.substr(wheres+1,(int)n.size()-wheres-1));
		}
	}


	treenode* findChild(string n)
	{
		for(int i = 0; i < (int)child.size(); i++)
		{
			if(child[i]->name == n)
				return child[i];
		}
		return NULL;
	}
};



int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int cases;
	int tCase;
	fin>>cases;
	tCase = 1;
	while(cases--)
	{
		res = 0;
		int N,M;
		fin>>N>>M;

		treenode root = treenode("root");
		vector <string> exist;
		for(int i = 0; i < N; i++)
		{
			string temp_str;
			fin>>temp_str;
			exist.push_back(temp_str);
		}
		int numslash = 1;
//		root.addChildByName("asgsd/ddd");
		while(!exist.empty())
		{
			for(int i = 0; i < (int)exist.size(); i++)
			{
				if(getSlashNum(exist[i]) == numslash)
				{
					root.addChildByName(exist[i].substr(1,(int)exist[i].size()-1));
					exist.erase(exist.begin()+i);
					i--;
				}
			}
			numslash++;
		}

		for(int i = 0; i < M; i++)
		{
			string temp_str;
			fin>>temp_str;
			root.createChildByName(temp_str.substr(1,(int)temp_str.size()-1));
		}



		fout<<"Case #"<<tCase++<<": "<<res<<endl;
	}
	return 0;
}

