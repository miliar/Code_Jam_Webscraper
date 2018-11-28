
#include <iostream>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
#include <ctime>
#include <cctype>
using namespace std;

long long gcd(long long a, long long b) {
	while(b)  std::swap(a%=b, b);	
		return a;
}

#define MAX 2000
bool isprime[MAX];
int primes[MAX] , pCount = 0; // numero de primos e' muito inferior a MAX

void doCrivo()
{ 
	int i, j, root = (int) sqrt(MAX) + 1;
	memset(isprime , true , sizeof(isprime));
	isprime[0] = isprime[1] = false;

	for(i = 2; i < root; i++)
		if(isprime[i])
			for(j = i * i ; j < MAX ; j += i)
				isprime[j] = false;
	// Condensar
	for(i = 2 ; i < MAX ; i++)
		if(isprime[i])
			primes[pCount++] = i;
}

struct unionfind{
	int p[MAX],rank[MAX], number[MAX];
	int size;

	void init(int s){
		size = s;
		for (int i = 0; i < size; i++) 
		{p[i]=i; rank[i]=0; number[i]=1;}
	}

	void link(int x, int y) {
		if (rank[x] <= rank[y]) {
			p[x] = y;
			number[y] += number[x];
			if (rank[x] == rank[y])
				rank[y]++;
		} else link(y, x);
	}

	int find_set(int x) {
		if (x != p[x]) p[x] = find_set(p[x]);
		return p[x];
	}

	void union_set(int x,int y) {
		link(find_set(x), find_set(y));
	}
};

void solve(int testcase)
{
	int low, high, minimum;
	unionfind sets;
	sets.init(MAX);
	cin >> low >> high >> minimum;

	for (int i = low; i <= high; i++)
		for (int j = i+1; j <= high; j++)
				for (int k = 0; k < pCount; k++)
					if (primes[k] >= minimum && i%primes[k] == 0 && j%primes[k] == 0)
					{
						sets.union_set(i, j);
						break;
					}
	
	int total = 0;
	for (int i = low; i <= high; i++)
	{
		if (sets.find_set(i) == i)
			total++;
			}


	printf("Case #%d: %d\n", testcase, total);
}



int main()
{
	int n;
	cin >> n;
	doCrivo();
	for (int i = 0; i < n; i++)
		solve(i+1);
	return 0;
}
