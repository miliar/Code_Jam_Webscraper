#include <iostream>
using namespace std;
#define tiao system("pause")

struct tree
{
	bool isLeaf;
	double w;
	char feature[15];
	tree *l, *r;
}*root;

char s[11111],tmp[111];
char name[111][111];
int lenS;
int l;
int a;
int n;
int ci;
double ans;

void work(tree* &root, char *s, int l, int r)
{
//	cout << l << ' ' << r ; tiao;
	int i,j,k,begin;
	while(s[l] != '(') l++;
	while(s[r] != ')') r--;
	
	begin = l+1;
	while(s[begin] == ' ') begin++;
	root = (tree*)malloc(sizeof(tree));
	sscanf(s+begin,"%lf",&root->w);
//	cout << s + begin ; tiao;
	
	
	while(s[begin] == '.' || isdigit(s[begin])) begin++;
	while(s[begin] == ' ') begin++;
	if (s[begin] == ')')
	{
		root->isLeaf = true;
		root->l = root->r = NULL;
	}
	else
	{
		root->isLeaf = false;
		sscanf(s+begin,"%s",root->feature);
//		cout << s + begin; tiao;
		while(s[begin] != ' ') begin++;
		l = begin;
		while(s[begin] != '(') begin++;
		int cnt = 1;
		while(cnt > 0)
		{
			begin++;
			if (s[begin] == '(') cnt++;
			else if (s[begin] == ')') cnt--;
		}
		work(root->l, s, l, begin);
		work(root->r, s, begin+1, r-1);
	}
}

void calc(tree *root)
{
	ans *= root->w;
	if (root->isLeaf) return;
	bool ok = false;
	for (int i=1; i<=ci; i++)
		if (strcmp(root->feature, name[i]) == 0)
		{
			calc(root->l);
			ok = true;
			break;
		}
	if (!ok) calc(root->r);
}
void print(tree *root)
{
	if (root->isLeaf)
	{
		cout << "( " << root->w << " )";
	}
	else
	{
		cout << "( " << root->w << ' ' << root->feature << ' ';
		print(root->l); 
		cout << ' ';
		print(root->r);
		cout << " )" ;
	}
	
}

int main(void)
{
	int i,j,k,cici,cicici;
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	scanf("%d",&n); 
	for (int cicici=1; cicici<=n; cicici++)
	{
		scanf("%d",&l); gets(tmp);
		strcpy(s,"");
		for (i=1; i<=l; i++)
		{
			gets(tmp);
			strcat(s,tmp);
		}
		
		lenS = strlen(s);
		root = NULL;
		work(root,s,0,lenS - 1);	
		
//		print(root);
		scanf("%d",&a);
		printf("Case #%d:\n",cicici);
		for (i=1; i<=a; i++)
		{
			scanf("%s%d",&tmp,&ci);
			for (j=1; j<=ci; j++)
			{
				scanf("%s",name[j]);
			}
			
			ans = 1;
			calc(root);
			printf("%.7lf\n",ans);
		}
		
	}
//	tiao;
	return 0;
}
