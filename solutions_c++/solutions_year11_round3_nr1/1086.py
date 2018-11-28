#include<cstdio>
#include<string>
#include<cstring>
#include<memory>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define SET(x, v) memset(x, v, sizeof(x))

typedef long long ll;
int r, c;
char p[51][51];

int main() {
    int e = 0, T;

    scanf("%d",&T);
    while(T--) {
        scanf("%d%d",&r,&c);
		for ( int i = 0 ; i < r; ++i)
			scanf("%s\n",p[i]);

		bool possible = true;
        for ( int i = 0 ; i < r; ++i){
			int count = 0;
			for ( int j = 0 ; j < c ; ++j){
				if (p[i][j] == '#')
					count ++;
			}
			if ( count % 2 != 0 ){
				possible=  false;
				break;
			}
		}
		if ( possible){
			for ( int i = 0 ; i < c; ++i){
				int count = 0;
				for ( int j = 0 ; j < r ; ++j){
					if (p[j][i] == '#')
						count ++;
				}
				if ( count % 2 != 0 ){
					possible=  false;
					break;
				}
			}

		}
		if ( possible){
			for ( int i = 0 ; i < r; ++i){
				for ( int j = 0 ; j < c ; ++j){
					if (p[i][j] == '#' && 
						j+1 < c && p[i][j+1] == '#' &&
						i+1 < r && p[i][j] == '#' && 
						p[i+1][j+1] == '#' )
					{
						p[i][j] = '/';
						p[i][j+1] = '\\';
						p[i+1][j] = '\\';
						p[i+1][j+1] = '/';

					}
					else if( p[i][j] == '#'){
						possible = false;
						i= r; j=c;
						break;
					}
				}
			}
		}

		printf("Case #%d:\n", ++e);
		if (!possible) 
		{
			printf("Impossible\n");
		}		// print result
		else{
			
			for ( int i = 0 ; i < r ; ++i)
			{
				printf("%s\n",p[i]);
			}
		}
    }
    return 0;
}
