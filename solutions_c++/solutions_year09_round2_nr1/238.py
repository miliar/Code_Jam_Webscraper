#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <set>
#include <string>
#define clr(a) memset(a, 0, sizeof(a))

#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}

char in[1000000];
char token[1000];
int cur;
int last;

void read_token()
{
	while(in[cur] != '(' && in[cur] != ')' && (in[cur] < 'a' || in[cur] > 'z') && ! ((in[cur] >= '0' && in[cur] <= '9') || in[cur] == '.'))
	{
		cur++;
	}
	if (in[cur] == '(' || in[cur] == ')')
	{
		token[0] = in[cur++];
		token[1] = 0;
	}
	else
	{
		int l = 0;
		while((in[cur] >= 'a' && in[cur] <= 'z') || (in[cur] >= '0' && in[cur] <= '9') || in[cur] == '.')
		{
			token[l++] = in[cur++];
		}
		token[l] = 0;
	}
}



class node
{
public:
	std::string name;
	node *l, *r;
	double w;
	void read()
	{
		read_token();
		read_token();
		
		sscanf(token, "%lf", &w);	
		
		read_token();
		
		
		char c = token[0];		
		if (c == ')')
		{
			l = r = 0;
			return;
		}
		else
		{
			name = std::string(token);
			l = new node();
			r = new node();
			l->read();
			r->read();
			read_token();
		}
	}   
};


void rm(node * p)
{
	if (p->l)
		rm(p->l);
	if (p->r)
		rm(p->r);
	delete p;
}


double parse(node * cur, std::set<std::string> &set)
{
	double a = cur->w;
	if (cur->l)
	{
		if (set.find(cur->name) != set.end())
		{
			a *= parse(cur->l, set);
		}
		else
		{
			a *= parse(cur->r, set);
		}
	}
	return a;
}

void read()
{
	int x;
	scanf("%d\n", &x);
	last = 0;
	for(int i = 0; i < x; i++)
	{
		gets(in + last);
		while(in[last])
			last++;
	}	
}


void solve(int test_case)
{
	printf("Case #%d: \n", test_case);
	read();
	cur = 0;
	
	node * root = new node();
	root->read();
	int n;
	std::set<std::string> set;
	scanf("%d\n", &n);
	for(int i = 0; i < n; i++)
	{
		set.clear();
		char s[100];
		int t;
		scanf("%s%d", &s, &t);
		for(int j = 0; j < t; j++)
		{
			scanf("%s", &s);
			set.insert(std::string(s));
		}
		printf("%.10lf\n", parse(root, set));
	}
	rm(root);
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
