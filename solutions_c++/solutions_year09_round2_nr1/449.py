#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <cstring>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <iostream>

using namespace std;

struct node
{
	long double p;
	string s;
	node *has;
	node *hasnt;
};

node n[1000];
int nbNode;
stack<int> next;

int main()
{
	int nn;
	scanf("%d\n", &nn);
	for(int i = 0; i < nn; i++)
	{
		///memset(n, 0, sizeof(n));
		int L;
		while(!next.empty()) next.pop();
		nbNode = 0;
		scanf("%d\n", &L);
		char buf[100];
		string buffer = "";
		for(int j = 0; j < L; j++)
		{
			fgets(buf, 100, stdin);
			buffer+=buf;
		}
		istringstream ins;
		//ins.clear();
		//printf("%s\n\n", buffer.c_str());
		ins.str(buffer);
		char c;
		while(ins.good())
		{
			ins >> c;
		//printf("%c ", c);
			
			if(c == '(')
			{
				int cur;
				if(next.empty())
					cur = nbNode++;
				else
				{
					cur = next.top();
					next.pop();
				}
				ins >> n[cur].p;
				c= ' ';
				while(c == ' ')
					ins >> c;
				n[cur].s = string("");
				if(c == ')') n[cur].s = c;
				while(c >= 'a' && c <= 'z')
				{	n[cur].s += c; ins >> c; }
				if(n[cur].s.find(')') == string::npos)
				{
					next.push(nbNode);
					n[nbNode].s = string("error");
					n[nbNode].has = NULL;
					n[nbNode].hasnt= NULL;
					n[cur].hasnt = &n[nbNode++];
						n[nbNode].s = string("error");
						n[nbNode].has = NULL;
					n[nbNode].hasnt= NULL;
					next.push(nbNode);
					n[cur].has= &n[nbNode++];		
				}
				else
				{
					n[cur].has = NULL;
					n[cur].hasnt= NULL;
				}
				//printf("%Lf\t%s\n", n[cur].p, n[cur].s.c_str());
				//if(c=='(') 
				ins.unget();
			}
		}
			
		
		int nb;
		scanf("%d", &nb);
		//printf("%d\n", nb);
		printf("Case #%d:\n", i+1);
		for(int j = 0; j < nb; j++)
		{
			char buf[100];
			int nbF;
			scanf("%s%d", buf, &nbF);
			
			vector<string> ens;
			ens.clear();
			for(int k = 0; k < nbF; k++)
			{
				scanf("%s", buf);
				ens.push_back(string(buf));
				//printf("%s\t%d\n", buf, nbF);
			}
			scanf("\n");
			//
			node *cur = &n[0];
			long double ans = 1.;
			while(true)
			{
				ans *= cur->p;
				//printf("%Lf\n", cur->p);
				if(cur->has == NULL) break;
				//printf("%s ", cur->s.c_str());
				bool find = false;
				for(int z = 0; z < (int)ens.size(); z++)
				{
					if(ens[z].compare(cur->s) == 0) 
					{
						cur = cur->has;
						find = true;
						break;
					}
				}
				if(!find) cur = cur->hasnt;
			}
			printf("%.7Lf\n", ans);
		}
		
	}
	return 0;
}
