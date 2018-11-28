#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
using namespace std;

class tree
{
	double weight;
	string desc;
	tree *left,*right;
	public:
	tree()
	{
		left=NULL,right=NULL;
		desc="";
	}
	void read()
	{
		char br;
		char iscb;
		char cb;
		scanf(" %c",&br);
		scanf(" %lf",&weight);
		//cout<<weight<<endl;
		//string iscb;
		scanf(" %c",&iscb);	
		//cin>>iscb;
		
		if(iscb!=')')
		{
			cin>>desc;
			if(desc[0]!='(')
			{
				desc=iscb+desc;
			}
			else{
				for(int i=desc.size()-1;i>=0;i--)
					ungetc(desc[i],stdin);

				desc=iscb;
			}

			//cout<<desc<<endl;
			left=new tree();
			left->read();
			right=new tree();
			right->read();
			scanf(" %c",&cb);
		}
		
	}
	void print()
	{
		cout<<weight;
		if(desc!="")
			cout<<" "<<desc;
		else
			cout<<" leaf";
		cout<<endl;
		if(left!=NULL)
			left->print();
		if(right!=NULL)
			right->print();

	}
	double compute(vector<string> & chars)
	{
		if(desc=="")
			return weight;
		double w=weight;
		bool flag=0;
		for(int i=0;i<chars.size() && !flag;i++)
		{
			if(chars[i]==desc)
				flag=true;

		}
		if(flag)
			return w*left->compute(chars);
		else
			return w*right->compute(chars);

	}
};

int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int l;
		cin>>l;
		//string temp;
		//getline(cin,temp,'\n');
		tree t;
		t.read();	
		//t.print();	
		int n_animal;
		cin>>n_animal;
		printf("Case #%d:\n",i);
		for(int k=0;k<n_animal;k++)
		{
		string animal;
		cin>>animal;
		int n_char;
		cin>>n_char;
		vector<string> chars(n_char);
		for(int j=0;j<chars.size();j++)
			cin>>chars[j];

			printf("%.7lf\n",t.compute(chars));
		}


	}
	return 0;
}
