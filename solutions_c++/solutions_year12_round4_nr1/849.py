#include <iostream>
#include <map>
#include <algorithm>
#include <utility>
#define MAX 110

using namespace std;
typedef long long LL;

#define NMAX 10100

int N, D,
	P[NMAX], L[NMAX],	// pos, len
	S[NMAX];			// max_swing

bool Solve()
{
	for(int i=0; i<=N; ++i) S[i]=0;
	S[0] = P[0];

	for(int i=0; i<N; ++i)
	{
		if(P[i]+S[i]>=D) return true;
		for(int j=i+1; j<N && P[j]<=P[i]+S[i]; ++j) 
		{
			int sj = min(L[j], P[j]-P[i]);
			if(sj>S[j])
				S[j] = sj;
		}
	}

	return false;
}

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		cin>>N;
		for(int i=0; i<N; ++i)
			cin>>P[i]>>L[i];
		cin>>D;
		P[N] = D+1;
		cout<<"Case #"<<test<<": ";
		cout<<(Solve()?"YES":"NO");
		cout<<endl;
	}
	
	return 0;
}

/**
4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14
*/