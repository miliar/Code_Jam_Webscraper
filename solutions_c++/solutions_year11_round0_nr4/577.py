#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef vector<int> VI;

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int N; cin>>N;
		VI V(N);

		for (int i=0; i<N; ++i) cin>>V[i];
		VI S=V;
		sort(S.begin(),S.end());

		int licznik=0;
		for (int i=0; i<N; ++i) if (V[i]!=S[i]) ++licznik;
			
		cout<<"Case #"<<test<<": "<<licznik<<endl;
	}
	return 0;
}