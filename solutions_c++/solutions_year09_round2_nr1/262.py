#include <iostream>
#include <set>

using namespace std;

struct tree
{
	double value;
	string name;
	tree *left;
	tree *right;
	tree(double value=0, string x="")
	{
		left=0;right=0;
	}
	~tree()
	{
		if(left)
		{
			delete left;
			delete right;
		}
	}
};
int ex_bracket=0;
void take_input(tree *root)
{
	double num;
	cin>>num;
	root->value=num;
	//cout<<"value = "<<num<<endl;
	string str;
	cin>>str;
	//cout<<"GOT "<<str<<endl;
	if(str[0]==')')
	{
		ex_bracket+=str.size()-1;
		//cout<<"ex_bracket="<<ex_bracket<<endl;
		return;
	}
	if(str[str.size()-1]=='(')
	{
		str.erase(str.size()-1, 1);
		root->name=str;
	}
	else
	{
		root->name=str;
		char temp;
		cin>>temp;
		//cout<<"Here";
		//getchar();
	}
	//cout<<"name = "<<root->name<<endl;
	root->left=new tree;
	take_input(root->left);
	char temp;
	cin>>temp;
	root->right=new tree;
	take_input(root->right);
	if(ex_bracket) ex_bracket--;
	else
	{
		char temp;
		cin>>temp;
	}
}

void print_tree(tree *root)
{
	if(root)
	{
		cout<<root->value;
		if(root->left)
		{
			cout<<root->name<<endl;
			cout<<"left: ";
			print_tree(root->left);
			cout<<"right: ";
			print_tree(root->right);
		}
		else cout<<endl;
	}
	else cout<<"empty"<<endl;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int c_no;
	cin>>t;
	for(c_no=1;c_no<=t;c_no++)
	{
		int no_line;
		tree root_node;
		tree *root=&root_node;
		cin>>no_line;
		char temp;
		cin>>temp;
		//cout<<"temp="<<temp<<endl;
		ex_bracket=0;
		take_input(root);
		//cout<<"PRINTING STARTED\n";
		//print_tree(root);
		
		int no_animal;
		cout<<"Case #"<<c_no<<":\n";
		for(cin>>no_animal;no_animal;no_animal--)
		{
			string name;
			set<string> ch;
			cin>>name;
			int character;
			for(cin>>character;character;character--)
			{
				cin>>name;
				ch.insert(name);
			}
			tree* now=root;
			double prob=1;
			while(now)
			{
				prob *= now->value;
				if(ch.find(now->name)!=ch.end()) now=now->left;
				else now=now->right;
			}
			printf("%.7lf\n",prob);
		}
	}
	return 0;
}
