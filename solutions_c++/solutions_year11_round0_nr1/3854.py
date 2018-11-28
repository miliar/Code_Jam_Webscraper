#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main()
	{
	freopen("A-large.in", "rt", stdin);
	freopen("ki.txt", "wt", stdout);
	int testcases,n,mit,Ohelye,Bhelye,Oszam,Bszam,t,Opush,Bpush;
	char ki;

	cin >> testcases;
	t=testcases;
	while (t--)
		{
		Ohelye=1;Bhelye=1;Oszam=0;Bszam=0,Opush=0;Bpush=0;
		cin >> n;
		while (n--)
			{
			cin >> ki;
			cin >> mit;
			if (ki=='O')
				{				
				Oszam=max(Oszam+abs(mit-Ohelye)+1,Bszam+1);
				Ohelye=mit;
				}
			else
				{
				Bszam=max(Bszam+abs(mit-Bhelye)+1,Oszam+1);
				Bhelye=mit;
				}
			}
		cout << "Case #"<<testcases-t<<": "<<max(Oszam,Bszam)<<endl;
		}
	}
