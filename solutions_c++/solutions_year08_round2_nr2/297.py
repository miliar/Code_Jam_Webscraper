#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <set>
#include <iterator>
#include <iomanip>
#include <cmath>
#include <map>

using namespace std;

vector<int> primes;

#define NN 3000001 //nombre maximal d'éléments (numérotés de 0 à NN-1), à régler

struct element {
  long long int pere, rang;
};

element compo[NN];

//donne le représentant de la composante connexe de l'element e
long long int representant(long long int e) {
  if (compo[e].pere == e) return e;
  compo[e].pere = representant(compo[e].pere);
  return compo[e].pere;
}

//a et b sont les représentants des composantes connexes
void make_union(long long int a, long long int b) {
  if (a==b) return;
  if (compo[a].rang > compo[b].rang)
    compo[b].pere = a;
  else
    {
      compo[a].pere = b;
      if (compo[a].rang == compo[b].rang) {
	compo[b].rang++;
      }
    }
}

//initialise la composante connexe à l'aide de l'élément e
void init(long long int e) {
  compo[e].pere = e;
  compo[e].rang = 0;
}



#define N 1000000
unsigned int prime[N / 64];
#define gP(n) (prime[n>>6]&(1<<((n>>1)&31)))
#define rP(n) (prime[n>>6]&=~(1<<((n>>1)&31)))
void sieve()
{
    memset( prime, -1, sizeof( prime ) );

    unsigned int i;
    unsigned int sqrtN = ( unsigned int )sqrt( ( double )N ) + 1;
    for( i = 3; i < sqrtN; i += 2 ) if( gP( i ) )
    {
        unsigned int i2 = i + i;
        for( unsigned int j = i * i; j < N; j += i2 ) rP( j );
    }
}

int factor(long long int A, long long int B, long long int P) {
	for (int i=0;i<primes.size();i++) {
		if (primes[i] >= P) init(primes[i]);
	}
	
	map<long long int,int> largePrimes;
	
	for (int j=0;j<primes.size();j++) init(B-A+j);
	
	for (long long int i = A; i <= B ; i++) {
		long long int n = i;
		
	//	cout << i << endl;
		
		init(i-A);	
						
		for (int j=0; j<primes.size() && n>1; j++) {
			if (n%primes[j] == 0) {
				n /= primes[j];
				if (primes[j] >= P) make_union(representant(i-A), representant(B-A+j));
			} 
			
			while (n%primes[j] == 0) n /= primes[j];
		}
		
		if (n>sqrt(i)) // n is now prime and >= P
		{
			int index;
			if (largePrimes.find(n) == largePrimes.end()) 
			{
				int index = largePrimes.size();
				largePrimes[n]=index;
				init(2*N + index);
			}
		 	else {
				index = largePrimes[n];
			}
			
			make_union(representant(i-A), representant(2*N+index));
		}
	}
}

int main()
{
	int C;
	cin >> C;
	
	sieve();
	
	primes.push_back(2);
	
	for (int i=1;i<N/2-1;i++) if (gP(2*i+1)) primes.push_back(2*i+1); 

	//copy(primes.begin(), primes.end(), ostream_iterator<int>(cout, " "));
	
	for (int c=0;c<C;c++) {
		
		long long int A, B, P;
		cin >> A >> B >> P;

		factor(A, B, P);
		
		set<int> rep;
		
		for (long long int i=A;i<=B;i++) {
			rep.insert(representant(i-A));
		}
		
		cout << "Case #" << c+1 << ": " << rep.size() << endl;
	}
}
