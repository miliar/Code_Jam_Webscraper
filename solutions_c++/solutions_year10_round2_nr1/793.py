#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <stdlib.h>

using namespace std;

bool count=false;
int counted=0;

class Directory
{
public:
	map<string,Directory> subdirs;
	Directory* get(const string& name)
	{
		map<string,Directory>::iterator it=subdirs.find(name);
		if(it==subdirs.end())
		{
			if(count)
				counted++;
			return &subdirs[name];
		}
		return &it->second;
	}
};

Directory root;

Directory* recursiveGet(string& name)
{
	Directory* cur=&root;
	int start=1;
	int next;
	if(name[0]!='/')
		::abort();
		//start=0;
	while((next=name.find('/',start))!=name.npos)
	{
		//cout << "getting " << name.substr(start,(next-start)) << endl;
		cur=cur->get(name.substr(start,(next-start)));
		start=next+1;
	}
	//Now get the final dir
	//cout << "getting last " << name.substr(start) << endl;
	cur->get(name.substr(start));
}

int main(int argc, char* argv[])
{
	ifstream f(argv[1]);
	int cases;
	f >> cases;
	for(int cas=0;cas<cases;cas++)
	{
		int N,M;
		f >> N >> M;
		string s;
		count=false;
		counted=0;
		for(int i=0;i<N;i++)
		{
			f >> s;
			recursiveGet(s);
		}
		count=true;
		for(int i=0;i<M;i++)
		{
			f >> s;
			recursiveGet(s);
		}
		cout << "Case #" << (cas+1) << ": " << counted << endl;
		root=Directory();
	}

}
