#include<iostream>
#include<string>
using namespace std;

struct node{
	int cnt;
	node* next[26];
	node()
	{
		cnt=0;
		memset(next,0,sizeof(next));
	}
	~node()
	{
		for (int i=0;i<26;i++)
			delete next[i];
	}
};

void insert(char* s, int len, node* &t)
{
	if (t==NULL) t=new node;
	if (len==0) t->cnt++;
	else insert(s+1,len-1,t->next[s[0]-'a']);
}

int l,d,n;
node* tree;
string q[15];

int count(node* t, int indx)
{
	if (t==NULL) return 0;
	if (t->cnt>0) return t->cnt;

	int i,ans=0;
	for (i=0;i<q[indx].length();i++)
		ans+=count(t->next[q[indx][i]-'a'],indx+1);
	return ans;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);

	cin>>l>>d>>n;
	
	int i,j;
	char tmp[1000];

	tree=NULL;
	for (i=0;i<d;i++)
	{
		cin>>tmp;
		insert(tmp,strlen(tmp),tree);
	}

	int p;
	for (i=1;i<=n;i++)
	{
		cin>>tmp;
		p=0;
		
		for (j=0;j<l;j++)
		{
			q[j]="";

			if (tmp[p]!='(') 
			{
				q[j]+=tmp[p];p++;
			}
			else
			{
				p++;
				while (tmp[p]!=')')
				{
					q[j]+=tmp[p];
					p++;
				}
				p++;
			}
		}
		printf("Case #%d: %d\n",i,count(tree,0));
	}
}
