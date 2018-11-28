//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#define maxn 10000000
typedef long long LL;

using namespace std;
int		l[20],cnt,p[maxn]; 
int		num[maxn];
int		find(int x )
{
	if ( p[x] != x ) p[x] = find(p[x]); 
	return p[x]; 
}

int		move(int i ) 
{
	for (cnt = 0; i ; cnt++ , i /= 10) l[cnt] = i%10; 
	if ( cnt > 1 && l[cnt-2] == 0 ) return -1; 
	int x = 0; 
	for (int i = cnt-2; i>=0; i-- ) 
		x = x*10+l[i]; 
	x = x*10 + l[cnt-1]; 
	return x; 
}
int		main()
{
	int cas,tt = 0 , A , B; 
	scanf("%d", &cas ); 
	for (int i = 1; i<maxn; i++) p[i] = i;
	for (int i = 1; i<maxn; i++)
	{
		int j = move(i); 
		if ( j != -1 ) p[find(i)] = find(j); 
	}
	while ( cas -- )
	{
		scanf("%d%d", &A , &B );
		memset( num , 0 , sizeof(num) ); 
		for (int i = A; i<=B; i++) 
			num[find(i)] ++; 
		long long ans = 0; 
		for (int i = 1; i<maxn; i++)
			ans += (long long)num[i]*(num[i]-1)/2;
		printf("Case #%d: ", ++tt );
		cout<<ans<<endl; 
	}
}
