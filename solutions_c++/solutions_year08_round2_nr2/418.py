// Jacek Migdal 2008 Google code jam
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

//const int MAX = 1000000;
const int MAX = 1000;

vector<int> primes;
void prepare() {
	primes.push_back(2);
	for( int i = 3 ; i<MAX ; i+=2 ) {
		int j;
		for( j = 1 ; j<primes.size() ; j++ ) 
			if( i%primes[j]==0 )
				break;
		if(j==primes.size())
			primes.push_back(i);
	}
}

vector<int> parent;
int get( int w ) {
	if( parent[w]!=w ) {
		parent[w] = get(parent[w]);
	}
	return parent[w];
}

void merge( int a, int b ) {
	a = get(a);
	b = get(b);
	parent[b] = a;
}

void doIt() {
	int A, B, P;
	scanf( "%d %d %d", &A, &B, &P );
	int begin = 0;
	while(begin<primes.size() && primes[begin]<P )
		begin++;

	parent = vector<int>(B-A+1);
	for( int i = A ; i<=B ; i++ )
		parent[i-A] = (i-A);

	for( int j = begin ; j<primes.size()  ; j++ ) {
		int first = A+(primes[j]-A%primes[j])%primes[j];
		for( int i = first+primes[j] ; i<=B ; i+=primes[j] ) {
			merge( first-A, i-A );
		}
	}

	int result = 0;
	for( int i = 0 ; i<parent.size() ; i++ )
		if( i==parent[i] )
			result++;

	printf("%d\n", result);
}

int main() {
	prepare();
	int nTests;
	scanf( "%d", &nTests);
	for( int i = 0 ; i<nTests ; i++ ) {
		printf("Case  #%d: ", i+1);
		doIt();
	}
	return 0;
}


