#include<iostream>
#include<cstring>
#include<vector>
#include<string>
using namespace std;

#define MAXN 15
#define MAXL 128
#define MAXBUF 1000
struct TRIE
{
    int tag,id;
    TRIE* son[MAXL];
    TRIE ()
    {
        for ( int i=0 ; i<MAXL ; i++ )
            son[i]=0;
        tag=id=0;
    }
};
vector<char> lan[MAXN];
int L,N,D;
TRIE* root;

bool add ( char c , TRIE* p )
{
	TRIE *q;

    if( p->son[c]==NULL  )
    {
		q=new TRIE;
        p->son[c]=new TRIE;
        return true;
    }
    return false;
}

void build ( int n )
{
    string buf;
    int i,j,len,k;
    TRIE *p;
    root=new TRIE;
    for ( i=0 ; i<n ; i++ )
    {
        cin>>buf;
        len=buf.size();
        for ( p=root,j=0 ; j<len-1 ; j++ )
        {
            add(buf[j],p);
            p=p->son[buf[j]];
        }
        add(buf[j],p);
        p=p->son[buf[j]];
        p->id=i;
        p->tag=1;
    }
}

void init ( int n )
{
    int i,j,len,k,st;
    string buf;
    for ( i=0 ; i<n ; i++ )
        lan[i].clear();
    cin>>buf;
    k=-1;
	for ( st=i=0 ; i<buf.size() ; i++ )
	{
		if ( st==0 )
		{
			if ( buf[i]=='(' )
			{
				st=1;
				k++;
			}
			else
				lan[++k].push_back(buf[i]);
		}
		else
			if ( st==1 )
			{
				if ( buf[i]==')' )
					st=0;
				else
					lan[k].push_back(buf[i]);
			}
	}

}

void solve ( TRIE* v , int n , int& cnt )
{
    int i;

    for ( i=0 ; i<lan[n].size() ; i++ )
    {
        if ( v->son[lan[n][i]] )
        {
            if ( v->son[lan[n][i]]->tag )
            {
                cnt++;
                continue;
            }
            solve(v->son[lan[n][i]],n+1,cnt);
        }
    }
}

void print ( TRIE * v , int n )
{
    int i;

    for ( i=0 ; i<MAXL ; i++ )
    {

        if ( v->son[i] )
        {
            printf("%c",i);
			if ( v->son[i]->tag )
			{
				printf("\n");
				continue;
			}
            print(v->son[i],n+1);
        }
		//print(v->son[i],n+1);
    }
}
void destroy ( TRIE* v )
{
    if ( v==NULL )
        return ;
    for (int i=0 ; i<MAXL ; i++ )
    {
        destroy(v->son[i]);
    }
    delete v;
}
int main ( )
{
    int i,k,j,res;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    while(  cin>>L>>D>>N )
    {
        build(D);
        //print(root,0);
        for ( i=1 ; i<=N ; i++ )
        {
            init(L);
//            for ( k=0 ; k<L ; k++ )
//            {
//                for ( j=0 ; j<lan[k].size() ; j++ )
//                    printf("%c",lan[k][j]);
//                printf("\n");
//            }
            res=0;
            solve(root,0,res);
            printf("Case #%d: %d\n",i,res);
        }
        destroy(root);
    }
}

