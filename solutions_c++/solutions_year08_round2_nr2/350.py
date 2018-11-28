#include <iostream>
#include <math.h>

using namespace std;

#define MAX 4000

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

struct set{
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

long long gcd(long long a, long long b) {
	while(b)  std::swap(a%=b, b);	
	return a;
}

int main(){
	int C; cin >> C;
	doCrivo();
	for (int tc = 1; tc <= C; tc++) {
		int A, B, P; cin >> A >> B >> P;
		set s; s.init (B - A + 1);
		int count = 0;
				
		for (int i = A; i < B; i++) {
			for (int j = i+1; j <= B; j++) {
				if (gcd(i, j) >= P) {
					for (int k = 0; k < pCount; k++) {
						if (i % primes[k] == 0 && j % primes[k] == 0 && primes[k] >= P) {
							s.union_set(i - A, j - A);
							break;
						}
					}
				}
			}
		}
		
		for (int i = 0; i <= B - A; i++)  {
			if (s.find_set(i) == i) count ++;
		}
		cout << "Case #" << tc << ": " << count << endl;
	}
	
	return 0;
}