#include<stdio.h>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
using namespace std ;
#define fo(i, n) for (i=0 ; i<n ; i++)

FILE *in = fopen ("input.in", "r") ;
FILE *out = fopen ("output.out", "w") ;

int T, N ;
vector<int> tmp ;

int rank[25] ;


bool check()
{
	int cur = tmp.size() ;

	int i ;
	while(1)
	{
		if (cur==1)
			return true ;

		for (i=0 ; i<cur ; i++)
			if (tmp[i]==cur)
				break ;

		if (i!=cur)
			cur = i+1 ;
		else
			return false ;
	}
		

}
int main()
{
	int i, z, j, ret=0, r ;

	fscanf (in, "%d", &T) ;

	fo(z, T)
	{
		ret = 0 ;
		fscanf (in, "%d", &N) ;

		fo(i, (1<<N)-1)
		{
			if (!(i & 1<<N-1))
				continue ;

			tmp.clear() ;			

			fo(j, N)
				if (i& 1<<j)
					tmp.push_back(j+1) ;

			if (check())
			{
				ret++;
				ret = ret % 100003 ;
			}
		}

		fprintf (out, "Case #%d: %d\n", z+1, ret) ;
		//printf ( "Case #%d: %d\n", z+1, ret) ;
	}

	return 0 ;
}




