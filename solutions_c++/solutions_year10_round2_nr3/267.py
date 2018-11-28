#include<set>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;

ifstream in("plik.in");
ofstream out("plik.out");

int DP[600][600], bin[600][600];
const int modulo = 100003;

int binomial(int n, int k)
{
	if(k < 0 || k > n) return 0;
	if(k == 0 || k == n) return 1;
	if(bin[n][k] >= 0) return bin[n][k];
	return bin[n][k] = (binomial(n - 1, k) + binomial(n - 1, k - 1)) % modulo;
}

int rek(int n, int k)
{
	if(n <= 1 || k < 1 || n <= k) return 0;
	if(k == 1) return 1;

	int &ret = DP[n][k];

	if(ret >= 0) return ret;
	ret = 0;

	for(int i = 1; i < k; ++i)
	{
		if(n == 8 && k == 4)
		{
		//	cout << i << " " << rek(k, i) << " " << n-k-1 << " " << k-i-1 << " " << binomial(n-k-1, k-i-1) << "\n";
		}
		ret = (ret + rek(k, i) * 1LL * binomial(n - k - 1,  k - i - 1)) % modulo;
	}
	return ret;
}

int lecim(int n)
{
	int ret = 0;
	for(int i = 1; i < n; ++i)
	{
		//cout << n << " " << i << " " << rek(n, i) << "\n";
		ret = (ret + rek(n, i)) % modulo;
	}
	return ret;
}

int byl[30];

void verify(int N, int ret)
{
	if(byl[N] >= 0) return ;
	int tab[30], akt, wynik = 0, wart;
	//int ile[50];
	//memset(ile, 0, sizeof(ile));
	for(int i = (1<<(N-2)); i < (1<<(N-1)); ++i)
	{
		akt = 0;
		for(int j = 0; j < N - 1; ++j) if((i>>j)&1) tab[akt++] = j + 2;
		bool ok = true;
		
		wart = N;
		while(ok)
		{
			int nakt = 0;
			while(tab[nakt] != wart) ++nakt;
			if(nakt == 0) break;
			wart = nakt + 1;
			if(!((i>>(wart - 2))&1)) ok = false;
		}
		/*if(ok && N == 8)
		{
			for(int i = 0; i < akt; ++i) cout << tab[i] << " "; cout << "\n";
			ile[akt]++;
		}*/
		wynik += ok;
	}
	/*if(N == 8)
	{
		for(int i = 1; i < 8; ++i) cout << i << " --- " << ile[i] << "\n";
	}*/
	cout << N << ": ";
	wynik %= modulo;
	if(wynik != ret)
	{
		cout << wynik << " " << ret << "\n";
	} else
		cout << "OK\n";
	byl[N] = wynik;
}
	
int main()
{
	int t;
	int N;
	in >> t;

	memset(DP, -1, sizeof(DP));
	memset(bin, -1, sizeof(bin));
	memset(byl, -1, sizeof(byl));

	//rek(8, 4);
	//cin >> N;
	//return 0;
	for(int i = 1; i <= t; ++i)
	{
		in >> N;
		out << "Case #" << i << ": " << lecim(N) << "\n";

		//verify(N, lecim(N));
	}
	in.close();
	out.close();
	//cin >> N;
	return 0;
}