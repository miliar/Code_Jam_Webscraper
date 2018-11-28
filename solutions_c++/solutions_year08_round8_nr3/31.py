#include <cstdio>
#include <algorithm>
#include <vector>
#define LLD long long int
#define MOD 1000000009

using namespace std;

class Tro
{
public:
	int A,B,C;
	Tro(int a,int b,int c):A(a),B(b),C(c){}
};

vector<int> Graf[501];
int Dis[501][501];
LLD S;
LLD Wynik;
int Mark[501];
vector< pair<int,int> > Kraw;

int Odlg( pair<int,int> A, pair<int,int> B)
{
	if (A.first > A.second) swap(A.first,A.second);
	if (Dis[A.first][B.first] <= 1 ) return 1;
	if (Dis[A.first][B.second] <= 1 ) return 1;
	if (Dis[A.second][B.first] <= 1 ) return 1;
	if (Dis[A.second][B.second] <= 1 ) return 1;
	return 2;
}

void DFS(int A)
{
	Mark[A] = 1;
	for (int i=0;i<Graf[A].size();i++)
	{
		if (Mark[ Graf[A][i] ] == 0)
		{		
		LLD T = S;
		for (int j=0;j<Kraw.size();j++)
			if ( Odlg( make_pair( A, Graf[A][i] ), Kraw[j] ) <= 1 )
				T--;

		if (T<0) T = 0;
		Wynik *= T;
		Wynik %= MOD;

		int B = Graf[A][i];
		Kraw.push_back( make_pair( min(A, B), max(A,B)) );
		}
	}
	for (int i=0;i<Graf[A].size();i++)
		if (Mark[Graf[A][i]]==0)
			DFS(Graf[A][i]);
}

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int L=1;L<=lw;L++)
	{
		int n;
		scanf("%d%Ld",&n,&S);

		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				Dis[i][j] = 10000000;
		
		for (int i=1;i<=n;i++)
		{
			Graf[i].clear();
			Mark[i] = 0;
			Dis[i][i] = 0;
		}
		Kraw.clear();

		for (int i=0;i<n-1;i++)
		{
			int A,B;
			scanf("%d%d",&A,&B);
			Graf[A].push_back(B);
			Graf[B].push_back(A);
			Dis[A][B] = Dis[B][A] = 1;
		}

		Wynik = 1;

		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					Dis[i][j] = min(Dis[i][j],Dis[i][k]+Dis[k][j]);

		DFS(1);

		printf("Case #%d: %Ld\n",L,Wynik);
		
	}

	return 0;
}
