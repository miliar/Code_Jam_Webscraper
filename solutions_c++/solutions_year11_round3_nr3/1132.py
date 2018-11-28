#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int TC = 1, T, NC = 1, N, L, H;
//unsigned __int64 L, H;
int other[100];

int main ()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
//	memset(vs, 0 , 10000*sizeof(int));
	for (cin>>T; TC <= T; TC++)
    {
		int k = 0;
		for (cin>>N>>L>>H, NC = 0; NC < N; NC++)
		{
			cin>>other[NC];

		}
		int freq, can = 0;
		for (freq = L; freq<=H; freq++)
		{
			int flag = 1;
			for (NC = 0; NC < N && flag; NC++)
				if (freq % other[NC] && other[NC] % freq) flag = 0;
			if (flag)
			{
				cout<<"Case #"<<TC<<": "<<freq<<endl;
				can = 1; break;
			}
		}
		if (can == 0)
		cout<<"Case #"<<TC<<": "<<"NO"<<endl;
    }
	fclose(stdin);
	fclose(stdout);
    return 0;
}

