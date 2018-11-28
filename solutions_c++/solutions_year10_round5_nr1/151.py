// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)

//string split given string a and delimiters
vs strsp(string a, string delim=" ")
{
  vs ret;
  string cr = "";
  for(int i = 0; i < a.size(); i++)
  {
    if(delim.find(a[i])==string::npos) cr += a[i];
    else { if(cr.size()) ret.push_back(cr); cr = ""; }
  }
  if(cr.size()) ret.push_back(cr);
  return ret;
}
//long long gcd using Euclid
long long gcd(long long a, long long b)
{
	long long tmp = 0;
	while(b != 0)
	{
		tmp = b;
		b = a % b;
		a = tmp;
	}
	return a;
}
//long long egcd
//if original arguments are X,M then X*first - M*second = 1, so X*first = 1 mod M
pair<long long, long long> egcd(long long a, long long b)
{
	if(a % b == 0)
	{
		return make_pair(0,1);
	}
	else
	{
		pair<long long, long long> ret = egcd(b,a%b);
		long long Q = a / b;
		return make_pair(ret.second, ret.first - ret.second * Q);
	}
}

inline long long inverse(int num,int mod)
{
	return (egcd(num,mod).first+mod)%mod;
}

int main()
{
	int T;
	cin >> T;
	vector<long long> primes;
	primes.push_back(2);
	for(int i = 3; i <= 1000005; i++)
	{
		int ok = 1;
		for(int j = 0; j < primes.size(); j++)
		{
			if(primes[j]*primes[j] > i) break;
			if(i%primes[j] == 0)
			{
				ok = 0;
				break;
			}
		}
		if(ok == 1) primes.push_back(i);
	}
	
	for(int tcase = 1; tcase <= T; tcase++)
	{
		int D,K;
		cin >> D >> K;
		long long seq[K], mxs = 0;
		for(int i = 0; i < K; i++)
		{
			cin >> seq[i];
			if(seq[i] > mxs) mxs = seq[i];
		}

		if(K == 1)
		{
			printf("Case #%d: I don't know.\n",tcase);
			continue;
		}
		else if(K == 2)
		{
			if(seq[0] == seq[1])
			{
				printf("Case #%d: %lld\n",tcase,seq[0]);
			}
			else
			{
				printf("Case #%d: I don't know.\n",tcase);
			}
			continue;
		}
		
		int mx = 1;
		for(int i = 0; i < D; i++) mx *= 10;

		long long ans = -1;
		for(int i = 0; i < primes.size(); i++)
		{
			if(primes[i] > mx) break;
			if(primes[i] <= mxs) continue;
			
			long long cp = primes[i];
			int ok = 1;
			long long cra = -1;
			
			for(int i = 1; i < K-1; i++)
			{
				long long neua = inverse((seq[i]-seq[i-1]+cp)%cp,cp);
				
				neua %= cp;
				neua *= ((seq[i+1]-seq[i]+cp)%cp);
				neua %= cp;
				if(neua < 0) deb("FAIL3");
				if(cra == -1 || neua == cra)
				{
					cra = neua;
				}
				else
				{
					cra = -2;
					break;
				}
			}
			if(cra == -2) continue;
			//printf("%d --> %d\n",cp,cra);
			long long bs = -1;
			for(int i = 1; i < K; i++)
			{
				long long neub = seq[i] - ( (seq[i-1]*cra) % cp );
				neub = (neub+cp)%cp;
				if(neub < 0) deb("FAIL1");
				if(bs == -1 || neub == bs)
				{
					bs = neub;
				}
				else bs = -2;
			}
			if(bs == -2) continue;
			//printf("%d --> %d %d\n",cp,cra,bs);

			long long neuans = (seq[K-1]*cra+bs+cp)%cp;
			if(neuans < 0) deb("FAIL");
			if(ans == -1 || neuans == ans)
			{
				ans = (seq[K-1]*cra+bs)%cp;
			}
			else ans = -2;
		}
		if(ans == -2)
		{
			printf("Case #%d: I don't know.\n",tcase);
		}
		else
		{
			printf("Case #%d: %lld\n",tcase,ans);
		}
	}
	return 0;
}
