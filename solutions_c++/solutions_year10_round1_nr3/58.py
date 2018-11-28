// by shik
#include <iostream>
#include <map>
using namespace std;
map<int,bool> tbl[2000010];
int st[1000010],ed[1000010];
bool go( int a, int b ) {
	if ( a<b ) swap(a,b);
	if ( b<=0 ) return 1;
	if ( tbl[a].find(b)!=tbl[a].end() ) return tbl[a][b];
	for ( int i=a/b*b; i>0; i-=b )
		if ( !go(a-i,b) ) return tbl[a][b]=1;
	return tbl[a][b]=0;
}
void pre_calc() {
	int n=1000000,i,j,k;
	for ( i=j=k=1; i<=n; i++ ) {
		while ( go(i,j) ) j++;
		while ( !go(i,k) ) k++;
		st[i]=j;
		ed[i]=k-1;
	}
}
int main()
{
	pre_calc();
	int t,T,x1,x2,y1,y2,i;
	long long ans;
	scanf("%d",&T);
	for ( t=1; t<=T; t++ ) {
		scanf("%d%d%d%d",&x1,&x2,&y1,&y2);
		ans=(long long)((x2-x1+1))*(y2-y1+1);
		for ( i=x1; i<=x2; i++ ) {
			ans-=max(min(ed[i],y2)-max(st[i],y1)+1,0);
		}
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}
