#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#include <iostream>
#include <vector>
#include <algorithm>

typedef vector<int> VI;
typedef pair<int,int> PII;

// return a % b (positive value)
int mod(int a, int b) {
  return ((a%b)+b)%b;
}

// computes gcd(a,b)
int gcd(int a, int b) {
  int tmp;
  while(b){a%=b; tmp=a; a=b; b=tmp;}
  return a;
}

// computes lcm(a,b)
int lcm(int a, int b) {
  return a/gcd(a,b)*b;
}

// returns d = gcd(a,b); finds x,y such that d = ax + by
int extended_euclid(int a, int b, int &x, int &y) {  
  int xx = y = 0;
  int yy = x = 1;
  while (b) {
    int q = a/b;
    int t = b; b = a%b; a = t;
    t = xx; xx = x-q*xx; x = t;
    t = yy; yy = y-q*yy; y = t;
  }
  return a;
}

// finds all solutions to ax = b (mod n)
VI modular_linear_equation_solver(int a, int b, int n) {
	a=((a%n)+n)%n;
	b=((b%n)+n)%n;
  int x, y;
  VI solutions;
  int d = extended_euclid(a, n, x, y);
  if (!(b%d)) {
    x = mod (x*(b/d), n);
    for (int i = 0; i < d; i++)
      solutions.push_back(mod(x + i*(n/d), n));
  }
  return solutions;
}

// computes b such that ab = 1 (mod n), returns -1 on failure
int mod_inverse(int a, int n) {
  int x, y;
  int d = extended_euclid(a, n, x, y);
  if (d > 1) return -1;
  return mod(x,n);
}

// Chinese remainder theorem (special case): find z such that
// z % x = a, z % y = b.  Here, z is unique modulo M = lcm(x,y).
// Return (z,M).  On failure, M = -1.
PII chinese_remainder_theorem(int x, int a, int y, int b) {
  int s, t;
  int d = extended_euclid(x, y, s, t);
  if (a%d != b%d) return make_pair(0, -1);
  return make_pair(mod(s*b*x+t*a*y,x*y)/d, x*y/d);
}

// Chinese remainder theorem: find z such that
// z % x[i] = a[i] for all i.  Note that the solution is
// unique modulo M = lcm_i (x[i]).  Return (z,M).  On 
// failure, M = -1.  Note that we do not require the a[i]'s
// to be relatively prime.
PII chinese_remainder_theorem(const VI &x, const VI &a) {
  PII ret = make_pair(a[0], x[0]);
  for (int i = 1; i < x.size(); i++) {
    ret = chinese_remainder_theorem(ret.first, ret.second, x[i], a[i]);
    if (ret.second == -1) break;
  }
  return ret;
}

// computes x and y such that ax + by = c; on failure, x = y =-1
void linear_diophantine(int a, int b, int c, int &x, int &y) {
  int d = gcd(a,b);
  if (c%d) {
    x = y = -1;
  } else {
    x = c/d * mod_inverse(a/d, b/d);
    y = (c-a*x)/b;
  }
}

int d, n;
int a[16];
bool sieve[1048576];
const int lim=1000000;
vector<int> primes;

bool f_okay(int aa, int bb, int p)
{
	int i;
	for(i=0;i<n;i++)
	{
		if((aa*a[i]+bb)%p!=a[i+1]) return false;
	}
	return true;
}

int f_get(int p)
{
	int i;
	for(i=0;i<=n;i++)
	{
		if(p<=a[i]) return -1;
	}
	int ret=-1, tmp;
	for(i=2;i<=n;i++)
	{
		VI as=modular_linear_equation_solver(a[i-1]-a[i-2], a[i]-a[i-1], p);
		int aa, bb;
		aa=((as[0]%p)+p)%p; bb=(((a[i-1]-aa*a[i-2])%p)+p)%p;
		tmp=(((aa*a[n]+bb)%p)+p)%p;
		if(ret==-1) ret=tmp;
		else if(ret!=tmp){ret=-1; break;}
	}
	return ret;
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j;
	int t, tc;
	int e;
	int res, tmp;
	sieve[1]=true;
	primes.push_back(2);
	for(i=2;i<=lim;i+=2) sieve[i]=true;
	for(i=3;i<=lim;i+=2)
	{
		if(sieve[i]) continue;
		primes.push_back(i);
		for(j=i;j<=lim;j+=i) sieve[j]=true;
	}
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d", &d, &n);
		n--;
		for(i=0;i<=n;i++) fscanf(fp, "%d", &a[i]);
		e=1;
		for(i=1;i<=d;i++) e*=10;
		if(n>=1 && a[n]==a[n-1]) res=a[n];
		else res=-1;
		for(i=0;i<primes.size() && primes[i]<=e;i++)
		{
			tmp=f_get(primes[i]);
			if(tmp==-1) continue;
			if(res==-1) res=tmp;
			else if(res!=tmp){res=-1; break;}
		}
		fprintf(ofp, "Case #%d: ", t);
		if(res==-1) fprintf(ofp, "I don't know.\n");
		else fprintf(ofp, "%d\n", res);
		printf("%d\n", res);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
