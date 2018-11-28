# include <stdio.h>
# include <vector>
# include <stdlib.h>
# include <string>
# include <math.h>
using namespace std;

int Com[33][33] , c ;
int d , Opp[33][33] ;
vector < char > ret ;

int main ()
{
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int tc ; 
	scanf ("%d",&tc);
	char seq[111];
	for ( int k=1 ; k<=tc ; k++ )
	{
		ret.clear();
		memset ( Com , 0 , sizeof Com );
		memset ( Opp , 0 , sizeof Opp );
		scanf ("%d",&c);
		char tmp[11];
		for ( int i=0 ; i<c ; i++ )
		{
			scanf ("%s",tmp);
			Com [ tmp[0]-'A' ] [ tmp[1]-'A' ] = tmp[2]-'A' ;
			Com [ tmp[1]-'A' ] [ tmp[0]-'A' ] = tmp[2]-'A' ;
		}
		scanf ("%d",&d) ;
		for ( int i=0 ; i<d ; i++ )
		{
			scanf ("%s",tmp);
			Opp [ tmp[0]-'A' ] [ tmp[1]-'A' ] = 1 ;
			Opp [ tmp[1]-'A' ] [ tmp[0]-'A' ] = 1 ;
		}
		int n ;
		scanf ("%d%s",&n,seq);
		for ( int i=0 ; i<n ; i++ )
		{
			ret.push_back (seq[i]);
			if ( i==0 ) continue ;
			if ( ret.size() > 1 )
				if ( Com [ ret[ret.size()-1]-'A' ] [ ret[ret.size()-2]-'A' ] )
			{
				char tmp = Com [ ret[ret.size()-1]-'A' ] [ ret[ret.size()-2]-'A' ]+'A';
				ret.pop_back();
				ret.pop_back();
				ret.push_back(tmp);
				continue;
			}
			for ( int j=0 ; j<ret.size()-1 ; j++ )
				if ( Opp [ ret[ret.size()-1]-'A' ] [ ret[j]-'A' ] )
				{
					ret.clear();
					break;
				}
		}
		printf ("Case #%d: [",k);
		if ( !ret.size() )
		{
			printf("]\n");
			continue;
		}
		for ( int i=0 ; i<ret.size() ; i++ )
		{
			if ( i != ret.size()-1 )
				printf ("%c, ",ret[i]);
			else
				printf ("%c]\n",ret[i]);
		}
	}
	//while(1);
}