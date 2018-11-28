#include<iostream>
#include<map>
#include<stack>
#include<string>
using namespace std;


#define maxn 10000
#define maxm 220

struct node {
	string name;
	double val;
}tree[ maxn ];


string str;
char tems[ maxm * maxm ];
int len;
char ss[maxm];
int hash[ maxm * maxm ];
double out;

void Just() {
	memset( hash, - 1, sizeof(hash) );
	stack< int > hd;
	for( int i = 0; i < len; i ++ ) {
		if( str[i] == '(' ) {
			hd.push(i);
		}
		if( str[i] == ')' ) {
			int x = hd.top();
			hash[x] = i;
			hd.pop();
		}
	}
}

char buf[maxm];
void DFS( int num, int low, int high ) {
	int i = low + 1;
	while( str[i] == ' ' ) i ++;
	double val;
	sscanf(tems + i,"%lf %s", &val, buf);

	int lens = strlen( buf );
	for( int j = lens - 1; j >=0; j -- ) {
		if( !(buf[j] >= 'a' && buf[j] <= 'z') )
			buf[j] = 0;
	}
	tree[num].name = (string) buf;
	tree[num].val = val;

	if( tree[num].name == "" ) return;
	for(; str[i] != '(' && i < high; i ++ );
	DFS( num * 2, i , hash[i] );
	i = hash[i] + 1;
	for(; str[i] != '(' && i < high; i ++ );
	DFS( num * 2 + 1, i, hash[i] );
}

map< string, int > yifenfei;

void Query( int num ) {
	out *= tree[num].val;
	if( tree[num].name == "" ) return;
	if( yifenfei.find( tree[num].name ) != yifenfei.end() ) 
		Query( num * 2);
	else Query( num * 2 + 1 );
}

int main() {
	freopen("D:\\in.in", "r", stdin);
	freopen("D:\\out.out", "w", stdout);
	int T;
	int ca = 0;
	scanf("%d", & T);
	while( T -- ) {
		int n;
		scanf("%d\n", &n);
		str = "";
		for( int i = 0; i < n; i ++ ) {
			scanf("%[^\n]%*c", ss);
			str += ss;
		}
		len = str.size();
		for( int i = 0; i < len; i ++ )
			tems[i] = str[i];
		Just();
		DFS( 1, 0, len - 1 );
		/*
		for( int i = 1; i <= 7; i ++ )
			cout << tree[i].name << " " << tree[i].val << endl;
			*/
		int m, k;
		scanf("%d", &m);

		printf("Case #%d:\n", ++ ca);
		while( m -- ) {
			yifenfei.clear();
			scanf("%s %d",ss,&k);
			while( k -- ) {
				scanf("%s", ss);
				yifenfei[ ss ] = 1;
			}
			out = 1;
			Query( 1 );
			printf("%.7lf\n", out);
		}
	}
	return 0;
}