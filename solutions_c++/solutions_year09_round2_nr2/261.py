#include <vector>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

istringstream *iss;

struct Tree
{
	double val;
	string property;
	Tree *left,*right;
	Tree(void)
	{
		left = right = NULL;
		string dummy;
		*iss >> val;
		*iss >> property;
		if(property==")")
		{
			//done
			//property.clear();
			return;
		}
		else
		{
			//read in tree left and tree right
			*iss >> dummy;
			left = new Tree();
			*iss >> dummy;
			right = new Tree();
		}
	};
	~Tree()
	{
		delete left;
		delete right;
	};
};

int main(int argc,char **argv)
{
	if(argc>1){freopen(argv[1],"r",stdin);}
	int CC;
	cin >> CC;
	for(int cn=1;cn<=CC;++cn)
	{
		string s;
		cin >> s;
		vector<int> ct(10,0);
		for(int i=0;i<s.size();++i)
		{
			++ct[s[i]-'0'];
		}
		if(next_permutation(s.begin(),s.end()))
		{
			printf("Case #%d: %s\n",cn,s.c_str());
		}
		else
		{
			s.push_back('0');
			sort(s.begin(),s.end());
			int t;
			for(t=1;t<10;++t)
			{if(ct[t]){break;}}
			int q;
			for(q=s.size()-1;q>=0;--q)
			{if(s[q]=='0'+t){break;}}
			s[0] = t+'0';
			s[q] = '0';
			sort(s.begin()+1,s.end());
			printf("Case #%d: %s\n",cn,s.c_str());
		}
	}


}
