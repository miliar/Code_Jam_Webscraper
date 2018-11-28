#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <string>
#include <sstream>
#include <iomanip>
#include <cmath>

#define MAX 100100
#define INF 1000000000

using namespace std;
typedef long long LL;
typedef vector<LL> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VC> MC;

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int L,N,C;
		LL t;
		cin>>L>>t>>N>>C;

		LL sumaAll=0;

		VI X(C),V(N),Ostatnie;
		for (int i=0; i<C; ++i) cin>>X[i];
		for (int i=0; i<N; ++i)
		{
			V[i]=X[i%C];
			sumaAll+=V[i]*2;
			if (sumaAll>=t)
			{
				if (Ostatnie.empty())
				{
					LL ile=(sumaAll-t)/2;
					Ostatnie.push_back(ile);
				}
				else Ostatnie.push_back(V[i]);
			}
		}
		sort(Ostatnie.begin(),Ostatnie.end(),greater<int>());
		if ((int)Ostatnie.size()>L) Ostatnie.resize(L);

		LL suma=0;
		for (int i=0; i<(int)Ostatnie.size(); ++i) suma+=Ostatnie[i];

		LL wynik=sumaAll-suma;
		cout<<"Case #"<<test<<": "<<wynik<<endl;
		
	}
	return 0;
}
