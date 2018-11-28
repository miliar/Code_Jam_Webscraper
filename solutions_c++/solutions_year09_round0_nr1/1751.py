#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>
#include <cstdio>
#include <cstring>
using namespace std ;
int L , D , N ;
struct Node
{
	Node *nex[27] ;
};
char str[10000] ;
vector<char>vec[100] ; 
void create(Node *root , int pos )
{
	if( pos == L )
		return ;
	int id = str[pos]-'a' ;
	if( root->nex[id] == NULL)
	{
		root->nex[id] = new Node() ;
		memset(root->nex[id] , false , sizeof(root->nex[id])) ;
	}
	create(root->nex[id] , pos+1) ;
	return ; 
}
void query(Node *root , int pos , int &res )
{
	if(pos == L )
	{
		res ++ ;
		return ;
	}
	int id , i ; 
	for ( i = 0 ; i < vec[pos].size() ; i ++)
	{
		id = vec[pos][i]-'a' ;
		if( root->nex[id] != NULL )
			query(root->nex[id] , pos+1 , res );
	}
	return ; 
}
int main()
{
	freopen("A-large.in","r",stdin) ;
	freopen("A-large.out","w",stdout) ;
	while ( 3 == scanf("%d%d%d",&L,&D,&N))
	{
		int i , j , len , cnt , res = 0 ; 
		Node *root = new Node(); 
		memset(root->nex , NULL , sizeof(root->nex) ) ;
		for ( i = 0 ; i < D ; i ++)
		{
			scanf("%s",str) ; 
			create(root , 0 ) ; 
		}
		for ( i = 0 ; i < N ; i ++)
		{
			scanf("%s",str) ;
			len = strlen(str) ;
			cnt = 0 ; 
			for ( j = 0 ; j < len ; j ++)
			{
				if( str[j] == '(' )
				{
					j ++ ; 
					vec[cnt].clear() ; 
					while ( str[j] != ')')
					{
						vec[cnt].push_back(str[j]) ;
						j ++ ; 
					}
					cnt ++ ; 
				}
				else
				{
					vec[cnt].clear() ; 
					vec[cnt++].push_back(str[j]) ;
				}
			}
			res = 0 ; 
			query( root , 0  ,res ) ; 
			printf("Case #%d: %d\n",i+1,res) ;
		}
	}
	return 0 ; 
}