#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <sstream>
#include <queue>
#include <map>
using namespace std;

FILE * fp;
int t;

int l,n;

string s;
struct Node
{
	string st;
	Node * lef;
	Node * rig;
	double p;
	Node():st(""),lef(NULL),rig(NULL){}
};
Node * root;
void construct(Node *& rt,int l,int r)
{
	if(l >= r)
	{
		rt = NULL;
		return ;
	}
	int bel;
	rt = new Node;
	stringstream ss;
	int pos = l + 1;
	while(s[pos] == ' ')
		pos ++;
	while(s[pos] != ' ' && s[pos] != '(' && s[pos] != ')')
	{
		ss << s[pos];
		pos ++;
	}
	ss >> rt->p;
	while(s[pos] == ' ')
		pos ++;
	if(s[pos] == ')')
		return ;
	if(s[pos] != '(')
	{
		while(s[pos] != ' ' && s[pos] != '(')
		{
			rt->st += s[pos];
			pos ++;
		}
		while(s[pos] == ' ')
			pos ++;
		bel = pos;
		int cnt = 1;
		int mid = pos + 1;
		while(mid <= r)
		{
			if(cnt == 1 && s[mid] == ')')
				break;
			if(s[mid] == '(')
				cnt ++;
			if(s[mid] == ')')
				cnt --;
			mid ++;
		}

		construct(rt->lef,bel,mid);
		mid ++;
		while(mid <= r && s[mid] == ' ')
			mid ++;
		int edr = r - 1;
		while (edr >= mid && s[edr] != ')')
			edr --;
		construct(rt->rig,mid,edr);
	}

}

map<string,int> mp;

double dfs(Node * r)
{
	if(r == NULL)
		return 1.0;
	if(mp.count(r->st) != 0)
	{
		return dfs(r->lef) * r->p;
	}
	else
		return dfs(r->rig) * r->p;
}




int main()
{
	fp = fopen("out.txt","w");
	scanf("%d",&t);
	int r = 1;
	while(--t >= 0)
	{
		cin >> l;
		s.clear();
		string temp;
		getline(cin,temp);
		temp.clear();
		for(int i = 0;i < l;i ++)
		{
			getline(cin,temp);
			s += temp;
		}
		construct(root,0,s.size() - 1);

		int k;
		cin >> k;
		fprintf(fp,"Case #%d:\n",r);
			r ++;
		for(int i = 0;i < k;i ++)
		{
			//map<string,int> mp;
			mp.clear();
			cin >> temp;
			int m;
			cin >> m;
			for(int j = 0;j < m;j ++)
			{
				cin >> temp;
				mp[temp] = 1;
			}
			double ans = dfs(root);
			fprintf(fp,"%.8lf\n",ans);
		}
	}






	return 0;
}