using namespace std;

#include <set>
#include <map>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <utility>
#include <iomanip>
#include <fstream>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>

#define oo 1<<30
#define f first
#define s second
#define II inline
#define db double
#define ll long long
#define pb push_back
#define mp make_pair
#define Size(V) ((int)(V.size()))
#define all(v) v.begin() , v.end()
#define CC(v) memset((v),0,sizeof((v)))
#define CP(v,w) memcpy((v),(w),sizeof((w)))
#define FOR(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define REP(i, N) for (int (i)=0;(i)<(int)(N);++(i))
#define FORit(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define IN "code.in"
#define OUT "code.out"
#define N_MAX (1<<11)

typedef vector<int> VI;
typedef pair<int,int> pi;
typedef vector<string> VS;
template<class T> string toString(T n) {ostringstream ost;ost<<n;ost.flush();return ost.str();}

int T,N,M;
int Sum[N_MAX][N_MAX],Sol[N_MAX],C2[N_MAX][N_MAX],C1[N_MAX][N_MAX],S[N_MAX][N_MAX];
bool C[N_MAX][N_MAX],B[N_MAX][N_MAX];

II void scan()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);
	scanf("%d",&T);
}

II void solve(int TestCase)
{
	CC(S);
	CC(Sol);
	CC(Sum);
	CC(C);
	CC(B);
	
	fprintf(stderr,"Time %d ms [reset before test %d]\n",TestCase);
	
	scanf("%d%d",&M,&N);
	char aux;
	
	FOR(i,1,M)
	{
		int poz = 1;
		FOR(j,1,N / 4)
		{
			scanf(" %c",&aux);
			if(aux >= 'A' && aux <= 'F')
				aux = aux - 'A' + 1 + 9;
			else
				aux -= '0';
			
			for(int nr = 4;aux;aux >>= 1)
				if(aux & 1)
					B[i][poz + --nr] = true;
				else
					B[i][poz + --nr] = false;
			
			poz += 4;
		}
	}
	
	for(int i = M;i >= 1;--i)
	FOR(j,1,N)
		C1[i][j] = (B[i][j] != B[i+1][j]) ? C1[i+1][j] + 1 : 1;
	
	FOR(i,1,M)
	for(int j = N;j >= 1;--j)
		C2[i][j] = (B[i][j] != B[i][j+1]) ? C2[i][j+1] + 1 : 1;
	
	FOR(i,1,M)
	FOR(j,1,N)
	{
		int size = min( min(M - i + 1,N - j + 1),C2[i][j] );
		FOR(k,1,size)
		{
			size = min(size,C1[i][j + k - 1]);
			S[i][j] = max(S[i][j], min(size,k) ); 
		}
	}
	
	for(int size = min(N,M);size >= 1;--size)
	FOR(i,1,M)
	FOR(j,1,N)
	{
		if(S[i][j] < size)
			continue;
		
		bool ok = true;
		
		FOR(k,j,j + size - 1)
			if(Sum[k][i] != Sum[k][i + size])
			{
				ok = false;
				break;
			}
		
		if(!ok)
			continue;
		
		FOR(k1,j,j + size - 1)
		{
			FOR(k2,i,i + size - 1)
				C[k1][k2] = true;
			for(int k2 = i + size - 1;k2 >= 1;--k2)
				Sum[k1][k2] = Sum[k1][k2 + 1] + C[k1][k2];
		}
		
		++Sol[size];
	}
	
	int rez = 0;
	for(int size = min(N,M);size >= 1;--size)
		rez += (Sol[size] >= 1);
	printf("Case #%d: %d\n",TestCase,rez);
	
	for(int size = min(N,M);size >= 1;--size)
		if(Sol[size] != 0)
			printf("%d %d\n",size,Sol[size]);
		
	fprintf(stderr,"Time %d ms [after test %d]\n",TestCase);
}

int main()
{
	scan();
	FOR(i,1,T)
		solve(i);
	return 0;
}
