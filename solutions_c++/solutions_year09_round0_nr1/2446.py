#include <stdio.h>
#include <string.h>
class Node
{
public:
	Node* pNode[27];
	Node()
	{
		for(int i=0;i<27;i++)
		{
			pNode[i] = NULL;
		}
	}
};
class Trie
{
public:
	Node * pNode;
	void insert(char *ch,int len);
	Trie()
	{
		pNode = new Node();
	}
	~Trie();
	void deleteNode(Node *p);

};
void Trie::deleteNode(Node *p)
{
	for(int i=0;i<27;i++)
	{
		if(p->pNode[i]!=NULL)
		{
			deleteNode(p->pNode[i]);
			delete(p->pNode[i]);
			p->pNode[i] = NULL;
		}
	}
}
Trie::~Trie()
{
	deleteNode(pNode);
}
void Trie::insert(char *ch,int len)
{
	Node *p = pNode;
	for(int i=0;i<len;i++)
	{
		if(p->pNode[ch[i]-'a']==NULL)
		{
			p->pNode[ch[i]-'a'] = new Node();
			
		}
		p = p->pNode[ch[i]-'a'];
		
	}
}
int count;
void dfs(Node *node, bool buf[][30],int row,int len)
{
	if(row == len-1)
	{
		for(int i=0;i<30;i++)
			if(buf[row][i] && node->pNode[i]!=NULL)
				count++;
		
	}
	else
	{
		for(int i=0;i<30;i++)
			if(buf[row][i])
				if( node->pNode[i]!=NULL)
					dfs(node->pNode[i],buf,row+1,len);
	}
}
int main()
{
	int L,D,N,i,j,k;
	char ttt[20];
	bool buf[20][30];
	bool flag =false;
	char c;
	Trie tree;
	freopen("out.txt","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++)
	{
		scanf("%s",ttt);
		tree.insert(ttt,L);
	}
	getchar();
	for(i=1;i<=N;i++)
	{
		memset(buf,false,sizeof(buf));
		j=0;
		count =0;
		while((c=getchar())!='\n')
		{
			if(c == '(')
				flag = true;
			else if(c == ')')
			{
				flag = false;
				j++;
			}
			else
			{
				if(flag)
				{
					buf[j][c-'a']=true;
				}
				else
				{
					buf[j++][c-'a']=true;
				}
			}
		}
		dfs(tree.pNode,buf,0,L);
		printf("Case #%d: %d\n",i,count);
	}
}
