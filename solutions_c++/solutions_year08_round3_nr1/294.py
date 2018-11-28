#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

int N,P,K,L;

struct Fre
{
	int index;
	int freq;
}LP[1010];

int PP[1100];

bool cmp(int &a, int &b)
{
	return a>b;
}

int main()
{
	cin >> N;
	long long ss = 1;
	while(N--)
	{
		cin >> P >> K >> L;

		for(int i = 0; i< L; ++i)
		{
			cin >> PP[i];
		}
		sort(PP,PP+L,cmp);
		long long bei = L/K;
		long long yu = L%K;
		long long t = 0;
		long long ans = 0;
		while(t<bei)
		{
			long long sum = 0;
			for(int i = 0; i< K; ++i)
			{
				sum += PP[i+t*K];
			}
			t++;
			ans += t*sum;
		}
		t++;
		for(int i = 0; i< yu; ++i)
		{
			ans += t*PP[L-i-1];
		}
		cout << "Case #" << ss++ << ": ";
		cout << ans << endl;
	}
	return 0;
}