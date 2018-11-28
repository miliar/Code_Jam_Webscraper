#include<iostream>
using namespace std;
#define NUM_CHARS 26 
#define MAX 26
int l,d,n;
typedef struct trie
{
	char* data; // 附加数据
    struct trie * next[NUM_CHARS]; // 指针域
	int branches; // 存放该节点的后续节点分支数
	bool cnt;// 记录是否是单词
}*Trie,Node;
Trie root;
void init()     //初始化
{
	root = (Trie)malloc(sizeof(Node));
	for(int i=0;i<MAX;i++)
		root->next[i]=NULL;
	root->cnt=0;
}
void del(Trie root)  //释放
{
	if(!root) return ;
	for(int i=0;i<MAX;i++)
	{	
		if(root->next[i])
			del(root->next[i]);
		free(root->next[i]);	
	}
}

void insert(char *a)
{
	Trie t,p = root;	
	int i,j,n=strlen(a);
	for(i=0;i<n;i++)
	{	if(p->next[a[i]-'a']==NULL)
		{
			t=(Trie)malloc(sizeof(Node));
			for(j=0;j<MAX;j++)
				t->next[j]=NULL;
			t->cnt=0;
			p->next[a[i]-'a'] = t;
		}
		p=p->next[a[i]-'a'];
	}
	p->cnt=1;
}

int find(char *a)
{
    int cc;     
	Trie p = root;	
	int i=0;
    while(p&&a[i]) 
    { 
		if (a[i]>='a' && a[i]<='z') 			
			cc = a[i]-'a'; 
        else 			
			return -1;
		p=p->next[cc];        
		i++; 
	}
	if ( p&&p->cnt==1)      
		return 1;
	else   return 0;
}
int search(Trie r,char *a,int k,int m)
{
	int cc;
	Trie p = r;
	int i=k,j,res=0;;
	if (m==l) return 1;
	if (a[k]<='z'&&a[k]>='a') 
	{
		cc=a[i]-'a';
		if (p->next[cc]) res+=search(p->next[cc],a,k+1,m+1);
	}
	else
	{
		i++;
		for (j=i;a[j]!=')';j++);
		while (a[i]!=')')
		{
			cc=a[i]-'a';
			if (p->next[cc]) res+=search(p->next[cc],a,j+1,m+1);
			i++;
		}
	}
	return res;
}
int main()
{
	int i;
	char lib[10000],ss[10000];
	freopen("alien.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	init();
	for (i=1;i<=d;i++)
	{
		scanf("%s",lib);
		insert(lib);
	}
	for (i=1;i<=n;i++)
	{
		scanf("%s",ss);
		printf("Case #%d: %d\n",i,search(root,ss,0,0));
	}
	return 0;
}
