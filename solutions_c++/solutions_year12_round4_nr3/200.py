#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<queue>
using namespace std;

#define LL long long

const int MaxN = 20000;
const int lim = 800000000;
int N;
int T[MaxN], H[MaxN];

LL cross(LL a, LL b, LL c, LL d, LL e, LL f)
{
	return (c-a)*(f-b)-(e-a)*(d-b);
}

bool Solve(int L, int R, LL x, LL y, LL a, LL b)
{
	if(L >= R) return true;
	// H[R] is fixed
	bool flag=false;
	for(int i=L;i<R;++i) {
		if(T[i] > R) return false;
		if(T[i]==R) flag=true;
	}
	if(!flag) return false;


	//cout << ">> Calc < "<<L<<" , "<<R<<" > "<<endl;

	for(int i=L;i<R;++i)
		if(T[i]==R)
		{
			LL lo = -lim, hi = y, mid;
			while(lo+1<hi)
			{
				mid=(lo+hi)/2;
				if(cross(x,y,R,H[R],i,mid)>=0
					&&cross(x,y,a,b,i,mid)>0)lo=mid;else hi=mid;
			}
			H[i] = lo;
			if(!Solve(L, i, R, H[R], a, b) || !Solve(i+1, R, x, y, i, H[i])) return false;
			return true;
		}
	return false;
}

bool run()
{
	scanf("%d", &N);
	for(int i=1;i<N;++i) scanf("%d", T+i);

	H[N] = lim;
	H[N+1]=lim;
	H[0] = lim+1;
	if(!Solve(1, N, N+1, lim, 0, lim+1)) {
		puts(" Impossible");
		return false;
	}
	int low=*min_element(H+1,H+N+1);
	for(int i=1;i<=N;++i) {
		H[i]-=low;
		printf(" %d", H[i]);
	}
	puts("");
	
	return true;
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int test;scanf("%d", &test);
	for(int no=1;no<=test;++no)
	{
		printf("Case #%d:",no);

		cerr << "no#"<<no<<endl;

		run();
	}
	return 0;
}