#include<iostream>

using namespace std;

struct Node
{
	char feat[11];
	int left,right,father;
	double pob;
}tree[100000];

char tmpstr[100];
char name[100];
char feature[101][101];
char str[8000];

int k; 

void build_tree()
{
	int len = strlen(str);
	int now = 0;
	int node = 0;
	int Tail = 0;
	while(now < len)
	{
		if (str[now] == '(')
		{
			Tail++;
			if (tree[node].left == -1)
			{
				tree[node].left = Tail;
				tree[Tail].father = node;
			}
			else
			{ 
				tree[node].right = Tail;
				tree[Tail].father = node;
			}
			node = Tail;
			now++;
		}
		else 
		if (str[now] == ')')
		{
			node = tree[node].father;
			now++;
		}
		else
		if (str[now] == '0' || str[now] == '1')
		{
			double tmp = 0;
			if (str[now] == '0') tmp = 0; else tmp = 1;
			now += 2;
			double r = 0.1,f = 0;;
			while(str[now] >= '0' && str[now] <= '9')
			{
				f += r *  (str[now] - 48);
				r *= 0.1;
				now++;
			}
			tree[node].pob = tmp + f;
		}
		else
		if (str[now] >= 'a' && str[now] <= 'z')
		{
			char tmp[20];
			int d = 0;
			while(str[now] >= 'a' && str[now] <= 'z')
			{
				tmp[d++] = str[now];
				now++;
			}
			tmp[d] = 0;
			strcpy(tree[node].feat,tmp);
		}
		else now++;
	}
}

double cal(int now)
{
	if (now == -1) return 1;
	for (int i = 0; i < k; i ++)
		if (strcmp(feature[i],tree[now].feat) == 0)
			return tree[now].pob * cal(tree[now].left);
	return tree[now].pob * cal(tree[now].right);
}

int main()
{
	int T;
	scanf("%d\n",&T);
	for (int t = 0; t < T; t ++)
	{
		printf("Case #%d:\n",t + 1);
		int L;
		scanf("%d\n",&L);
		strcpy(str,"");
		for (int i = 0; i < L; i++)
		{
			gets(tmpstr);
			strcat(str,tmpstr);
		}
		
		for (int i = 0; i < 100000; i ++)
		{
			tree[i].left = tree[i].right = -1;
			tree[i].pob = 0;
			tree[i].father = 0;
		}

		build_tree();
		
		int Q;
		scanf("%d\n",&Q);
		for (int q = 0; q < Q; q++)
		{
			scanf("%s",name);
			scanf("%d",&k);
			for (int i = 0; i < k; i++)
				scanf("%s",feature[i]);
			printf("%.7lf\n",cal(1));
		}
	}
	return 0;
}
