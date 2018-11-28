#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
class node
{
	public:
	string s;
	vector<node*> v;
	node(){}
	node(string _s)
	{
		s=_s;
	}
	int ispresent(string str)
	{
		int n = v.size();
		int i;
		for(i=0;i<n;++i)
			if((*v[i]).s==str)
				return i;
		return -1;
	}
	void add(node* n)
	{
		v.push_back(n);
	}
};
vector<string> token(string s,string c)
{
	vector<string> ret;
	string temp;
	int i,j;
	bool flag;
	
	for(i=0;i<s.length();++i)
	{
		for(j=0;j<c.length();++j)
		{
			flag=1;
			if(s[i]==c[j])
			{
				flag=0;
				if(temp.length()>0)
				{
					ret.push_back(temp);
					temp="";
				}
				break;
			}
		}
		if(flag)
			temp+=s[i];
	}
	if(temp.length()>0)
		ret.push_back(temp);
	return ret;
}
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T;
	fin>>T;
	int i,t;
	for(t=1;t<=T;++t)
	{
		fout<<"Case #"<<t<<": ";
		node root(".");
		int N,M;
		fin>>N;
		fin>>M;
		vector<string> vstr;
		int sz;
		int j;
		int tmp;
		node* next;
		string str;
		for(i=0;i<N;++i)
		{
			fin>>str;
			vstr=token(str,"/");
			sz=vstr.size();
			node* curr=&root;
			for(j=0;j<sz;++j)
			{
			//	cout<<vstr[j]<<endl;
				if((tmp=curr->ispresent(vstr[j]))!=-1)
				{
					curr=curr->v[tmp];
				}
				else
				{
					next = new node(vstr[j]);
					curr->add(next);
					curr=next;
				}
			}
		}
		int count=0;
		for(i=0;i<M;++i)
		{
			fin>>str;
			vstr=token(str,"/");
			sz=vstr.size();
			node* curr=&root;
			for(j=0;j<sz;++j)
			{
			//	cout<<vstr[j]<<endl;
				if((tmp=curr->ispresent(vstr[j]))!=-1)
				{
					curr=curr->v[tmp];
				}
				else
				{
					next = new node(vstr[j]);
					curr->add(next);
					curr=next;
					++count;
				}
			}
		}
		fout<<count<<endl;
	}
	return 0;
}
				
				

