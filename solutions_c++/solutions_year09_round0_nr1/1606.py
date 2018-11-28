#include<iostream>
using namespace std;
char s[5001][20];
char a[10000];
struct ff
{
	char str[1000];
	int num;
}f[1000];
int n;
int sum;
int l,m;
#define SIZE 10000000

struct trie_tree
{
    int  flag;
    int next[26];
    void Init()
    {
        memset( next,-1,sizeof(next) );
        flag=-1;
    }
}Trie[SIZE];
int num;
void Insert(char *p)
{
    int i,pos,Index=0;
    for(i=0; p[i] ;i++)
    {
        pos=p[i]-'a';

        if( Trie[ Index ] .next[pos] == -1 )
        {
            Trie[ ++num ].Init();
            Trie[ Index ].next[ pos ] = num; 
        }

        Index = Trie[ Index ] .next[pos];
        //Trie[ Index ].flag++;
    }
    Trie[ Index ].flag=1;
    return ;

}
int  find(char *p)
{
    int i,pos,Index=0;
    for(i=0; p[i] ;i++)
    {
        pos=p[i]-'a';
        if( Trie[ Index ].next[pos] == -1 )
        {
            
            return 0;
        }
        Index=Trie[ Index ].next[pos];
    }
    return Trie[ Index ].flag;
    
}

void dfs(int bushu,char * p)
{
	int i;
	if(bushu==n)
	{
		p[n]='\0';
		int haha=find(p);
	//	puts(p);
	//	printf("%d\n",haha);
		if(haha==1)
			sum++;
	}
	p[bushu]='\0';
	if(find(p)==0)
		return ;
	for(i=0;i<f[bushu].num;i++)
	{
		p[bushu]=f[bushu].str[i];
		dfs(bushu+1,p);
	}
	return ;
}
int main()
{
	int d;
	int i,j,k;
	int tt=0;

		freopen("A-large.in","r",stdin);
		freopen("out.out","w",stdout);
    num=0;
    Trie[ num ].Init();

	scanf("%d %d %d",&l,&m,&d);
	{

		for(i=0;i<m;i++)
		{
			scanf("%s",&s[i]);
			Insert(s[i]);
		}

		while(d--)
		{
			tt++;
		scanf("%s",&a);
		n=0;
		f[0].num=0;
		for(i=0;a[i]!='\0';i++)
			if(a[i]>='a' || a[i] <= 'z')
				break;
		for(i=0;a[i]!='\0';i++)
		{
			if(a[i]=='(')
			{
				for(j=i+1,k=0;a[j]!=')';j++,k++)
					f[n].str[k]=a[j];
				f[n].str[k]='\0';
				f[n].num=k;
				n++;
				i=j;
			}
			else 
			{
				f[n].num=1;
				f[n].str[0]=a[i];
				n++;
			}
		}
		sum=0;
		char ss[100];
		dfs(0,ss);
		printf("Case #%d: ",tt);
		printf("%d\n",sum);
		}
	}
	return 0;
}
