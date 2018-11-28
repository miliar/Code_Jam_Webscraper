#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;
typedef long long ll;

int main(int argc, char** argv)
{
	FILE *iFile, *oFile;
	freopen_s(&iFile, argv[1], "rt", stdin);
	freopen_s(&oFile, "result.txt", "wt", stdout);
	int num_case;
	cin >> num_case;

	for(int c=0; c<num_case; c++)
	{
		int P,K,L;
		cin >> P >> K >> L;
		vector<ll> f;
		ll tmp;
		for(int i=0; i<L; i++)
		{
			cin >> tmp;
			f.push_back(tmp);
		}
		sort(f.begin(),f.end(), greater<ll>());
		//for(int i=0; i<f.size(); i++)
		//	cerr << f[i] << ",";
		//cerr <<endl;

		int p=1, k=1;
		ll press=0;
		for(int i=0; i<L; i++)
		{
			press += f[i]*p;

			if(k<K) 
				++k;
			else
			{
				k=1;
				++p;
			}
		}
	
		cout << "Case #" << c+1 << ": " << press << endl;
	}

	fclose(iFile);
	fclose(oFile);
	return 0;
}
