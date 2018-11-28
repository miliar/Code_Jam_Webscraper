#include <iostream>
#include <string>
#include <cassert>

using namespace std;

#define MAXN 1024

int n[MAXN];

int p[MAXN];
int r[MAXN];

int maxfactor[MAXN];

char isPrime[MAXN];

int seen[MAXN];

void make_set(int x)
{
	p[x] = x;
	r[x] = 1;
}

int find(int x)
{
	if (p[x] == p[p[x]]) return p[x];
	else return (p[x] = find(p[x]));
}

void link(int x, int y)
{
	if (r[x] > r[y])
		p[y] = p[x];
	else
	{
		p[x] = p[y];
		if (r[x] == r[y])
			r[y]++;
	}
}


void Union(int x, int y)
{
	link(find(x), find(y));
}

int gcd(int x, int y){
	if (y == 0)
		return x;
	else
		return gcd(y, x % y);
}

int main(){
	int N;

	cin >> N;

	/* Crivello di Eratostene fino a 4n */
	for (int i = 2; i <= MAXN; i++)
		isPrime[i] = 1;

	for (int i = 2; i*i <= MAXN; i++)
		if (isPrime[i])
			for(int j = 2*i; j <= MAXN; j += i)
				isPrime[j] = 0;



	for(int i = 2; i <= MAXN; i++){
		for(int j = i; ; j--){
			if (isPrime[j] && ((i % j) == 0)){
				maxfactor[i] = j; break;
			}
		}
	}


	for(int Case = 1; Case <= N; Case++){
		int A, B, P;
		cin >> A >> B >> P;
		int len = B - A + 1;
		for(int i = 0; i < len; i++)
			n[i] = A+i;

		for(int i = 0; i < len; i++)
			make_set(i);


		for(int i = 0; i < len; i++){
			for(int j = i+1; j < len; j++){
				int g = gcd(n[i], n[j]);

				if (g == 1)
					continue;

				if (maxfactor[g] >= P)
					Union(i, j);
			}
		}

		for(int i = 0; i < len; i++){
			seen[i] = 0;
		}

		int count = 0;
		for(int i = 0; i < len; i++){
			int f = find(i);
			//cout << "find(" << n[i] << ") = " << f << endl;
			if(!seen[f]){
				++count;
				seen[f] = 1;
			}
		}

		cout << "Case #" << Case << ": " << count << endl;
	}
	return 0;
}
