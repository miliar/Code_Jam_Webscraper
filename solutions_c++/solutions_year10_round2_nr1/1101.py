#include <cstdio>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int T,N,M;
struct node
{
	string name;
	vector<struct node *> child;
};

struct node *root = NULL;

int insert(string str)
{
	int i,j,k,len = str.length(),insert_count = 0,index;
	string name;
	bool tag;
	struct node *p = root,*temp = NULL;
	i=1;
	while(i<len)
	{
		j = i;
		while(i<len&&str[i]!='/')
			i++;
		name = str.substr(j,i-j);
		tag = true;
		for (k=0;k<int(p->child.size());k++)
			if (name==p->child[k]->name)
			{
				tag = false;
				index = k;
				break;
			}
		if (tag)
		{
			temp = new node;
			temp->name = name;
			int pos = p->child.size();
			p->child.push_back(temp);
			p = p->child[pos];
			insert_count++;
		}
		else
			p = p->child[index];
		i++;
	}
	return insert_count;
}

void destroy(struct node *r)
{
	int i;
	if (r->child.size()==0)
		delete r;
	else
		for (i=0;i<int(r->child.size());i++)
			destroy(r->child[i]);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,ans;
	string str;
	cin>>T;
	for (i=1;i<=T;i++)
	{
		cin>>N>>M;
		root = new node;
		ans = 0;
		for(j=0;j<N;j++)
		{
			cin>>str;
			insert(str);
		}
		for(j=0;j<M;j++)
		{
			cin>>str;
			ans+=insert(str);
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
		destroy(root);
	}
	return 0;
}

