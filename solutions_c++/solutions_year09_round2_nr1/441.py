#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <ctime>
#include <string>
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>

#define inputfilename "input"
#define outputfilename "a.out"

using namespace std;

struct node
{
	double p;
	string name;
	int left , right;
	int parent;
}tree[1000];

int num;

int read(int father)
{
	num ++;
	int n = num;
	tree[n].left = -1;
	tree[n].right = -1;
	tree[n].name.clear();
	tree[n].parent = father;
	char c;
	do
	{
		c = getchar();
	}
	while (c != '(');
	scanf("%lf" , &tree[n].p);
	do
	{
		c = getchar();
	}
	while( !( (c >= 'a' && c <= 'z') || (c == ')') ) );
	
	if (c != ')')
	{
		string s;
		s.clear();
		s = s + c;
		do
		{
			c = getchar();
			if (c < 'a' || c > 'z') break;
			s = s + c;
		}
		while (1);
		tree[n].name = s;
		tree[n].left = read(n);
		tree[n].right = read(n);
		do
		{
			c = getchar();
		}
		while ( c != ')');
	}
	return n;
}

int main ()
{
	//freopen(inputfilename , "r" , stdin);
	/*freopen(outputfilename , "w" , stdout);*/

	int number , times;
	scanf("%d" , &number);
	for (times = 0 ; times <  number ; times ++)
	{
		printf("Case #%d:\n", times+1);
		
		int l;
		scanf("%d" , &l);
		num = -1 ;
		read(-1);

		int N , loop;
		scanf("%d" , &N);
		for (loop = 0 ; loop < N ; loop++)
		{
			char buf[1000];
			scanf("%s" , &buf);
			int n;
			scanf("%d" , &n);
			int i;
			set <string> fea;
			for (i = 0 ; i < n ; i++)
			{
				scanf("%s" , &buf);
				string s(buf);
				fea.insert(buf);
			}

			int pos = 0;
			double p = 1;
			do
			{
				p *= tree[pos].p;
				if (tree[pos].left == -1) break;
				if (fea.find(tree[pos].name) != fea.end())
				{
					pos = tree[pos].left;
				}
				else
				{
					pos = tree[pos].right;
				}
			}
			while (1);

			printf("%.7lf\n" , p);
		}
	}



	return 0;
}

 
