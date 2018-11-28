#include<cstdio>
#include<vector>
#include<cstring>
using namespace std;
const int maxn = 105;

int i , t , n , j ,list[2][maxn] , ind[2] , poz[2] , pos;
vector < pair <int , int > > v;
char type;

int main()
{
	freopen("bot.in","r",stdin);
	freopen("bot.out","w",stdout);
	
	scanf("%d",&t);
	
	for( i = 1 ; i <= t ; ++i ) {
		int ans = 0 , cnt1 = 0 ,cnt0 = 0;
		scanf("%d ",&n);
		poz[0] = 1 , poz[1] = 1 , ind[0] = 1 , ind[1] = 1;
		v.clear();
		memset( list , 0 , sizeof(list));
		
		for( j = 1 ; j <= n ; ++j ) {
			scanf("%c %d ",&type,&pos);
			if( type == 'O') 
				list[0][++cnt0] = pos,
				v.push_back( make_pair(0 , pos));
			else
				list[1][++cnt1] = pos,
				v.push_back( make_pair(1 , pos));
		}
		
		scanf("\n");
		
		for( j = 0 ; j < n ; ++j ) {
			int act = v[j].first , other = act ^ 1;
			int t = abs( poz[act] - v[j].second ) + 1;
			poz[act] = v[j].second;
			int go = poz[other] - list[other][ind[other]];
				if ( go < 0 )
					poz[other] += min(-go , t);
				else
					poz[other] -= min(go , t);
			ans += t;
			ind[act]++;
		}
		
		printf("Case #%d: %d\n",i,ans);
	}
	
return 0;
}