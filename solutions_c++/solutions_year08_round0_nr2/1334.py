#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	vector <int> sA, aB, sB, aA;
	int n, j, k;

	cin >> n;

	for(int i=1; i<=n; ++i)
	{
		int delay, numA, numB;
		int hour, min;
		int descA=0, descB=0;

		sA.clear(); aB.clear(); sB.clear(); aA.clear();

		cin >> delay >> numA >> numB;

		for(j=0; j< numA; ++j)
		{
			scanf("%d:%d", &hour, &min);
			sA.push_back(hour * 60 + min);

			scanf("%d:%d", &hour, &min);
			aB.push_back(hour * 60 + min + delay);
		}

		for(j=0; j<numB; ++j)
		{
			scanf("%d:%d", &hour, &min);
			sB.push_back(hour * 60 + min);

			scanf("%d:%d", &hour, &min);
			aA.push_back(hour * 60 + min + delay);
		}

		sort(sA.begin(), sA.end());
		sort(aA.begin(), aA.end());

		sort(sB.begin(), sB.end());
		sort(aB.begin(), aB.end());

		for(j=0, k=0; j< aA.size() && k < sA.size() ;)
		{
			if( aA[j] <= sA[k] )
			{
				++k; ++j;
				descA++;
			}else
				++k;
		}

		for(j=0, k=0; j< aB.size() && k < sB.size();)
		{
			if( aB[j] <= sB[k] )
			{
				++k; ++j;
				descB++;
			}else
				++k;
		}

		cout << "Case #" << i << ": " << numA - descA << " " << numB - descB << endl;

	}

	return 0;
}
