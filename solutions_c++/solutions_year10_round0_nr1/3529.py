#include <iostream>
using namespace std;

struct Node {
	bool on;
	bool power;
}node[40];
int n;
bool check() {
	if( node[1].on || !node[1].power ) return false;
	for( int i = 2 ; i <= n ; i++ )
		if( node[i].on || node[i].power ) return false;
	return true;
}

void sim() {
	int i;
	for( i = 1 ; i <= n ; i++ ){
		if( !node[i].power ) break;
		node[i].on = !node[i].on;
	}
	i = 1;
	node[1].power = true;
	while( i < n ) {
		if( !node[i].on ) break;
		node[i+1].power = true;
		i++;
	}
	while( i <= n && node[i].on ) i++;
	if( i <= n ) node[i++].power = true;
	while( i <= n ) node[i++].power = false;

//	for( i = 1 ; i <= n ; i++ )
	//	printf("%d %d\n", node[i].on, node[i].power);
	//for( i = 1 ; i <= 200000000 ; i++ );
}

int main()
{
	int cnt;
	int t,k;
	int cc;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w", stdout);
	cc = 0;
	cin >> t;
	while( t-- && cin >> n >> k ) {
		memset(node,0,sizeof(node));
		cnt = 0;
		node[1].on = false;
		node[1].power = true;
		k %= (1<<n);
		
		printf("Case #%d: %s\n", ++cc, k==(1<<n)-1 ?  "ON" : "OFF" );
	}
	return 0;
}