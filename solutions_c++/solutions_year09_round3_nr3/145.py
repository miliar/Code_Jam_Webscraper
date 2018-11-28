#include<cstdio>
#include<map>
#include<algorithm>
using namespace std;

map< pair<int,int> , int > hash;

int P,Q;
int a[1000];
int solve( int l,int r,int al,int ar )
{
	if( l>r || al>ar ) return 0;
	if( hash.find( make_pair(l,r) ) !=hash.end() )
		return hash[make_pair(l,r)];

	hash[ make_pair(l,r) ] = 1<<30;
	int &ans = hash[ make_pair(l,r) ];

	for(int i=al;i<=ar;i++) ans = min(ans,solve(l,a[i]-1,al,i-1) + solve(a[i]+1,r,i+1,ar));
	return ans+=r-l;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int TT=1;TT<=T;TT++)
	{
		scanf("%d%d",&P,&Q);
		for(int i=1;i<=Q;i++) scanf("%d",a+i);
		sort(a+1,a+Q+1);
		hash.clear();
		printf("Case #%d: %d\n",TT,solve(1,P,1,Q));
	}
	return 0;
}
