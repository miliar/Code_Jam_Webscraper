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
			*iss >> dummy;
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
	int L;
		cin >> L;
		cerr << L << endl;
		getline(cin,s);
		string ss = "";
		for(int i=0;i<L;++i)
		{
			getline(cin,s);
			for(int j=0;j<s.size();++j)
			{if(s[j]=='\n'||s[j]=='\r'){s[j]=' ';}ss.push_back(s[j]);}
			//ss.append(s);
		}
		//cerr << ss << endl;
		string sw = "";
		for(int i=0;i<ss.size();++i)
		{
			if(ss[i] == '(' || ss[i] == ')')
			{
				sw.push_back(' ');
				sw.push_back(ss[i]);
				sw.push_back(' ');
			}
			else
			{
				sw.push_back(ss[i]);
			}
		}
		cerr << sw << endl;
		iss = new istringstream(sw);
		*iss >> ss;
		cerr << ss << endl;
		//cerr << iss->str() << endl;
		Tree *t = new Tree();
		int A;
		cin >> A;
		cerr << A << endl;
		printf("Case #%d:\n",cn);
		for(int i=0;i<A;++i)
		{
			string st;int P;
			cin >> st >> P;
			vector<string> vs;vs.clear();
			for(int j=0;j<P;++j)
			{cin >> st;vs.push_back(st);}
			sort(vs.begin(),vs.end());
			double out = 1.0;
			Tree *cur = t;
			while(1)
			{
				out *= cur->val;
				if(cur->left != NULL)
				{
					if(binary_search(vs.begin(),vs.end(),cur->property))
					{
						cur = cur->left;
					}
					else
					{
						cur = cur->right;
					}
				}
				else
				{break;}
			}
			printf("%.12lf\n",out);
			//cerr << (int)(t) << endl;
		}
		delete iss;
		iss = NULL;
	//	cerr << "FDFD" << endl;
		delete t;
		t = NULL;
	}


}
