#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

typedef long long int ll;

const int SIZE = 10000;

int main()
{
	ofstream out("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\a.out");
	ll i, j, k, N, otest;
	ll P, K, L, best;
	ll fq[SIZE];
	cin >> N;
	for(otest = 0; otest < N;)  {
		best = 0;
		cin >> P >> K >> L;
		for(i = 0; i < L; i++)
			cin >> fq[i];
		sort(fq, fq+L);
		for(i = 1, j = L-1; j >= 0 && i <= P; i++)
			for(k = K; j >=0 && k > 0; j--, k--) best += i*fq[j];
   		out << "Case #" << ++otest << ": " << best << endl;
	}
	system("pause");
	return 0;
}

