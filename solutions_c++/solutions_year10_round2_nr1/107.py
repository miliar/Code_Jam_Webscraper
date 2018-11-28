#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

struct dir
{
	string name;
	vector<dir*> subs;

	~dir()
	{
		for (int i=0;i<subs.size();i++)
			delete subs[i];
	}

	int add_path(string path)
	{
		if (path=="")
			return 0;
		int ans=0;
		string cur;
		for (int i=1;i<=path.size();i++)
			if (i==path.size() || path[i]=='/')
			{
				cur=string(++path.begin(),path.begin()+=i);
				path=string(path.begin()+=i,path.end());
				break;
			}
		bool flag=false;
		dir *next;
		for (int i=0;i<subs.size();i++)
			if (subs[i]->name==cur)
			{
				flag=true;
				next=subs[i];
				break;
			}
		if (!flag)
		{
			next=new dir;
			next->name=cur;
			subs.push_back(next);
			ans++;
		}
		ans+=next->add_path(path);
		return ans;
	}

};

int n,m;
dir* root;

int caseN;
int main()
{
	cin>>caseN;
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		root=new dir;
		root->name="";
		cin>>n>>m;
		while (n--)
		{
			string path;
			cin>>path;
			root->add_path(path);
		}
		int ans=0;
		while (m--)
		{
			string path;
			cin>>path;
			ans+=root->add_path(path);
		}
		cout<<"Case #"<<caseI<<": "<<ans<<endl;
		delete root;
	}
	return 0;
}
