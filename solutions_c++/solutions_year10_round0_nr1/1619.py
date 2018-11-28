// Started 1.30pm, fin 3pm
#include <iostream>
#include <utility>
#include <algorithm>
#define for0(i,n) for(int i = 0; i < n; i ++)

using namespace std;


#define POWERED 1
#define ON 2

int xs[10000][3];
int kasenums[10000];
int cmp(int k0, int k1)
{
	return xs[k0][1] < xs[k1][1];
}

int main()
{
	int kases; cin >> kases;
	for0(kase, kases)
	{
		kasenums[kase] = kase;
		cin >> xs[kase][0] >> xs[kase][1];
	}
	sort(kasenums, kasenums+kases, cmp);
	
	int N = 31, K = 100000000;
	
	int nextKase = 0;
	
	int* on = new int[N];
	for0(i,N) on[i] = 0;
	on[0] = POWERED;
	
	while (0 == xs[kasenums[nextKase]][1])
	{
		int nn = xs[kasenums[nextKase]][0];
		xs[kasenums[nextKase]][2] = ((on[nn-1] & POWERED) && (on[nn-1] & ON));
		nextKase ++;
	}
	for (int k=1; k <= K && nextKase < kases; k ++)
	{
		for0(n,N)
		{
			if(on[n] & POWERED) on[n] = on[n] ^ ON;
			
			if(n==0 || ((on[n-1] & POWERED) && (on[n-1] & ON)))
				on[n] = on[n] | POWERED;
			else if (on[n] & POWERED)
				on[n] = on[n] - POWERED;
		}
		while (k == xs[kasenums[nextKase]][1])
		{
			int nn = xs[kasenums[nextKase]][0];
			xs[kasenums[nextKase]][2] = ((on[nn-1] & POWERED) && (on[nn-1] & ON));
			nextKase ++;
		}
	}
	
	for0(kase, kases)
	{
		cout << "Case #" << (kase+1) << ": " << (xs[kase][2] ? "ON" : "OFF") << endl;
	}
}