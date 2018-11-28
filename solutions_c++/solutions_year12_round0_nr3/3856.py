#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int A, B, lc, tn;
long long wynik;
char V[10], X[10];
vector<pair<int, int> > S;

void check(void)
{
	int k;
	for(int p=0; p+2<=lc; p++)
	{
		for(int i=1; i<=lc; i++)
			X[i] = V[(i+p)%lc+1];
		k = 0;
		for(int i=1; i<=lc; i++)
		{
			k += X[i];
			k *= 10;
		}
		k /= 10;
		
		if(k>tn && k<=B)
		{
			//printf("(%d>%d)\n", k, tn);
			S.push_back(make_pair(tn, k));
			//wynik++;
		}
	}
	return;
}

void l_c(void)
{
	if(A < 10)
		lc = 1;
	else
	if(A < 100)
		lc = 2;
	else
	if(A < 1000)
		lc = 3;
	else
	if(A < 10000)
		lc = 4;
	else
	if(A < 100000)
		lc = 5;
	else
	if(A < 1000000)
		lc = 6;
	else
	if(A < 10000000)
		lc = 7;
	return;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		wynik = 0ll;
		scanf("%d %d", &A, &B);
		l_c();
		for(int n=A; n<=B; n++)
		{
			tn = n;
			for(int i=lc; i>=1; i--)
			{
				V[i] = tn%10;
				tn /= 10;
			}
			//printf("\n");
			//for(int i=1; i<=lc; i++)
				//printf("%d", V[i]);
			//printf(": ");
			tn = n;
			check();
		}
		sort(S.begin(), S.end());
		S.erase(unique(S.begin(), S.end()), S.end());
		wynik = S.size();
		printf("Case #%d: %lld\n", t, wynik);
		S.clear();
	}
	return 0;
}
