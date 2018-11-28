#include <iostream>
#include <string>
#include <math.h>

using namespace std;
typedef long long ll;

ll pos[50];
ll vel[50];
ll N,K,B,T;

int main()
{
	ll t;
	cin >> t;
	for(int a =1;a<=t;a++)
	{
		cin>>N>>K>>B>>T;

		for(int n=N-1;n>=0;n--)
		{
			cin >> pos[n];
		}
		for(int n=N-1;n>=0;n--)
		{
			cin >> vel[n];
		}
		if(K==0)
		{
			cout << "Case #" << a << ": 0" << endl;
			continue;
		}
		int fin=0;
		int swaps=0;
		int blocks=0;
		for(int n=0;n<N;n++)
		{
			if(B > pos[n]+T*vel[n])
			{
				blocks++;
			}
			else
			{
				swaps+=blocks;
				fin++;
				//cout<<fin<<endl;
				if(fin == K)
				{
					cout << "Case #" << a << ": " << swaps << endl;
					break;
				}
			}
		}
		if(fin < K)
			cout << "Case #" << a << ": IMPOSSIBLE" <<endl;
	}
}
