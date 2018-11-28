#include <iostream>
#include <string>
#include <map>
using namespace std ; 

struct Node
{
	double probability  ;
	string feature ;
	bool flag ;
	Node(){feature = "" ; flag = false ; left = NULL ; right = NULL;}
	Node* left ; 
	Node* right ;

	void Add( double p , string f ) ;
	double Cal( double ) ;
} ;

void Node::Add( double p , string f ) 
{
	if( feature == "" && flag == false )
	{
		flag = true ;
		probability = p ;
		feature = f ;
		return ;
	}

	if( left == NULL )
	{
		left = new Node() ;
		left->probability =  p ;
		left->feature = f ;
		if( f == "" ) left->flag = true;
		else 
			left->flag = false ;
	}
	else if( !(left->flag) )
	{
		left->Add(p, f) ;
	}
	
	else if( right == NULL )
	{
		right = new Node() ; 
		right->probability = p ;
		right->feature = f ; 
		if( f == "" ) right->flag = true ;
		else right->flag = false ;
	}
	else right->Add(p , f) ;
	if( right == NULL ) return ;
	if( (left->flag) && (right->flag) )
		flag = true ;
}
map<string , int> Map ;
double Node::Cal( double ans)
{
	if( feature == "" ) return probability ;
	if( Map.find( feature ) != Map.end() )
		return probability*left->Cal(  ans ) ;
	else return probability*right->Cal( ans ) ;
}

int main()
{
	freopen("A-large.in" , "r" , stdin) ;
	freopen("A-large.out" , "w" , stdout) ;
	int T , t ; 
	int n , m , len ; 
	string f ;
	char str[10000] ;
	double p , k  ;
	int i , j ;
	scanf("%d" ,&T) ;
	for(t = 1 ; t <= T ; t++)
	{
		Node *root = new Node() ;
		scanf("%d" , &n) ;
		getchar() ;
		while(n--)
		{
			gets( str ) ;
			len = strlen(str) ;
			for(i = 0 ; i < len ; i++)
				if( str[i] == '.' ) break ;
			if(i == len) continue ;
			if( str[i-1] == '1' )
			{
				p = 1.0 ;
				for(i++ ; i < len ; i++)
				{
					if( str[i] >= '0' && str[i] <= '9' ) continue ;
					else break ;
				}
			}

			else 
			{
				k = 1.0 ;
				p = 0.0 ;
				for(i++ ; i < len ; i++)
				{
					if( str[i] >= '0' && str[i] <= '9' )
					{
						p = p*10 + str[i] - '0' ;
						k *= 10 ;
					}
					else break ;
				}
				p = p/k ;
			}
			while(i < len)
				if( str[i] == ' ' ) i++ ;
				else break ;
			if(str[i] == ')') f = "" ;
			else 
			{
				f = "" ;
				for(; i < len ; i++)
				{
					if( str[i] == ' ' || str[i] == ')' ) break ;
					f += str[i] ;
				}
			}
			root->Add( p , f ) ;
		}

		printf("Case #%d:\n" , t) ;
		scanf("%d" ,&m) ;
		while(m--)
		{
			scanf("%s" , str) ;
			scanf("%d" ,&n) ;
			Map.clear() ;
			for(i= 0 ; i < n; i++)
			{
				cin>>f ;
				Map[f]++ ;
			}
			if( n == 0 )
			{
				Map[""]++ ;
				n = 1 ;
			}
			len = n ; 
			p = root->Cal(1.0) ;
			printf("%.7lf\n" , p) ;
		}
	}
	return 0 ;
}