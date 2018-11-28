#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
char search[110][110];
char query[1100][110];
int main()
{
	int s,q,cur_ind,tn; 
	int casen=1;
	scanf("%d",&tn);
	while ( tn-- > 0 ) 
	{
		memset(search,0,sizeof(search) );
		scanf("%d ",&s);
		for ( int i = 0 ; i < s;i++)
			gets(search[i]);
		
		scanf("%d ",&q);
		for ( int i = 0 ; i < q;i++)
			gets(query[i]);
		int ans = 0 ; 
		int max_adv;
		cur_ind = 0 ;
		do 
		{
			max_adv=0;
			for ( int cur_search = 0 ; cur_search < s; cur_search++) // current search engine
			{
				int adv;
				for ( adv = 0 ; cur_ind+adv < q ; adv++)
				{
					if ( strcmp ( query[ cur_ind + adv ], search[cur_search] ) ==0 )
						break;
				}
				if ( max_adv < adv ) 
					max_adv = adv;
			}
			cur_ind+= max_adv;
			if ( max_adv > 0 ) ans++;
		} while ( cur_ind < q ) ;

		ans--; if( ans < 0) ans = 0 ; 
		printf("Case #%d: %d\n",casen++,ans);
	}
	return 0 ; 
}
