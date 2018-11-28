#include<cstdio>
#include<vector>
#include<stack>
#include<map>
#include<cstring>
#include<algorithm>
using namespace std;
class game
{
private:
	stack<int> e;
	vector<pair<int,int> > r1[26];
	vector<int> r2[26];
	int s[26];
	int rule_1(int a,int b)
	{
		for(vector<pair<int,int> >::iterator c=r1[a].begin();c!=r1[a].end();c++)
			if(c->first==b)return c->second;
		return -1;
	}
	bool rule_2(int a)
	{
		for(vector<int>::iterator c=r2[a].begin();c!=r2[a].end();c++)
			if(s[*c])return 1;
		return 0;
	}
public:
	void clear()
	{
		while(!e.empty())e.pop();
		for(int i=0;i<26;i++)r1[i].clear();
		for(int i=0;i<26;i++)r2[i].clear();
		memset(s,0,sizeof s);
	}
	void add_rule_1(char*rule)
	{
		int a=rule[0]-'A',b=rule[1]-'A',c=rule[2]-'A';
		r1[a].push_back(make_pair(b,c)),
		r1[b].push_back(make_pair(a,c));
	}
	void add_rule_2(char*rule)
	{
		int a=rule[0]-'A',b=rule[1]-'A';
		r2[a].push_back(b),
		r2[b].push_back(a);
	}
	void push_element(char element)
	{
		int a=element-'A';
		while(1)
		{
			if(e.empty()){s[a]++;e.push(a);return;}
			int p=rule_1(a,e.top());
			if(p==-1)
			{
				if(rule_2(a))
				{
					while(!e.empty())s[e.top()]--,e.pop();
					return;
				}
				s[a]++;e.push(a);return;
			}else
			{
				a=p;s[e.top()]--;e.pop();
			}
		}
	}
	void output()
	{
		stack<char> a;
		while(!e.empty())a.push('A'+e.top()),e.pop();
		bool F=1;
		putchar('[');
		while(!a.empty())
		{
			if(!F)putchar(' ');else F=0;
			putchar(a.top());
			a.pop();
			if(!a.empty())putchar(',');
		}
		puts("]");
	}
}A;
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		A.clear();
		int num_rule_1;
		scanf("%d",&num_rule_1);
		while(num_rule_1--)
		{
			char rule[5];
			scanf("%s",rule);
			A.add_rule_1(rule);
		}
		int num_rule_2;
		scanf("%d",&num_rule_2);
		while(num_rule_2--)
		{
			char rule[5];
			scanf("%s",rule);
			A.add_rule_2(rule);
		}
		int num_push;
		scanf("%d",&num_push);
		char element[200];
		scanf("%s",element);
		for(int i=0;i<num_push;i++)
			A.push_element(element[i]);
		printf("Case #%d: ",__);
		A.output();
	}
	return 0;
}

