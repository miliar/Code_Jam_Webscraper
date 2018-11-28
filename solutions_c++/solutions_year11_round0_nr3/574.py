#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 23

using namespace std;
typedef vector<int> VI;

int main()
{
	ios_base::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int N,suma=0; cin>>N;
		VI V(N);
		for (int i=0; i<N; ++i)
		{
			cin>>V[i];
			suma+=V[i];
		}
		sort(V.begin(),V.end());

		bool Tab[MAX]={};
		bool ok=true;
		for (int i=0,maska=1; i<MAX; ++i,maska<<=1)
		{
			for (int j=0; j<(int)V.size(); ++j)
			{
				bool bit=((V[j]&maska)!=0);
				Tab[i]^=bit;		
			}
			if (Tab[i]) ok=false;
		}
		if (ok)
		{
			int wynik=suma-V.front();
			cout<<"Case #"<<test<<": "<<wynik<<endl;
		}
		else cout<<"Case #"<<test<<": NO"<<endl;
	}
	return 0;
}