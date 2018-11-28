#include<iostream>
#include<algorithm>
using namespace std;

#define maxn 110
#define inf 1<<30
char str[maxn];
int len;

int main() {
	freopen("D:\\in.in", "r", stdin );
	freopen("D:\\out.out", "w", stdout);
	int T;
	int ca = 0;
	scanf("%d", &T);
	while( T -- ) {
		scanf("%s", str);
		len = strlen( str );

		bool flag = 0;
		for( int i = len - 1; i >= 0; i -- ) {
			int Min = inf;
			int key = i;
			for( int j = i + 1; j < len; j ++ ){
				if( str[j] > str[i] && str[j] <= Min ) {
					Min = str[j];
					key = j;
				}
			}
			if( Min != inf ) {
				flag = 1;
				swap( str[i], str[key] );
				sort( str + i + 1, str + len );
				break;
			}
		}

		if( !flag ) {
			int Min = inf;
			int key = 0;
			for( int i = 0; i < len; i ++ ) {
				if( str[i] == '0' ) continue;
				if( str[i] < Min ) {
					Min = str[i];
					key = i;
				}
			}
			swap(str[0], str[key]);
			sort( str + 1, str + len );
			for( int i = len; i > 1; i -- )
				str[i] = str[i - 1];
			str[1] = '0';
			str[len + 1] = 0;
		}
		printf("Case #%d: %s\n",++ca, str);
	}
	return 0;
}