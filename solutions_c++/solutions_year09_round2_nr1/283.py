#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <cstdio>

using namespace std;

char tree[10000]={0};

struct node
{
	double prob;
	string name;
	node * left;
	node * right;
};

void parseTree(istringstream &iss,node * &head)
{
	head = new node;
	head->left = 0;
	head->right =0;
	head->name="";
	head->prob=1;
	string o,c,n;
	double dl;
	iss>>o;
	iss>>head->prob;
	iss>>head->name;
	if(head->name.compare(")")==0)
	{
		return;
	}
	parseTree(iss,head->left);
	parseTree(iss,head->right);
	iss>>c;
}

int main()
{
	int T,t;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		int L;
		cin>>L;
		char ch;
		cin.get(ch);
		string str;
		for(int i=0;i<L;i++)
		{
			cin.get(ch);
			while(ch!='\n')
			{
				if((ch=='(')||(ch==')'))
				{
					str.push_back(' ');
					str.push_back(ch);
					str.push_back(' ');
				}
				else
					str.push_back(ch);
				cin.get(ch);
			}
		}
		istringstream iss(str);
		node *head =NULL;
		parseTree(iss,head);
		int A;
		cin>>A;
		cout<<"Case #"<<t<<":"<<endl;
		for(int i=0;i<A;i++)
		{
			string animal;
			cin>>animal;
			int fn;
			cin>>fn;
			set<string> fs;
			for(int j=0;j<fn;j++)
			{
				string f;
				cin>>f;
				fs.insert(f);
			}
			double prob=1.0;
			node * cur =head;
			while(cur!=0)
			{
				prob*=cur->prob;
				if(fs.find(cur->name)!=fs.end())
					cur = cur->left;
				else 
					cur = cur->right;
			}
			printf("%.7lf\n",prob);
		}
	}
	return 0;
}