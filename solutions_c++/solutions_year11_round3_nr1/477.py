#include <cstdio>
#include <cstring>

const int Max = 60;

char mp[Max][Max];
char st[60];
int R,C;

void solve(){
	memset( mp , 0 , sizeof( mp ) );
	scanf("%d%d",&R,&C);
	gets(st);
	for( int i = 0 ; i < R ; ++i ){
		gets( mp[i] );
	}
	bool ok = true;
	for( int i = 0 ; i < R && ok ; ++i ){
		for( int j = 0 ; j < C && ok ; ++j ){
			if( mp[i][j] == '#' ){
				if( mp[i][j+1] != '#' || mp[i+1][j] != '#' || mp[i+1][j+1] != '#' ){
					ok = false;
					break;
				}
				mp[i][j] = '/';
				mp[i][j+1] = '\\';
				mp[i+1][j] = '\\';
				mp[i+1][j+1] = '/';
			}
		}
	}
	if( !ok ){
		printf("Impossible\n");
		return;
	}
	for( int i = 0 ; i < R ; ++i ){
		printf("%s\n",mp[i]);
	}
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; ++i ){
		printf("Case #%d:\n",i);
		solve();
	}
}