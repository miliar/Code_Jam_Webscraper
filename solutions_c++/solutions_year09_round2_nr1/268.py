#include<iostream>
#include<string>
#include<sstream>
#include<map>
using namespace std;

struct Tnode{
	double w;
	string s;
	Tnode* l;
	Tnode* r;

	Tnode()
	{
		w=0;
		s="";
		l=r=NULL;
	}

	~Tnode()
	{
		delete l;
		delete r;
	}
};

int tt,tc;
int r,q;

Tnode* tree;
map<string,int> ani;

void parser(string s,Tnode* &t)
{
	if (t==NULL) t=new Tnode;

	while (s[0]==' ') s.erase(0,1);
	s.erase(0,1);

	while (s[s.length()-1]==' ') s.erase(s.length()-1,1);
	s.erase(s.length()-1,1);

	stringstream ss(s);
	
	ss>>t->w;
	if (ss>>t->s)
	{
		getline(ss,s);
		string str="";

		int i,j,mark,cnt;
		for (i=0;i<s.length();i++)
			if (s[i]=='(')
			{
				cnt=0;
				str="";
				for (j=i;j<s.length();j++)
				{
					str+=s[j];
					if (s[j]=='(') cnt++;
					if (s[j]==')') cnt--;
					if (cnt==0)
					{
						mark=j;
						break;
					}
				}
				break;
			}
		parser(str,t->l);
		for (i=mark;i<s.length();i++)
			if (s[i]=='(')
			{
				str="";
				cnt=0;
				for (j=i;j<s.length();j++)
				{
					str+=s[j];
					if (s[j]=='(') cnt++;
					if (s[j]==')') cnt--;
					if (cnt==0)
					{
						mark=j;
						break;
					}
				}
				break;
			}
		parser(str,t->r);
	}
}

double search(Tnode* t)
{
	if (t->s=="") return t->w;

	if (ani.count(t->s)>0) return t->w*search(t->l);
	else return t->w*search(t->r);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);

	cin>>tc;
	
	string s;
	string tmp;

	for (tt=1;tt<=tc;tt++)
	{
		cin>>r;
		cin.get();
		s="";	

		while (r--)
		{
			getline(cin,tmp);
			s+=(" "+tmp);
		}
		
		delete tree;
		tree=NULL;

		parser(s,tree);

		printf("Case #%d:\n",tt);
		
		cin>>q;
		int f;

		while (q--)
		{
			cin>>s;
			cin>>f;
			ani.clear();
			while (f--)
			{
				cin>>s;
				ani[s]=1;
			}

			printf("%.7lf\n",search(tree));
		}
		
	}
}
