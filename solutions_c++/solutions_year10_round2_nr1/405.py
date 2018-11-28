#include<stdio.h>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
using namespace std ;
#define fo(i, n) for (i=0 ; i<n ; i++)

FILE *in = fopen ("input.in", "r") ;
FILE *out = fopen ("output.out", "w") ;


int T ;
int N, M, ret ;

vector<string> exist ;
vector<string> job ;
vector<string> cur ;


class node
{
public:

	map<string, node *> next ;
};
node *root ;

vector<string> extract (string s)
{
	vector<string> ret ;
	string tmp ;

	s.erase(s.begin()) ;

	while(s.find('/')!=string::npos)
	{
		tmp = s.substr(0, s.find('/')) ;
		s.erase(s.begin(), s.begin()+tmp.size()+1) ;
		ret.push_back(tmp) ;
	}
	ret.push_back(s) ;

	return ret ;
	
}

void build()
{
	node * curP = root ;

	int i ;
	string s ;
	fo(i, cur.size())
	{
		s = cur[i] ;

		if (curP->next[s]!=0)
			curP = curP->next[s] ;
		else
		{
			node * X = new node ;
			curP->next[s] = X ;
			curP = X ;
		}
	}
}

void calc()
{
	int i ;
	node *curP = root ;
	

	fo(i, cur.size())
	{
		if (curP->next[cur[i]]!=0)
			curP = curP->next[cur[i]] ;
		else
			break ;		
		
	}

	ret+= cur.size() - i ;
	build() ;	
}
		

int main()
{
	fscanf (in, "%d", &T) ;

	int z, i ;
	char x[120] ;
	string s ;

	fo(z, T)
	{
		ret = 0 ;
		root = new node ;
		exist.clear() ;
		job.clear() ;

		fscanf (in, "%d %d", &N, &M) ;

		fo(i, N)
		{
			fscanf (in, "%s", x) ;
			s = x ;
			exist.push_back(s) ;
		}
		fo(i, M)
		{
			fscanf (in, "%s", x) ;
			s = x ;
			job.push_back(s) ;
		}

		fo(i, N)
		{
			cur = extract(exist[i]) ;
			build() ;
		}
		fo(i, M)
		{
			cur = extract(job[i]) ;
			calc() ;
		}

		fprintf (out, "Case #%d: %d\n", z+1, ret) ;
	}


	return 0 ;
}