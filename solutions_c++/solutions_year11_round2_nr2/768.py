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
		double maxTime=0;

		int C,D; cin>>C>>D;
		VI V(C),R(C),SUMA(C);
		for (int i=0; i<C; ++i)
		{
			cin>>V[i]>>R[i];
			if (i==0) SUMA[i]=R[i];
			else SUMA[i]=SUMA[i-1]+R[i];
		}

		for (int i=0; i<C; ++i)
		{
			for (int j=i; j<C; ++j)
			{
				int ile;
				if (j==i) ile=R[i]-1;
				else if (i==0) ile=SUMA[j]-1;
				else ile=SUMA[j]-SUMA[i-1]-1;

				double needDist=ile*D;
				double dist=V[j]-V[i];
				if (dist>=needDist) continue;

				double roznica=needDist-dist;
				double time=roznica/2;
				maxTime=max(time,maxTime);
			}
		}
		cout<<"Case #"<<test<<": "<<maxTime<<endl;
	}

	return 0;
}