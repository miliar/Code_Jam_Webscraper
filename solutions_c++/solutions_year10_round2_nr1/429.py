#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <functional>
#include <cmath>
using namespace std;

struct Node
{
	map<string,Node> next;
};

Node root;
char s[101];

int read_patch()
{
	scanf("%s",s);
	Node *t=&root;
	int st=1,k=1;
	string str;
	int res=0;
	for(;;)
	{
		while((s[k]!=0)&&(s[k]!='/'))
			k++;
		str=string(s+st,s+k);
		if(t->next.find(str)==t->next.end())
			res++;
		t=&(t->next[str]);
		if(s[k]==0)
			break;
		else
			st=k=k+1;
	}
	return res;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int num_tests;
	scanf("%d",&num_tests);
	for(int test=1;test<=num_tests;test++)
	{
		printf("Case #%d: ",test);
		int n,m;
		root.next.clear();
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			read_patch();
		long long res=0;
		for(int i=0;i<m;i++)
			res+=read_patch();
		printf("%lld\n",res);
	}
	fclose(stdout);
	return 0;
}