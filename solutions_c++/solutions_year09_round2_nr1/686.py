#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <iostream>
using namespace std;
const int maxn=100000;

set<string> mp;
double p[maxn], ret; 
string id[maxn];
int l, o, ll,leftg[maxn],rightg[maxn],task,cs=0;
char s[maxn], st[maxn];
string all, alls;
int tot;

void readd( int x){
	while ( s[o]!='(' ) o+=1;
	o+=1;
	sscanf(s+o, "%lf%n", &p[x], &ll);
	o+=ll;
	sscanf(s+o, "%s%n", st, &ll);	
	if ( st[0]==')' ){
		id[x] = "-1";
		return;
	}
	id[x] = st;
	tot++;
	leftg[x]=tot;
	readd( tot );
	tot++;
	rightg[x]=tot;
	readd( tot);
	while ( s[o]!=')' ) o++;
	o++;
}

void dfs( int x ){
	ret = ret * p[x];
	if ( id[x]=="-1" ) return;
	if ( mp.count( id[x] )>0 )
		dfs( leftg[x] );else
		dfs( rightg[x] );
}

int main(){
	freopen("A-Small.in","r",stdin);
	freopen("A-Small.out","w",stdout);
	for (scanf("%d\n", &task); task--;){
		all = "";
		tot=0;
		scanf("%d\n", &l); 
		for (int i=1;i <=l; i++){
			gets(s); alls = s;
			all += alls;
		}
		for (int i=0; i<all.length(); i++)
			s[i] = all[i];
		s[all.length()] = 0;
		o = 0;
		readd( tot );
		printf("Case #%d:\n", ++cs);
		int tt, num;
		for (scanf("%d", &tt); tt--;){
			mp.clear();
			for (scanf("%s %d", s, &num);num--;){
				scanf("%s", s);
				alls = s;
				mp.insert( alls );
			}
			ret = 1;
			dfs( 0 );
			printf("%.7lf\n", ret);
		}
	}
	return 0;
} 
