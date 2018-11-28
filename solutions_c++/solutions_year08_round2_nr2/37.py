#include <iostream>
#include <queue>
#include <cstdio>
#include <vector>

#define pb push_back
#define mp make_pair

using namespace std;

vector<long long> GN;
vector<int> primes;

void init(void)
{
    primes.pb(2);
    for(int i=3;i<=1000000;i+=2)
    {
	bool fail=false;
	for(int j=0;j<primes.size();j++)
	{
	    if((long long)primes[j] * primes[j] > i) break;
	    if(i % primes[j] == 0)
	    {
		fail = true;
		break;
	    }
	}
	if(!fail) primes.pb(i);
    }
}

bool merge(int a,int b)
{
    if(GN[a] == GN[b])
	return false;

    int mother=b;
    while(GN[mother] != mother)
    {
	mother = GN[mother];
    }

    while(GN[b] != b)
    {
	int tmp;
	tmp = b;
	b = GN[b];
	GN[tmp] = mother;
    }

    mother = a;
    while(GN[mother] != mother)
    {
	mother = GN[mother];
    }

    while(GN[a] != a)
    {
	int tmp;
	tmp = a;
	a = GN[a];
	GN[tmp] = mother;
    }

    if(GN[a] == GN[b])
	return false;

    GN[a] = GN[b];
    return true;
}

void process(int t)
{
    long long a,b,p;
    cin >> a >> b >> p;

    GN.clear();

    for(int i=a;i<=b;i++)
    {
	GN.push_back(i-a);
    }

    long long ret = b-a+1;

    for(int i=0;i<primes.size();i++)
    {
	if(primes[i] < p) continue;
	long long first = ((a+primes[i]-1)/primes[i]) * primes[i];
	for(long long j=first;j<=b;j+=primes[i])
	{
//	    cout << "merge " << first << " " << j << endl;
	    if(merge(first - a, j - a))
	    {
		ret--;
	    }
	}
    }

    cout << "Case #" << t << ": " << ret << endl;
}

int main(void)
{
    init();
    int T;
    cin >> T;
    for(int i=1;i<=T;i++)
	process(i);
}
