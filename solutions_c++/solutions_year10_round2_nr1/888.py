#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>	

using namespace std;

struct Node
{
	string name;
	//vector<string> c;
	vector<Node*> next;
};

Node *root;
char str[105];

int addpath()
{
	int len = strlen(str);
	Node *p = root;
	int i, j, k;
	int ret = 0;
	for(i=0; i<len; )
	{
		if(str[i]=='/'){i++; continue;}
		j = i;
		string s="";
		for(;j<len&&str[j]!='/'; j++)
			s += str[j];
		i=j;

		//cout<<s<<endl;

		bool f = false;
		for(k=0; k<p->next.size(); k++)
		{
			if(p->next[k]->name == s)
			{
				p = p->next[k];
				f = true;
				break;
			}
		}

		if( !f )
		{
			Node* ad = new Node;
			ad->name = s;
			ad->next.clear();
			p->next.push_back(ad);
			ret++;
			p = p->next[p->next.size()-1];
		}
	}
	return ret;
}

int main()
{

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	int nCase;
	int m, n;
	int i, j, k;

	scanf("%d", &nCase);
	for(int cc=1; cc<=nCase; cc++)
	{
		root = new Node;
		//root->c.clear();
		root->name = "/";
		root->next.clear();
		int res = 0;

		scanf("%d%d", &n, &m);
		for(i=0; i<n; i++)
		{
			scanf("%s", str);
			addpath();
		}
		for(i=0; i<m; i++)
		{
			scanf("%s", str);
			res += addpath();
		}

		printf("Case #%d: %d\n", cc, res);
	}
	return 0;

}