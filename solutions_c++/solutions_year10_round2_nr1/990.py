#include <fstream>
#include <string>
#include <set>
#include <map>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");


class tree;

typedef map<string,tree> MS;

class tree
{
public:
	MS next;
	void add(const string &str)
	{
		if(str.length()==0)return;
		int t=str.find('/');
		if(t!=-1)
		{
			string str1=str.substr(0,t);
			next[str1].add(str.substr(t+1,str.length()));
		}
		else 
		{
			if(next.find(str)==next.end())next[str]=tree();
		}
	}
	int count()const
	{
		int sum=next.size();
		for(MS::const_iterator i=next.begin();
			i!=next.end();i++)
		{
			sum+=i->second.count();
		}
		return sum;
	}
};

int main()
{
	int T;
	cin>>T;
	for(int tn=1;tn<=T;tn++)
	{
		int n,m;
		cin>>n>>m;
		tree tr;
		for(int i=0;i<n;i++)
		{
			string str;
			cin>>str;
			tr.add(str.substr(1,str.length()));
		}
		int len=tr.count();
		for(int i=0;i<m;i++)
		{
			string str;
			cin>>str;
			tr.add(str.substr(1,str.length()));
		}
		cout<<"Case #"<<tn<<": "<<tr.count()-len<<endl;
	}
	
}