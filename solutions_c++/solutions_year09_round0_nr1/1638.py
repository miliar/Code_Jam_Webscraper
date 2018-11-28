#include <iostream>
#include <cstring>

#define MAX  26

int L , N , D , cnt;
int s[20][30];

struct tire {
	struct tire *next[MAX];
	int  isword;
} *root;

struct tire *init()
{
	struct tire *root=(struct tire *)malloc(sizeof(struct tire));
	int i;
	for(i=0;i<MAX;i++)root->next[i]=NULL;
	root->isword=0;
	return root;
} 

void insert(char path[])
{
	struct tire *t,*p=root;
	int i,j,n=L;

	for(i=0;i<n;i++)
	{
		if(p->next[path[i]-'a']==NULL) 
		{
			t=(struct tire *)malloc(sizeof(struct tire));
			for(j=0;j<MAX;j++) 
				t->next[j]=NULL;
			t->isword=0;
			p->next[path[i]-'a']=t;
		}
		p=p->next[path[i]-'a'];
	}
	p->isword=1;
}
int find(char path[])
{
	struct tire *p=root;
	int i,n=strlen(path); 
	i=0;
	while(p&&path[i]) p=p->next[path[i++]-'a'];
	if(p&&p->isword)
		return 1;
	return 0;
}

void dfs(int j , tire *p)
{
	//struct tire *p=root;
	if( p == NULL )
		return;

	if( j == L )
	{
		if(p&&p->isword)
			cnt++;
		return;
	}

	int i;
	//struct tire *pp = (struct tire *)malloc(sizeof(struct tire));
	struct tire *pp;
	for( i = 1 ; i <= s[j][0] ; i++)
	{
		pp = p->next[s[j][i]-'a'];
		dfs(j+1 , pp);			
	}
}

int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	char word[256] , c;
	int i , j , b;
	
	root = init();
	scanf("%d%d%d" , &L , &D , &N);
	getchar();
	for( i = 0 ; i < D ; i++)
	{
		gets(word);
		insert(word);
	}
	
	for( i = 0 ; i < N ; i++)
	{
		for( j = 0 ; j < L ; j++)
		{
			c = getchar();
			if(c != '(')
			{
				s[j][0] = 1;
				s[j][1] = c;
			}
			else
			{
				//c = getchar();
				s[j][0] = 0;
				c = getchar();
				while( c != ')')
				{
					++s[j][0];
					s[j][s[j][0]] = c;
					c = getchar();
				}
			}
			
		}
		cnt = 0;
		dfs(0 , root);
		printf("Case #%d: %d\n" , i+1 , cnt);
		getchar();
		
		
	}
	//system("pause");
	return 0;
}

/*


3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

*/