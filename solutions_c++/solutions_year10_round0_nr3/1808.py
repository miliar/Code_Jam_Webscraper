#include<cstdio>
#include<fstream>
#include<queue>
#include<cstring>
#define ll long long
using namespace std;
const int maxn = 1052;
ll int i , j , t , n , r , k , A[maxn] ; 
ll int cost[maxn] , poz[maxn];
ll int seen[maxn];
ofstream fout("C2.out");
ll int solve() {
	
	ll int sum , j , i;
	ll int aux = r , cnt = 0 , act;
	queue <int> Q;
	while ( !Q.empty()) Q.pop();
	for( i = 1 ; i <= n ; ++i ) 
		Q.push(i);
	
	memset( poz , 0 , sizeof(poz) );
	memset( cost , 0 , sizeof(cost) );
	memset(seen ,0 , sizeof(seen));
	bool ok = false;
	
	for( ; aux ; ) {
		act = Q.front();
		if ( seen[act] ) {ok = true ; break;}
		seen[act] = true;
		sum = 0;
		do  {
			sum += A[Q.front()];
			Q.push(Q.front());
			Q.pop();
		} while( sum + A[Q.front()] <= k  && Q.front() != act); 
		cost[++cnt] = cost[cnt - 1] + sum;
		poz[act] = cnt;
		aux --;
	}

	ll int result = cost[cnt];
	if ( ok ) {
	result += 1LL * (aux / (cnt - poz[act] + 1) ) * ( cost[cnt] - cost[poz[act] - 1] );
	result += cost[poz[act] + aux % (cnt - poz[act] + 1 ) - 1] - cost[poz[act] - 1];
	}
	return result;
}
int main()
{
	freopen("C2.in","r",stdin);
	//freopen("C.out","w",stdout);
	
	scanf("%lld",&t);
	
	for( i = 1 ; i <= t ; ++i ) {
			scanf("%lld %lld %lld",&r,&k,&n);
			for( j = 1 ; j <= n ; ++j ) scanf("%lld",&A[j]);
			fout <<"Case #"<<i<<": "<<solve()<<'\n';
	}
	return 0;
}